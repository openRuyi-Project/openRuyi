# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <zhengxingda@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mesa-demos
Version:        9.0.0
Release:        %autorelease
Summary:        A set of simple OpenGL (ES) and Vulkan demos
License:        MIT
URL:            https://gitlab.freedesktop.org/mesa/demos
#!RemoteAsset
Source:         https://archive.mesa3d.org/demos/mesa-demos-%{version}.tar.xz
BuildSystem:    meson

# Patch pointblast/spriteblast/dinoshade out for legal reasons
# (unclear license specification)
Patch0:         mesa-demos-8.5.0-legal.patch
# Install glsl demos data to the system data directory
Patch1:         mesa-demos-system-data.patch

BuildOption(conf):  -Dwith-system-data-files=true
# OSMesa is deprecated in favor of EGL_MESA_platform_surfaceless and not
# part of modern Mesa
BuildOption(conf):  -Dosmesa=disabled

BuildRequires:  pkgconfig(glesv1_cm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(glx)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  meson
# Needed for building shaders for Vulkan demos
BuildRequires:  glslang

%description
mesa-demos is a set of demos for various graphics APIs maintained by Mesa
developers to demonstrate Mesa.
These demos aren't bound to Mesa, and can be used with alternative providers
of these graphics APIs.

%files
%doc README.rst
%{_bindir}/*
%{_datadir}/mesa-demos/*

%changelog
%autochangelog
