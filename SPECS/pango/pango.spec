# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pango
Version:        1.57.0
Release:        %autorelease
Summary:        System for layout and rendering of internationalized text
License:        LGPL-2.0-or-later
URL:            https://www.pango.org/
VCS:            git:https://gitlab.gnome.org/GNOME/pango
#!RemoteAsset:  sha256:890640c841dae77d3ae3d8fe8953784b930fa241b17423e6120c7bfdf8b891e7
Source0:        https://download.gnome.org/sources/pango/1.57/pango-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libthai)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xrender)

%description
Pango is a library for laying out and rendering of text, with an emphasis
on internationalization. Pango can be used anywhere that text layout is needed,
though most of the work on Pango so far has been done in the context of the
GTK+ widget toolkit. Pango forms the core of text and font handling for GTK+.

Pango is designed to be modular; the core Pango layout engine can be used
with different font backends.

The integration of Pango with Cairo provides a complete solution with high
quality text handling and graphics rendering.

%package        devel
Summary:        Development files for pango
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The pango-devel package includes the header files for the pango package.

# TODO: Broken check also no distro is checking it - 251
%check

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libpango*-*.so.*
%{_bindir}/pango-list
%{_bindir}/pango-segmentation
%{_bindir}/pango-view
%{_libdir}/girepository-1.0/Pango-1.0.typelib
%{_libdir}/girepository-1.0/PangoCairo-1.0.typelib
%{_libdir}/girepository-1.0/PangoFc-1.0.typelib
%{_libdir}/girepository-1.0/PangoFT2-1.0.typelib
%{_libdir}/girepository-1.0/PangoOT-1.0.typelib
%{_libdir}/girepository-1.0/PangoXft-1.0.typelib

%files devel
%{_libdir}/libpango*.so
%{_includedir}/*
%{_libdir}/pkgconfig/pango.pc
%{_libdir}/pkgconfig/pangocairo.pc
%{_libdir}/pkgconfig/pangofc.pc
%{_libdir}/pkgconfig/pangoft2.pc
%{_libdir}/pkgconfig/pangoot.pc
%{_libdir}/pkgconfig/pangoxft.pc
%{_datadir}/gir-1.0/Pango-1.0.gir
%{_datadir}/gir-1.0/PangoCairo-1.0.gir
%{_datadir}/gir-1.0/PangoFc-1.0.gir
%{_datadir}/gir-1.0/PangoFT2-1.0.gir
%{_datadir}/gir-1.0/PangoOT-1.0.gir
%{_datadir}/gir-1.0/PangoXft-1.0.gir

%changelog
%autochangelog
