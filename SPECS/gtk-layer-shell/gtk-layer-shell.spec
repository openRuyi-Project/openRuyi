# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gtk-layer-shell
Version:        0.10.1
Release:        %autorelease
Summary:        Library to create components for Wayland using the Layer Shell
License:        LGPL-3.0-or-later AND MIT
URL:            https://github.com/wmww/gtk-layer-shell
#!RemoteAsset:  sha256:88c3a3e0a5300532f3d368d5df64838a87f1fb85273f22d41df0a6b8d0ec59c6
Source0:        https://github.com/wmww/gtk-layer-shell/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dtests=false

BuildRequires:  meson >= 0.54
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0) >= 3.22.0
BuildRequires:  pkgconfig(wayland-client) >= 1.10.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.16
BuildRequires:  pkgconfig(wayland-scanner) >= 1.10.0
BuildRequires:  pkgconfig(wayland-server) >= 1.10.0

%description
A library to write GTK applications that use Layer Shell. Layer Shell is a
Wayland protocol for desktop shell components, such as panels, notifications
and wallpapers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%check
# skip tests as the tests need in real system.

%files
%license LICENSE_LGPL.txt LICENSE_MIT.txt
%doc README.md CHANGELOG.md
%{_libdir}/girepository-1.0/GtkLayerShell-*.typelib
%{_libdir}/libgtk-layer-shell.so.*

%files devel
%{_datadir}/gir-1.0/GtkLayerShell-*.gir
%{_datadir}/vala/vapi/gtk-layer-shell-*.deps
%{_datadir}/vala/vapi/gtk-layer-shell-*.vapi
%{_includedir}/gtk-layer-shell/
%{_libdir}/libgtk-layer-shell.so
%{_libdir}/pkgconfig/gtk-layer-shell-0.pc

%changelog
%autochangelog
