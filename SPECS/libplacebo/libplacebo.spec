# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libplacebo
Version:        7.360.1
License:        LGPL-2.0-or-later
Release:        %autorelease
Summary:        Reusable library for GPU-accelerated video/image rendering primitives
URL:            https://github.com/haasn/libplacebo
#!RemoteAsset:  sha256:d05fdf90bea2f629eaa2d115e909fd356388ac639e54f77b87a018a6d76224bd
Source0:        https://github.com/haasn/libplacebo/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dd3d11=disabled
BuildOption(conf):  -Ddemos=false
BuildOption(conf):  -Dshaderc=enabled
BuildOption(conf):  -Dglslang=disabled
BuildOption(conf):  -Dlibdovi=disabled

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  python3dist(glad2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(mako)
BuildRequires:  python3dist(markupsafe)
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  vulkan-devel
BuildRequires:  glslang
BuildRequires:  pkgconfig(libxxhash)

%description
libplacebo is essentially the core rendering algorithms and ideas of
mpv turned into a library. This grew out of an interest to accomplish
the following goals:

- Clean up mpv's internal API and make it reusable for other projects.
- Provide a standard library of useful GPU-accelerated image processing
  primitives based on GLSL, so projects like VLC or Firefox can use them
  without incurring a heavy dependency on `libmpv`.
- Rewrite core parts of mpv's GPU-accelerated video renderer on top of
  redesigned abstractions. (Basically, I wanted to eliminate code smell
  like `shader_cache.c` and totally redesign `gpu/video.c`)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license LICENSE
%doc README.md
%{_libdir}/libplacebo.so.360

%files devel
%{_includedir}/libplacebo
%{_libdir}/libplacebo.so
%{_libdir}/pkgconfig/libplacebo.pc

%changelog
%autochangelog
