# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Summary:        Tools for monitoring SMART capable hard disks
Name:           smartmontools
Version:        7.5
Release:        %autorelease
License:        GPL-2.0-or-later
URL:            https://www.smartmontools.org/
VCS:            git:https://github.com/smartmontools/smartmontools.git
#!RemoteAsset
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        smartmontools.sysconf
Source2:        smartmontools.tmpfiles
BuildSystem:    autotools

BuildOption(conf):  --with-libcap-ng=yes
BuildOption(conf):  --with-libsystemd
BuildOption(conf):  --with-systemdsystemunitdir=%{_unitdir}
BuildOption(conf):  --sysconfdir=%{_sysconfdir}/%{name}/
BuildOption(conf):  --with-systemdenvfile=%{_sysconfdir}/sysconfig/%{name}
BuildOption(build):  CXXFLAGS="$RPM_OPT_FLAGS -fpie"
BuildOption(build):  LDFLAGS="-pie -Wl,-z,relro,-z,now"

BuildRequires:  make
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  automake
BuildRequires:  util-linux
BuildRequires:  groff
BuildRequires:  gettext
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  systemd
BuildRequires:  pkgconfig(systemd)

%description
The smartmontools package contains two utility programs (smartctl
and smartd) to control and monitor storage systems using the Self-
Monitoring, Analysis and Reporting Technology System (SMART) built
into most modern ATA and SCSI hard disks. In many cases, these
utilities will provide advanced warning of disk degradation and
failure.

%conf -p
autoreconf -fiv

%install -a
rm -f examplescripts/Makefile*
chmod a-x -R examplescripts/*
install -D -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/smartmontools
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/smartd_warning.d
install -p -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
rm -rf $RPM_BUILD_ROOT/etc/{rc.d,init.d}
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}

%preun
%systemd_preun smartd.service

%post
%systemd_post smartd.service

%postun
%systemd_postun_with_restart smartd.service

%files
%doc AUTHORS ChangeLog INSTALL NEWS README
%doc TODO examplescripts smartd.conf
%license COPYING
%dir %{_sysconfdir}/%name
%dir %{_sysconfdir}/%name/smartd_warning.d
%config(noreplace) %{_sysconfdir}/%{name}/smartd.conf
%config(noreplace) %{_sysconfdir}/%{name}/smartd_warning.sh
%config(noreplace) %{_sysconfdir}/sysconfig/smartmontools
%{_unitdir}/smartd.service
%{_sbindir}/smartd
%{_sbindir}/update-smart-drivedb
%{_sbindir}/smartctl
%{_tmpfilesdir}/%{name}.conf
%{_mandir}/man?/smart*.*
%{_mandir}/man?/update-smart*.*
%{_datadir}/%{name}
%{_sharedstatedir}/%{name}

%changelog
%autochangelog
