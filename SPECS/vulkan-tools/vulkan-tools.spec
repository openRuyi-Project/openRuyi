# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond x11 1

Name:           vulkan-tools
Version:        1.4.335
Release:        %autorelease
Summary:        Vulkan tools
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Tools
#!RemoteAsset
Source0:        https://github.com/KhronosGroup/Vulkan-Tools/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_WSI_WAYLAND_SUPPORT=ON

%if %{with x11}
BuildOption(conf):  -DBUILD_WSI_XCB_SUPPORT=ON
BuildOption(conf):  -DBUILD_WSI_XLIB_SUPPORT=ON
%else
BuildOption(conf):  -DBUILD_WSI_XCB_SUPPORT=OFF
BuildOption(conf):  -DBUILD_WSI_XLIB_SUPPORT=OFF
%endif
BuildOption(conf):  -DBUILD_CUBE=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  cmake(VulkanLoader)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
%if %{with x11}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcb)
%endif

# Vulkan-Tools dlopen's libvulkan.so.1 from this package
Requires:       vulkan-loader
Provides:       vulkan-demos = %{version}-%{release}

%description
Vulkan tools, including vulkaninfo and vkcube.

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%{_bindir}/vulkaninfo
%{_bindir}/vkcube
%{_bindir}/vkcubepp

%changelog
%autochangelog
