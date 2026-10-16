# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Change these to 1 once we have them
%bcond gtk_doc 0

Name:           harfbuzz
Version:        14.0.0
Release:        %autorelease
Summary:        Text shaping library
License:        MIT-Modern-Variant
URL:            https://github.com/harfbuzz/harfbuzz/
#!RemoteAsset:  sha256:d4aa312728136e3dc7c3cda47b871614ce0d12bbb19f9dcac2ea70de836dc307
Source0:        %{url}/releases/download/%{version}/harfbuzz-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dgraphite2=enabled
BuildOption(conf):  -Dchafa=disabled
BuildOption(conf):  -Dgpu_demo=disabled
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
%{_libdir}/libharfbuzz-raster.so.0*
%{_libdir}/libharfbuzz-vector.so.0*
%{_libdir}/libharfbuzz-gpu.so.0*
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
%{_bindir}/hb-raster
%{_bindir}/hb-vector
%{_includedir}/harfbuzz/
%{_libdir}/libharfbuzz.so
%{_libdir}/libharfbuzz-gobject.so
%{_libdir}/libharfbuzz-cairo.so
%{_libdir}/libharfbuzz-icu.so
%{_libdir}/libharfbuzz-subset.so
%{_libdir}/libharfbuzz-raster.so
%{_libdir}/libharfbuzz-vector.so
%{_libdir}/libharfbuzz-gpu.so
%{_libdir}/pkgconfig/harfbuzz.pc
%{_libdir}/pkgconfig/harfbuzz-cairo.pc
%{_libdir}/pkgconfig/harfbuzz-gobject.pc
%{_libdir}/pkgconfig/harfbuzz-icu.pc
%{_libdir}/pkgconfig/harfbuzz-subset.pc
%{_libdir}/pkgconfig/harfbuzz-raster.pc
%{_libdir}/pkgconfig/harfbuzz-vector.pc
%{_libdir}/pkgconfig/harfbuzz-gpu.pc
%{_libdir}/cmake/harfbuzz/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/HarfBuzz-0.0.gir

%changelog
%autochangelog
