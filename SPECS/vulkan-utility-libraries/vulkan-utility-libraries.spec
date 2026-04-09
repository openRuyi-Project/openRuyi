# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           vulkan-utility-libraries
Version:        1.4.335.0
Release:        %autorelease
Summary:        Vulkan utility libraries
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Utility-Libraries
#!RemoteAsset
Source0:        https://github.com/KhronosGroup/Vulkan-Utility-Libraries/archive/refs/tags/vulkan-sdk-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTS:BOOL=ON
BuildOption(conf):  -DVUL_WERROR:BOOL=OFF
BuildOption(conf):  -DUPDATE_DEPS:BOOL=OFF
BuildOption(conf):  -DCMAKE_CXX_FLAGS="%{optflags} -I%{_includedir}/magic_enum"

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  vulkan-headers
# for tests
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(magic_enum)

%description
Vulkan utility libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       vulkan-headers

%description    devel
Development files for %{name}. This package contains static libraries and headers.

%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/vulkan/
%dir %{_libdir}/cmake/VulkanUtilityLibraries/
%{_libdir}/cmake/VulkanUtilityLibraries/*.cmake
%{_libdir}/libVulkanLayerSettings.a
%{_libdir}/libVulkanSafeStruct.a

%changelog
%autochangelog
