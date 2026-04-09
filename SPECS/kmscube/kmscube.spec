# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# No release or tag,so we use the latest commit.
%global commit f60e50e887d3c49e91ac9b06d8199b36152632fa
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           kmscube
Version:        0+git20260202.%{shortcommit}
Release:        %autorelease
Summary:        Example KMS/GBM/EGL application
License:        MIT
URL:            https://gitlab.freedesktop.org/mesa/kmscube
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/mesa/kmscube/-/archive/%{commit}/kmscube-%{commit}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dgstreamer=disabled

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gbm)

%description
kmscube is a demonstration program for how to drive bare metal graphics
without a compositor like X11 or Wayland. It uses DRM/KMS, GBM and EGL
for rendering content using OpenGL ES.

%files
%license COPYING
%{_bindir}/kmscube
%{_bindir}/texturator

%changelog
%autochangelog
