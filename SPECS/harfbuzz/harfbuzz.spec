# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Change these to 1 once we have them
%bcond gtk_doc 0

Name:           harfbuzz
Version:        12.1.0
Release:        %autorelease
Summary:        Text shaping library
License:        MIT-Modern-Variant
URL:            https://github.com/harfbuzz/harfbuzz/
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/harfbuzz-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dgraphite2=enabled
BuildOption(conf):  -Dchafa=disabled
%if %{without gtk_doc}
BuildOption(conf):  -Ddocs=disabled
%endif

BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(graphite2)
%if %{with gtk_doc}
BuildRequires:  gtk-doc
%endif

%description
HarfBuzz is an implementation of the OpenType Layout engine.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license COPYING
%doc NEWS AUTHORS README.md
%{_libdir}/libharfbuzz.so.0*
%{_libdir}/libharfbuzz-gobject.so.0*
%{_libdir}/libharfbuzz-subset.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/HarfBuzz-0.0.typelib
%{_libdir}/libharfbuzz-icu.so.*
%{_libdir}/libharfbuzz-cairo.so.*

%files devel
%if %{with gtk_doc}
%doc %{_datadir}/gtk-doc
%endif
%{_bindir}/hb-info
%{_bindir}/hb-view
%{_bindir}/hb-shape
%{_bindir}/hb-subset
%{_includedir}/harfbuzz/
%{_libdir}/libharfbuzz.so
%{_libdir}/libharfbuzz-gobject.so
%{_libdir}/libharfbuzz-cairo.so
%{_libdir}/libharfbuzz-icu.so
%{_libdir}/libharfbuzz-subset.so
%{_libdir}/pkgconfig/harfbuzz.pc
%{_libdir}/pkgconfig/harfbuzz-cairo.pc
%{_libdir}/pkgconfig/harfbuzz-gobject.pc
%{_libdir}/pkgconfig/harfbuzz-icu.pc
%{_libdir}/pkgconfig/harfbuzz-subset.pc
%{_libdir}/cmake/harfbuzz/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/HarfBuzz-0.0.gir

%changelog
%autochangelog
