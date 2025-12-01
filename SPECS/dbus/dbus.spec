# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

# default without selinux
%bcond selinux 0

# default without systemd
%bcond systemd 0

Name:           dbus
Version:        1.16.2
Release:        %autorelease
Summary:        D-Bus Message Bus System
License:        AFL-2.1 OR GPL-2.0-or-later
URL:            https://dbus.freedesktop.org/
#!RemoteAsset
Source0:        https://dbus.freedesktop.org/releases/dbus/dbus-%{version}.tar.xz
Source1:        messagebus.conf

BuildSystem:    meson

BuildOption(conf): -Dasserts=false

%if %{with systemd}
BuildOption(conf): -Dsystemd=enabled
BuildOption(conf): -Dsystemd_system_unitdir=%{_unitdir}
BuildOption(conf): -Dsystemd_user_unitdir=%{_userunitdir}
%else
BuildOption(conf): -Dsystemd=disabled
%endif

%if %{with selinux}
BuildOption(conf): -Dselinux=enabled
%else
BuildOption(conf): -Dselinux=disabled
%endif

BuildOption(conf): -Dx11_autolaunch=disabled
BuildOption(conf): -Dxml_docs=disabled
BuildOption(conf): -Ddoxygen_docs=disabled
BuildOption(conf): -Dducktype_docs=disabled
BuildOption(conf): -Dqt_help=disabled
BuildOption(conf): -Dlibaudit=enabled
BuildOption(conf): -Dapparmor=disabled
BuildOption(conf): -Dkqueue=disabled
BuildOption(conf): -Dlaunchd=disabled
BuildOption(conf): -Dmodular_tests=disabled

BuildRequires:  meson
BuildRequires:  audit-devel libcap-ng-devel expat-devel >= 2.1.0 pkgconfig xmlto
%if %{with systemd}
BuildRequires:  pkgconfig(libsystemd) >= 209
%endif
%if %{with selinux}
BuildRequires:  libselinux-devel
%endif

Requires(post): update-alternatives
Requires(preun):update-alternatives
Requires:       dbus-common >= %{version}
Requires:       dbus-tools >= %{version}
Requires:       dbus-broker

%description
D-Bus is a message bus system, a simple way for applications to talk to one another.
This package contains the core D-Bus components and runtime libraries.

%package common
Summary:        D-BUS message bus configuration
BuildArch:      noarch
Requires:       %{name} = %{version}
Provides:       user(messagebus)
Provides:       group(messagebus)
%if %{with systemd}
%{?systemd_requires}
%endif
%description common
This package provides the core configuration and setup files for D-Bus.

%package tools
Summary:        Command-line tools for D-Bus
Provides:       dbus-daemon = %{version}
%description tools
This package contains command-line tools for interacting with and managing D-Bus,
including the original dbus-daemon.

%package devel
Summary:        Developer package for D-Bus
Requires:       %{name} = %{version}
Requires:       glibc-devel
%description devel
This package contains the header files and libraries needed for D-Bus development.

%if %{with systemd}
%build -p
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/dbus.conf
%endif

%install -a
mv -f %{buildroot}%{_bindir}/dbus-launch %{buildroot}%{_bindir}/dbus-launch.nox11
install -d %{buildroot}/run/dbus
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
(cd %{buildroot}%{_bindir} && ln -sf ../../etc/alternatives/dbus-launch dbus-launch)
find %{buildroot} -type f -name "*.la" -delete

%verifyscript
%{_sbindir}/update-alternatives --install %{_bindir}/dbus-launch dbus-launch %{_bindir}/dbus-launch.nox11 10

%preun
if [ "$1" = 0 ] ; then
  %{_sbindir}/update-alternatives --remove dbus-launch %{_bindir}/dbus-launch.nox11
fi

%if %{with systemd}
%pre common
%sysusers_create_package dbus %{SOURCE1}
%endif
%post common
if [ ! -L %{_localstatedir}/lib/dbus/machine-id ]; then
  mkdir -p %{_localstatedir}/lib/dbus/
  ln -s %{_sysconfdir}/machine-id %{_localstatedir}/lib/dbus/machine-id
fi
%tmpfiles_create %{_prefix}/lib/tmpfiles.d/dbus.conf

%files
%license COPYING
%doc AUTHORS NEWS README
%doc %{_docdir}/dbus
%attr(4750,root,messagebus) %verify(not mode) %{_libexecdir}/dbus-daemon-launch-helper
%ghost %{_sysconfdir}/alternatives/dbus-launch
%{_bindir}/dbus-launch.nox11
%{_bindir}/dbus-launch
%{_libdir}/libdbus-1.so.*

%files common
%dir %{_localstatedir}/lib/dbus
%ghost /run/dbus
%ghost %{_localstatedir}/lib/dbus/machine-id
%config(noreplace) %{_sysconfdir}/dbus-1/session.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.conf
%dir %{_sysconfdir}/dbus-1
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%dir %{_datadir}/dbus-1/system.d
%dir %{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/session.conf
%{_datadir}/dbus-1/system.conf
%{_datadir}/xml/dbus-1/*

%if %{with systemd}
%{_userunitdir}/dbus.service
%{_userunitdir}/dbus.socket
%dir %{_userunitdir}/sockets.target.wants
%{_userunitdir}/sockets.target.wants/dbus.socket
%{_tmpfilesdir}/dbus.conf
%{_sysusersdir}/dbus.conf
%{_unitdir}/dbus.service
%{_unitdir}/dbus.socket
%dir %{_unitdir}/multi-user.target.wants
%{_unitdir}/multi-user.target.wants/dbus.service
%dir %{_unitdir}/sockets.target.wants
%{_unitdir}/sockets.target.wants/dbus.socket
%endif

%files tools
%{_bindir}/dbus-cleanup-sockets
%{_bindir}/dbus-daemon
%{_bindir}/dbus-run-session
%{_bindir}/dbus-test-tool
%{_bindir}/dbus-monitor
%{_bindir}/dbus-send
%{_bindir}/dbus-update-activation-environment
%{_bindir}/dbus-uuidgen

%files devel
%{_includedir}/*
%{_libdir}/libdbus-1.so
%dir %{_libdir}/dbus-1.0
%{_libdir}/dbus-1.0/include
%{_libdir}/pkgconfig/dbus-1.pc
%{_libdir}/cmake/DBus1

%changelog
%{?autochangelog}
