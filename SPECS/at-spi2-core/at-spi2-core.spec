# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

Name:           at-spi2-core
Version:        2.58.2
Release:        %autorelease
Summary:        Protocol definitions and daemon for D-Bus at-spi
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/at-spi2-core
#!RemoteAsset
Source0:        https://download.gnome.org/sources/at-spi2-core/2.58/at-spi2-core-%{version}.tar.xz
BuildSystem:    meson

%if %{with doc}
BuildOption(conf):  -Ddocs=true
%else
BuildOption(conf):  -Ddocs=false
%endif

BuildOption(conf):  -Ddefault_bus=dbus-daemon
BuildOption(conf):  -Ddbus_daemon=/usr/bin/dbus-daemon

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libsystemd)
%if %{with doc}
BuildRequires:  sphinx-build
BuildRequires:  pkgconfig(gi-docgen)
%endif

Requires:       dbus

%description
at-spi allows assistive technologies to access GTK-based applications.
This version replaces the old CORBA-based at-spi with D-Bus.

%package        devel
Summary:        Development files and headers for at-spi2-core
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The at-spi2-core-devel package includes the header files and
API documentation for libatspi.

%install -a
# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%check
# skip the tests,need dbus

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%{_libexecdir}/at-spi2-registryd
%{_libexecdir}/at-spi-bus-launcher
%{_libdir}/libatspi.so.*
%{_libdir}/girepository-1.0/Atspi-2.0.typelib
%dir %{_datadir}/defaults/at-spi2
%{_sysconfdir}/xdg/Xwayland-session.d/00-at-spi
%{_datadir}/defaults/at-spi2/accessibility.conf
%{_sysconfdir}/xdg/autostart/at-spi-dbus-bus.desktop
%{_datadir}/dbus-1/accessibility-services/*.service
%{_datadir}/dbus-1/services/*.service
%{_userunitdir}/at-spi-dbus-bus.service
%{python3_sitearch}/gi/overrides/Atspi.py
%{python3_sitearch}/gi/overrides/__pycache__/Atspi.*
%{_libdir}/libatk-1.0.so.*
%{_libdir}/girepository-1.0/Atk-1.0.typelib
%{_libdir}/libatk-bridge-2.0.so.*
%dir %{_libdir}/gtk-2.0/modules
%{_libdir}/gtk-2.0/modules/libatk-bridge.so
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop

%files devel
%{_libdir}/libatspi.so
%{_includedir}/at-spi-2.0/
%{_libdir}/pkgconfig/atspi-2.pc
%{_datadir}/gir-1.0/Atspi-2.0.gir
%if %{with doc}
%{_docdir}/libatspi
%endif
%{_libdir}/libatk-1.0.so
%{_includedir}/atk-1.0/
%{_libdir}/pkgconfig/atk.pc
%{_datadir}/gir-1.0/Atk-1.0.gir
%if %{with doc}
%{_docdir}/atk
%endif
%{_includedir}/at-spi2-atk/2.0/atk-bridge.h
%{_libdir}/libatk-bridge-2.0.so
%{_libdir}/pkgconfig/atk-bridge-2.0.pc

%changelog
%autochangelog
