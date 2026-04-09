# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond x11 0

Name:           vulkan-loader
Version:        1.4.335.0
Release:        %autorelease
Summary:        Vulkan ICD desktop loader
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Loader
#!RemoteAsset
Source0:        https://github.com/KhronosGroup/Vulkan-Loader/archive/refs/tags/vulkan-sdk-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_WSI_WAYLAND_SUPPORT=ON

%if %{with x11}
BuildOption(conf):  -DBUILD_WSI_XCB_SUPPORT=ON
BuildOption(conf):  -DBUILD_WSI_XLIB_SUPPORT=ON
%else
BuildOption(conf):  -DBUILD_WSI_XCB_SUPPORT=OFF
BuildOption(conf):  -DBUILD_WSI_XLIB_SUPPORT=OFF
%endif

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  vulkan-headers = %{version}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)

%if %{with x11}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
%endif

Provides:       vulkan = %{version}-%{release}
Provides:       vulkan-filesystem = %{version}-%{release}

%description
This project provides the Khronos official Vulkan ICD desktop
loader for Windows, Linux, and MacOS.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       vulkan-headers
Provides:       vulkan-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/vulkan/{explicit,implicit}_layer.d/ \
%{buildroot}%{_datadir}/vulkan/{explicit,implicit}_layer.d/ \
%{buildroot}{%{_sysconfdir},%{_datadir}}/vulkan/icd.d

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%dir %{_sysconfdir}/vulkan/
%dir %{_sysconfdir}/vulkan/explicit_layer.d/
%dir %{_sysconfdir}/vulkan/icd.d/
%dir %{_sysconfdir}/vulkan/implicit_layer.d/
%dir %{_datadir}/vulkan/
%dir %{_datadir}/vulkan/explicit_layer.d/
%dir %{_datadir}/vulkan/icd.d/
%dir %{_datadir}/vulkan/implicit_layer.d/
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/vulkan.pc
%{_libdir}/*.so
%dir %{_libdir}/cmake/VulkanLoader/
%{_libdir}/cmake/VulkanLoader/*.cmake

%changelog
%autochangelog
