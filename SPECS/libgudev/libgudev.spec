# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond tests 0
%bcond doc 0

Name:           libgudev
Version:        238
Release:        %autorelease
Summary:        GObject-based wrapper library for libudev
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/libgudev
#!RemoteAsset
Source:         https://download.gnome.org/sources/libgudev/%{version}/libgudev-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dvapi=disabled

%if %{with doc}
BuildOption(conf):  -Dgtk_doc=true
%else
BuildOption(conf):  -Dgtk_doc=false
%endif

%if %{with tests}
BuildOption(conf):  -Dtests=enabled
%else
BuildOption(conf):  -Dtests=disabled
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  glib-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  libudev-devel
BuildRequires:  pkgconfig

%if %{with doc}
BuildRequires:  gtk-doc
%endif

%if %{with tests}
BuildRequires:  umockdev-devel
%endif

%description
This library makes it much simpler to use libudev from programs
already using GObject. It also supports GObject introspection.

%package        devel
Summary:        Header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package is necessary to build programs using %{name}.

%files
%license COPYING
%doc NEWS
%{_libdir}/libgudev-1.0.so.*
%{_libdir}/girepository-1.0/GUdev-1.0.typelib
%if %{with doc}
%doc %{_datadir}/gtk-doc/html/gudev
%endif

%files devel
%{_libdir}/libgudev-1.0.so
%{_includedir}/gudev-1.0/
%{_datadir}/gir-1.0/GUdev-1.0.gir
%{_libdir}/pkgconfig/gudev-1.0.pc

%changelog
%{?autochangelog}
