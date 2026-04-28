# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           upower
Version:        1.91.1
Release:        %autorelease
Summary:        Power Management Service
License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/upower/upower
#!RemoteAsset:  sha256:d568638d670a63a1886335b7b136f4888cb38a3b28f3f4bcdeaffcca0b0f6df8
Source0:        https://gitlab.freedesktop.org/upower/upower/-/archive/v%{version}/upower-v%{version}.tar.bz2
BuildSystem:    meson

BuildOption(conf):  -Dman=true
BuildOption(conf):  -Dintrospection=enabled
BuildOption(conf):  -Didevice=disabled
BuildOption(conf):  -Dgtk-doc=true

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(glib-2.0) >= 2.6.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  polkit-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  gtk-doc

%description
UPower (formerly DeviceKit-power) provides a daemon, API and command
line tools for managing power devices attached to the system.

%package        devel
Summary:        Headers and libraries for UPower
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and libraries for UPower.

%install -a
mkdir -p %{buildroot}%{_libexecdir}/installed-tests
mv %{buildroot}%{_libexecdir}/upower %{buildroot}%{_libexecdir}/installed-tests/

%find_lang %{name} --generate-subpackages

%post
%systemd_post upower.service

%preun
%systemd_preun upower.service

%postun
%systemd_postun_with_restart upower.service

%check
# skip tests as it needs dus.

%files -f %{name}.lang
%license COPYING
%doc NEWS AUTHORS HACKING.md README.md
%dir %{_sysconfdir}/UPower
%config %{_sysconfdir}/UPower/UPower.conf
%{_sysconfdir}/UPower/UPower.conf.d/README.md
%{_bindir}/upower
%{_libexecdir}/upowerd
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/polkit-1/actions/org.freedesktop.upower.policy
%{_datadir}/zsh/
%{_udevrulesdir}/*.rules
%{_udevhwdbdir}/*.hwdb
%{_unitdir}/*.service
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_mandir}/man8/*
%ghost %dir %{_localstatedir}/lib/upower
%{_libdir}/libupower-glib.so.3*
%{_libdir}/girepository-1.0/*.typelib
%dir %{_datadir}/installed-tests/
%dir %{_datadir}/installed-tests/upower/
%{_datadir}/installed-tests/upower/upower-integration.test
%{_libexecdir}/installed-tests/upower/

%files devel
%dir %{_includedir}/libupower-glib
%{_includedir}/libupower-glib/up-*.h
%{_includedir}/libupower-glib/upower.h
%{_libdir}/libupower-glib.so
%{_libdir}/pkgconfig/upower-glib.pc
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html/UPower
%{_datadir}/gtk-doc/html/UPower/*

%changelog
%autochangelog
