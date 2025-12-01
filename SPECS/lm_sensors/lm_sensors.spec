# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _upstream_version 3-6-0
%define _version %(echo %{_upstream_version} | tr '-' '.')

Name:           lm_sensors
Version:        %{_version}
Release:        %autorelease
Summary:        Hardware monitoring tools
# Some man pages are licensed Linux-man-pages-copyleft-var and
# Linux-man-pages-copyleft (lib/sensors.conf.5, prog/sensors/sensors.1).
# Files from dist-git are licensed MIT.
# lib/* are LGPL-2.1-or-later.
# The rest is GPL-2.0-or-later.
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND Linux-man-pages-copyleft-var AND Linux-man-pages-copyleft AND MIT
URL:            http://github.com/lm-sensors/lm-sensors
#!RemoteAsset
Source0:        https://github.com/lm-sensors/lm-sensors/archive/V%{_upstream_version}/lm-sensors-%{_upstream_version}.tar.gz
Source1:        lm_sensors.sysconfig
# This one was taken from PLD-linux
Source2:        sensord.sysconfig
Source3:        lm_sensors-modprobe-wrapper
Source4:        lm_sensors-modprobe-r-wrapper
Source5:        sensord.service
Source6:        sensord-service-wrapper
Source7:        lm_sensors.service
Source8:        lm_sensors-wrapper

BuildSystem:    autotools
BuildRequires:  linux-headers
BuildRequires:  bison
BuildRequires:  libsysfs-devel
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  rrdtool-devel
BuildRequires:  gcc
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kmod
Requires:       systemd-units
%global  flags PREFIX=%{_prefix} LIBDIR=%{_libdir} MANDIR=%{_mandir} ETCDIR=%{_sysconfdir} EXLDFLAGS="$LDFLAGS" PROG_EXTRA=sensord BUILD_STATIC_LIB=0
BuildOption(build):  %flags user
BuildOption(install): %flags user_install

%patchlist
# Change PIDFile path from /var/run to /run
0001-Change-PIDFile-path-from-var-run-to-run.patch
# sensors-detect: Add support for AMD CPU Family 19h
0002-sensors-detect-Add-support-for-AMD-CPU-Family-19h.patch
# Flag allow-no-sensors added
0003-Flag-allow-no-sensors-added.patch
# rrd: adapt to constification of argv parameters
0004-lm_sensors-3.6.0-rrd-const-argv.patch

%description
lm_sensors (Linux-monitoring sensors), is a free open source software-tool
for Linux that provides tools and drivers for monitoring temperatures,
voltage, humidity, and fans. It can also detect chassis intrusions.

%package        libs
Summary:        lm_sensors core libraries
License:        LGPL-2.1-or-later

%description    libs
Core libraries for lm_sensors applications.

%package        devel
Summary:        Development files for programs which will use lm_sensors
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# One manual page is licensed Linux-man-pages-copyleft (lib/libsensors.3).
# The rest is LGPLv2+.
License:        LGPL-2.1-or-later AND Linux-man-pages-copyleft

%description    devel
The lm_sensors-devel package includes a header files and libraries for use
when building applications that make use of sensor data.

%package        sensord
Summary:        Daemon that periodically logs sensor readings
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# One man page is licensed Linux-man-pages-copyleft (prog/sensord/sensord.8).
# Files from dist-git are licensed MIT according to the FPCA. The rest is GPLv2+.
License:        GPL-2.0-or-later AND Linux-man-pages-copyleft AND MIT

%description    sensord
Daemon that periodically logs sensor readings to syslog or a round-robin
database, and warns of sensor alarms.

%prep -a

# Remove currently unused files to make sure we've got the license right
rm -f prog/init/sysconfig-lm_sensors-convert prog/hotplug/unhide_ICH_SMBus

mv prog/init/README prog/init/README.initscripts
chmod -x prog/init/fancontrol.init

# fixing the sensord-service-wrapper path
cp -p %{SOURCE5} sensord.service
cp -p %{SOURCE7} lm_sensors.service
sed -i "s|\@WRAPPER_DIR\@|%{_libexecdir}/%{name}|" sensord.service
sed -i "s|\@WRAPPER_DIR\@|%{_libexecdir}/%{name}|" lm_sensors.service

sed -i 's|CC := gcc|CC ?= gcc|' Makefile

# no configure
%conf

%install -a
ln -s sensors.conf.5.gz %{buildroot}%{_mandir}/man5/sensors3.conf.5.gz

mkdir -p -m 755 %{buildroot}%{_initrddir}
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/sensors.d
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/lm_sensors
install -pm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/sensord

# service files
mkdir -p %{buildroot}%{_unitdir}
install -pm 644 prog/init/fancontrol.service %{buildroot}%{_unitdir}
install -pm 644 lm_sensors.service           %{buildroot}%{_unitdir}
install -pm 644 sensord.service              %{buildroot}%{_unitdir}

# customized modprobe calls
mkdir -p %{buildroot}%{_libexecdir}/%{name}
install -pm 755 %{SOURCE3} %{buildroot}%{_libexecdir}/%{name}/lm_sensors-modprobe-wrapper
install -pm 755 %{SOURCE4} %{buildroot}%{_libexecdir}/%{name}/lm_sensors-modprobe-r-wrapper
install -pm 755 %{SOURCE8} %{buildroot}%{_libexecdir}/%{name}/lm_sensors-wrapper

# sensord service wrapper
install -pm 755 %{SOURCE6} %{buildroot}%{_libexecdir}/%{name}/sensord-service-wrapper

# no tests
%check

# ===== main =====
%post
%systemd_post lm_sensors.service
%preun
%systemd_preun lm_sensors.service
%postun
%systemd_postun_with_restart lm_sensors.service

# ==== sensord ===
%post sensord
%systemd_post sensord.service
%preun sensord
%systemd_preun sensord.service
%postun sensord
%systemd_postun_with_restart sensord.service

%files
%license COPYING
%doc CHANGES CONTRIBUTORS doc README*
%doc prog/init/fancontrol.init prog/init/README.initscripts
%config %{_sysconfdir}/sensors3.conf
%config(noreplace) %{_sysconfdir}/sysconfig/lm_sensors
%dir %{_sysconfdir}/sensors.d
%{_bindir}/*
%{_sbindir}/*
%{_unitdir}/lm_sensors.service
%{_unitdir}/fancontrol.service
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/lm_sensors-modprobe*wrapper
%{_libexecdir}/%{name}/lm_sensors-wrapper
%{_mandir}/man*
%exclude %{_sbindir}/sensord
%exclude %{_mandir}/man8/sensord.8.gz

%files libs
%license COPYING.LGPL
%{_libdir}/*.so.*

%files devel
%{_includedir}/sensors
%{_libdir}/lib*.so

%files sensord
%doc prog/sensord/README
%config(noreplace) %{_sysconfdir}/sysconfig/sensord
%{_sbindir}/sensord
%{_unitdir}/sensord.service
%{_libexecdir}/%{name}/sensord-service-wrapper
%{_mandir}/man8/sensord.8.gz

%changelog
%{?autochangelog}
