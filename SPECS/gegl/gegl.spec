# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gegl
Version:        0.4.68
Release:        %autorelease
Summary:        Graph based image processing framework
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.gegl.org
VCS:            git:https://gitlab.gnome.org/GNOME/gegl.git
#!RemoteAsset:  sha256:5002309b9a701260658e8b3a61540fd5673887cef998338e1992524a33b23ae3
Source0:        https://download.gimp.org/gegl/0.4/gegl-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  --auto-features=auto

BuildRequires:  meson
BuildRequires:  pkgconfig(babl-0.1) >= 0.1.116
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.0.0
BuildRequires:  pkgconfig(libjpeg) >= 1.0.0
BuildRequires:  pkgconfig(libpng) >= 1.6.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.32.0
BuildRequires:  pkgconfig(gexiv2) < 0.15.0
BuildRequires:  pkgconfig(vapigen) >= 0.20.0
BuildRequires:  pkgconfig(luajit) >= 2.0.4
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)

%description
GEGL (Generic Graphics Library) is a graph based image processing framework.
GEGLs original design was made to scratch GIMP's itches for a new
compositing and processing core. This core is being designed to have
minimal dependencies and a simple well defined API.

%package        devel
Summary:        Development files for gegl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The gegl-devel package contains libraries and header files for
developing applications that use GEGL.

%package        tools
Summary:        Command line tools for gegl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The gegl-tools package contains tools for the command line that use the
GEGL library.

%install -a
%find_lang %{name}-0.4 --generate-subpackages

%files -f %{name}-0.4.lang
%license COPYING
%{_libdir}/libgegl-0.4.so.*
%{_libdir}/gegl-0.4/
%{_libdir}/girepository-1.0/Gegl-0.4.typelib
%{_libdir}/libgegl-npd-0.4.so
%{_libdir}/libgegl-sc-0.4.so
%dir %{_datadir}/gegl-0.4/
%{_datadir}/gegl-0.4/lua/

%files devel
%{_includedir}/gegl-0.4/
%{_libdir}/libgegl-0.4.so
%{_libdir}/pkgconfig/gegl-0.4.pc
%{_libdir}/pkgconfig/gegl-sc-0.4.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gegl-0.4.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gegl-0.4.deps
%{_datadir}/vala/vapi/gegl-0.4.vapi

%files tools
%{_bindir}/gegl
%{_bindir}/gegl-imgcmp

%changelog
%autochangelog
