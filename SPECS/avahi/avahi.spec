# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           avahi
Version:        0.8
Release:        %autorelease
Summary:        Local network service discovery
License:        LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:            https://github.com/avahi/avahi
#!RemoteAsset:  sha256:060309d7a333d38d951bc27598c677af1796934dbd98e1024e7ad8de798fedda
Source0:        https://github.com/avahi/avahi/releases/download/v%{version}/avahi-%{version}.tar.gz
Source1:        avahi.sysusers
Source2:        avahi-autoipd.sysusers
BuildSystem:    autotools

# https://github.com/avahi/avahi/pull/265
# or nothing provides pkgconfig(libevent-2.1.5) needed by avahi-devel
Patch0:         0001-fix-pc-file.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --with-distro=none
BuildOption(conf):  --with-avahi-user=avahi
BuildOption(conf):  --with-avahi-group=avahi
BuildOption(conf):  --with-avahi-priv-access-group=avahi
BuildOption(conf):  --with-autoipd-user=avahi-autoipd
BuildOption(conf):  --with-autoipd-group=avahi-autoipd
BuildOption(conf):  --with-systemdsystemunitdir=%{_unitdir}
BuildOption(conf):  --disable-python
BuildOption(conf):  --disable-mono
BuildOption(conf):  --disable-monodoc
BuildOption(conf):  --disable-qt3
BuildOption(conf):  --disable-qt4
BuildOption(conf):  --disable-qt5
BuildOption(conf):  --enable-gtk3
BuildOption(conf):  --disable-compat-libdns_sd
BuildOption(conf):  --disable-compat-howl

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1) >= 0.90
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdaemon) >= 0.11
BuildRequires:  pkgconfig(libevent) >= 2.0.21
BuildRequires:  pkgconfig(expat)
BuildRequires:  gdbm-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  xmltoman

%description
Avahi is a system which facilitates service discovery on a local network.

%package        devel
Summary:        Libraries and header files for avahi development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The avahi-devel package contains the header files and libraries necessary for
developing programs using avahi.

%package        autoipd
Summary:        Link-local IPv4 address automatic configuration daemon (IPv4LL)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    autoipd
avahi-autoipd implements IPv4LL, "Dynamic Configuration of IPv4 Link-Local Addresses".

%prep -a
rm -fv docs/INSTALL

%conf -p
NOCONFIGURE=1 ./autogen.sh

%install -a
# remove example
rm -fv %{buildroot}%{_sysconfdir}/avahi/services/ssh.service
rm -fv %{buildroot}%{_sysconfdir}/avahi/services/sftp-ssh.service

mkdir -p %{buildroot}%{_localstatedir}/run/avahi-daemon
mkdir -p %{buildroot}%{_localstatedir}/lib/avahi-autoipd
mkdir -p %{buildroot}%{_sysconfdir}/avahi/etc
touch %{buildroot}%{_sysconfdir}/avahi/etc/localtime

install -m0644 -D %{SOURCE1} %{buildroot}%{_sysusersdir}/avahi.conf
install -m0644 -D %{SOURCE2} %{buildroot}%{_sysusersdir}/avahi-autoipd.conf

rm -fv %{buildroot}%{_sysconfdir}/rc.d/init.d/avahi-daemon
rm -fv %{buildroot}%{_sysconfdir}/rc.d/init.d/avahi-dnsconfd

# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%pre
%sysusers_create_package %{name} %{SOURCE1}
%sysusers_create_package %{name}-autoipd %{SOURCE2}

%post
%systemd_post avahi-daemon.socket avahi-daemon.service avahi-dnsconfd.service

%preun
%systemd_preun avahi-daemon.socket avahi-daemon.service avahi-dnsconfd.service

%postun
%systemd_postun_with_restart avahi-daemon.socket avahi-daemon.service avahi-dnsconfd.service

%files -f %{name}.lang
%license LICENSE
%doc docs/* avahi-daemon/example.service
%dir %{_sysconfdir}/avahi
%dir %{_sysconfdir}/avahi/etc
%ghost %{_sysconfdir}/avahi/etc/localtime
%config(noreplace) %{_sysconfdir}/avahi/hosts
%dir %{_sysconfdir}/avahi/services
%ghost %attr(0755, avahi, avahi) %dir %{_localstatedir}/run/avahi-daemon
%config(noreplace) %{_sysconfdir}/avahi/avahi-daemon.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/avahi-dbus.conf
%{_sbindir}/avahi-daemon
%dir %{_datadir}/avahi
%{_datadir}/avahi/*.dtd
%dir %{_libdir}/avahi
%{_mandir}/man5/*
%{_mandir}/man8/avahi-daemon.*
%{_unitdir}/avahi-daemon.service
%{_unitdir}/avahi-daemon.socket
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.Avahi.service
%{_libdir}/libavahi-core.so.*
%{_sysusersdir}/avahi.conf
%{_bindir}/avahi-browse*
%{_bindir}/avahi-publish*
%{_bindir}/avahi-resolve*
%{_bindir}/avahi-set-host-name
%{_mandir}/man1/avahi-browse*.1*
%{_mandir}/man1/avahi-publish*.1*
%{_mandir}/man1/avahi-resolve*.1*
%{_mandir}/man1/avahi-set-host-name.1*
%{_bindir}/bshell
%{_bindir}/bssh
%{_bindir}/bvnc
%{_bindir}/avahi-discover-standalone
%{_datadir}/applications/b*.desktop
%{_datadir}/avahi/interfaces/
%{_libdir}/libavahi-common.so.*
%{_libdir}/libavahi-client.so.*
%{_libdir}/libavahi-libevent.so.*
%{_libdir}/libavahi-glib.so.*
%{_libdir}/libavahi-gobject.so.*
%{_libdir}/libavahi-ui-gtk3.so.*
%config(noreplace) %{_sysconfdir}/avahi/avahi-dnsconfd.action
%{_sbindir}/avahi-dnsconfd
%{_mandir}/man8/avahi-dnsconfd.*
%{_unitdir}/avahi-dnsconfd.service

%files devel
%{_libdir}/libavahi-common.so
%{_libdir}/libavahi-core.so
%{_libdir}/libavahi-client.so
%{_libdir}/libavahi-libevent.so
%{_includedir}/avahi-client
%{_includedir}/avahi-common
%{_includedir}/avahi-core
%{_includedir}/avahi-libevent
%{_libdir}/pkgconfig/avahi-core.pc
%{_libdir}/pkgconfig/avahi-client.pc
%{_libdir}/pkgconfig/avahi-libevent.pc
%{_libdir}/libavahi-glib.so
%{_includedir}/avahi-glib
%{_libdir}/pkgconfig/avahi-glib.pc
%{_libdir}/libavahi-gobject.so
%{_includedir}/avahi-gobject
%{_libdir}/pkgconfig/avahi-gobject.pc
%{_libdir}/libavahi-ui-gtk3.so
%{_includedir}/avahi-ui
%{_libdir}/pkgconfig/avahi-ui-gtk3.pc

%files autoipd
%{_sbindir}/avahi-autoipd
%config(noreplace) %{_sysconfdir}/avahi/avahi-autoipd.action
%attr(1770,avahi-autoipd,avahi-autoipd) %dir %{_localstatedir}/lib/avahi-autoipd/
%{_mandir}/man8/avahi-autoipd.*
%{_sysusersdir}/avahi-autoipd.conf

%changelog
%autochangelog
