# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <zhengxingda@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           glmark2
Version:        2023.01
Release:        %autorelease
Summary:        A OpenGL (ES) 2.0 benchmark
License:        MIT AND BSD-3-Clause AND GPL-3.0-or-later
URL:            https://github.com/glmark2/glmark2
#!RemoteAsset
Source:         https://github.com/glmark2/glmark2/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

# Fixes visual config match for drivers bind depth with stencil (e.g. IMG proprietary GLES)
Patch1:         glmark2-2023.01-backport-visual-config-match.patch

BuildOption(conf):  -Dflavors=drm-gl,drm-glesv2,wayland-gl,wayland-glesv2,x11-gl,x11-glesv2,x11-gl-egl

BuildRequires:  meson
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

# glmark2 uses a dynamic loader (glad) for GL libraries
Requires:       libglvnd

%description
glmark2 is a benchmark suite for OpenGL / OpenGL ES 2.x. Please note that some
benchmark items in it do not reflect real work usage and the score isn't
properly weighted.

%files
%doc README NEWS
%license COPYING COPYING.SGI
%{_datadir}/glmark2/textures/*
%{_datadir}/glmark2/models/*
%{_datadir}/glmark2/shaders/*
%{_bindir}/glmark2*
%{_mandir}/man1/glmark*.1*

%changelog
%autochangelog
