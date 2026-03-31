# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
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
VCS:            git:https://gitlab.freedesktop.org/dbus/dbus.git
#!RemoteAsset
Source0:        https://dbus.freedesktop.org/releases/dbus/dbus-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dasserts=false

%if %{with systemd}
BuildOption(conf):  -Dsystemd=enabled
BuildOption(conf):  -Dsystemd_system_unitdir=%{_unitdir}
BuildOption(conf):  -Dsystemd_user_unitdir=%{_userunitdir}
%else
BuildOption(conf):  -Dsystemd=disabled
%endif
%if %{with selinux}
BuildOption(conf):  -Dselinux=enabled
%else
BuildOption(conf):  -Dselinux=disabled
%endif
BuildOption(conf):  -Dx11_autolaunch=disabled
BuildOption(conf):  -Dxml_docs=disabled
BuildOption(conf):  -Ddoxygen_docs=disabled
BuildOption(conf):  -Dducktype_docs=disabled
BuildOption(conf):  -Dqt_help=disabled
BuildOption(conf):  -Dlibaudit=enabled
BuildOption(conf):  -Dapparmor=disabled
BuildOption(conf):  -Dkqueue=disabled
BuildOption(conf):  -Dlaunchd=disabled
BuildOption(conf):  -Dmodular_tests=disabled

BuildRequires:  meson
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig
BuildRequires:  xmlto
%if %{with systemd}
BuildRequires:  pkgconfig(libsystemd) >= 209
%endif
%if %{with selinux}
BuildRequires:  pkgconfig(libselinux)
%endif

Requires(post): update-alternatives
Requires(preun):update-alternatives
Requires(pre):  dbus-common
Requires(pre):  user(messagebus)
Requires:       dbus-common
Requires:       user(messagebus)
Requires:       dbus-tools
Requires:       dbus-broker

%description
D-Bus is a message bus system, a simple way for applications to talk to one another.
This package contains the core D-Bus components and runtime libraries.

%package        common
Summary:        D-BUS message bus configuration
BuildArch:      noarch
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with systemd}
%{?systemd_requires}
%endif

%description    common
This package provides the core configuration and setup files for D-Bus.

%package        tools
Summary:        Command-line tools for D-Bus
Provides:       dbus-daemon = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
This package contains command-line tools for interacting with and managing D-Bus,
including the original dbus-daemon.

%package        devel
Summary:        Developer package for D-Bus
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glibc-devel

%description    devel
This package contains the header files and libraries needed for D-Bus development.

%install -a
mv -f %{buildroot}%{_bindir}/dbus-launch %{buildroot}%{_bindir}/dbus-launch.nox11
install -d %{buildroot}/run/dbus
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
%if %{with systemd}
# openRuyi keeps messagebus in setup, so drop the upstream sysusers
# provider file instead of shipping a second source of truth here.
rm -f %{buildroot}%{_sysusersdir}/dbus.conf
%endif

%post
if [ "$1" = 1 ]; then
%{_sbindir}/update-alternatives --install %{_bindir}/dbus-launch dbus-launch %{_bindir}/dbus-launch.nox11 10
fi

%preun
if [ "$1" = 0 ] ; then
  %{_sbindir}/update-alternatives --remove dbus-launch %{_bindir}/dbus-launch.nox11
fi

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
%ghost %{_bindir}/dbus-launch
%{_bindir}/dbus-launch.nox11
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
