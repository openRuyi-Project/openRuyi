# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           keybinder
Version:        0.3.2
Release:        %autorelease
Summary:        A library for registering global keyboard shortcuts
License:        MIT
URL:            https://github.com/kupferlauncher/keybinder
#!RemoteAsset
Source0:        %{url}/releases/download/keybinder-3.0-v%{version}/keybinder-3.0-%{version}.tar.gz
# https://github.com/kupferlauncher/keybinder/pull/18
Patch0:         fix-empty-gobject.patch
BuildSystem:    autotools

BuildOption(conf):  --enable-gtk-doc

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc

%description
Keybinder is a library for registering global keyboard shortcuts.
Keybinder works with GTK-based applications using the X Window System.

The library contains:
- A C library, libkeybinder
- Gobject-Introspection bindings

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the development files for %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}.

%files
%license COPYING
%doc NEWS AUTHORS README
%{_libdir}/libkeybinder-3.0.so.*
%{_libdir}/girepository-1.0/Keybinder-3.0.typelib

%files devel
%dir %{_includedir}/keybinder-3.0/
%{_includedir}/keybinder-3.0/keybinder.h
%{_libdir}/pkgconfig/keybinder-3.0.pc
%{_libdir}/libkeybinder-3.0.so
%{_datadir}/gir-1.0/Keybinder-3.0.gir

%files doc
%dir %{_datadir}/gtk-doc/html/keybinder-3.0/
%{_datadir}/gtk-doc/html/keybinder-3.0/*

%changelog
%autochangelog
