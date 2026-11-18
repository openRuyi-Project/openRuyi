# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond gtk_doc 1

Name:           harfbuzz
Version:        15.1.0
Release:        %autorelease
Summary:        Text shaping library
License:        MIT-Modern-Variant
URL:            https://github.com/harfbuzz/harfbuzz/
#!RemoteAsset:  sha256:0fc7c565443a5f4be7da65ac5ee5bd737d9b158dc908708b7689a0a5796b0c8d
Source0:        %{url}/releases/download/%{version}/harfbuzz-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dgraphite2=enabled
BuildOption(conf):  -Dicu=enabled
BuildOption(conf):  -Dgpu_demo=enabled
BuildOption(conf):  -Dchafa=disabled
%if %{with gtk_doc}
BuildOption(conf):  -Ddocs=enabled
%else
BuildOption(conf):  -Ddocs=disabled
%endif

BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
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
%doc NEWS AUTHORS README.md
%license COPYING
%{_libdir}/libharfbuzz.so.0*
%{_libdir}/libharfbuzz-gobject.so.0*
%{_libdir}/libharfbuzz-raster.so.0*
%{_libdir}/libharfbuzz-vector.so.0*
%{_libdir}/libharfbuzz-gpu.so.0*
%{_libdir}/libharfbuzz-subset.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/HarfBuzz-0.0.typelib
%{_libdir}/libharfbuzz-icu.so.*
%{_libdir}/libharfbuzz-cairo.so.*

%files devel
%if %{with gtk_doc}
%doc %{_datadir}/gtk-doc
%endif
%{_bindir}/hb-raster
%{_bindir}/hb-vector
%{_bindir}/hb-gpu
%{_bindir}/hb-info
%{_bindir}/hb-view
%{_bindir}/hb-shape
%{_bindir}/hb-subset
%{_mandir}/man1/hb-*.1*
%{_includedir}/harfbuzz/
%{_libdir}/libharfbuzz.so
%{_libdir}/libharfbuzz-gobject.so
%{_libdir}/libharfbuzz-cairo.so
%{_libdir}/libharfbuzz-icu.so
%{_libdir}/libharfbuzz-raster.so
%{_libdir}/libharfbuzz-vector.so
%{_libdir}/libharfbuzz-gpu.so
%{_libdir}/libharfbuzz-subset.so
%{_libdir}/pkgconfig/harfbuzz.pc
%{_libdir}/pkgconfig/harfbuzz-cairo.pc
%{_libdir}/pkgconfig/harfbuzz-gobject.pc
%{_libdir}/pkgconfig/harfbuzz-icu.pc
%{_libdir}/pkgconfig/harfbuzz-raster.pc
%{_libdir}/pkgconfig/harfbuzz-vector.pc
%{_libdir}/pkgconfig/harfbuzz-gpu.pc
%{_libdir}/pkgconfig/harfbuzz-subset.pc
%{_libdir}/cmake/harfbuzz/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/HarfBuzz-0.0.gir

%changelog
%autochangelog
