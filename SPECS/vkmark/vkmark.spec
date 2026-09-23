# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           vkmark
Version:        2025.01
Release:        %autorelease
Summary:        Vulkan benchmark with configurable scenes
License:        LGPL-2.1-or-later AND MIT
URL:            https://github.com/vkmark/vkmark
#!RemoteAsset:  git+https://github.com/vkmark/vkmark.git#%{version}
#!CreateArchive
Source0:        %{name}-%{version}.tar.gz
BuildSystem:    meson

# Backport a upstream fix for display winsys crash on lavapipe
Patch0001:      0001-UPSTREAM-display-Properly-handle-Vulkan-errors-during-probing.patch

BuildOption(conf):  -Dxcb=true
BuildOption(conf):  -Dwayland=true
BuildOption(conf):  -Dkms=true

BuildRequires:  glm-devel
BuildRequires:  glslang
BuildRequires:  meson
BuildRequires:  pkgconfig(assimp)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  python3
BuildRequires:  vulkan-headers >= 1.4.357.0

%description
vkmark is an extensible Vulkan benchmarking suite with targeted, configurable
scenes. It supports X11, Wayland, KMS, direct display and headless operation.

%prep -a
# Rebuild all SPIR-V shaders from their auditable GLSL sources.
rm data/shaders/*.spv
for shader in data/shaders/*.vert data/shaders/*.frag; do
    glslangValidator -V "$shader" -o "$shader.spv"
done

%files
%doc NEWS README.md
%license COPYING-LGPL2.1
%{_bindir}/vkmark
%{_datadir}/vkmark/
%{_libdir}/vkmark/
%{_mandir}/man1/vkmark.1*

%changelog
%autochangelog
