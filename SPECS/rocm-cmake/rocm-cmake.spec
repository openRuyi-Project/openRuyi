# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# there is no debug package - this is just cmake modules
%global debug_package %{nil}

%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:           rocm-cmake
Version:        %{rocm_version}
Release:        %autorelease
Summary:        CMake modules for common build and development tasks for ROCm
License:        MIT
URL:            https://github.com/ROCm/rocm-cmake
#!RemoteAsset
Source:         %{url}/archive/rocm-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    cmake

# https://github.com/ROCm/rocm-cmake/issues/276
Patch0:         0001-rocm-cmake-follow-cmake-install-rules.patch

BuildRequires:  cmake

Requires:       cmake

%description
rocm-cmake is a collection of CMake modules for common build and development
tasks within the ROCm project. It is therefore a build dependency for many of
the libraries that comprise the ROCm platform.

rocm-cmake is not required for building libraries or programs that use ROCm; it
is required for building some of the libraries that are a part of ROCm.

%prep -a

# Fix hardcoding of libdir
sed -i -e "s@set(CMAKE_INSTALL_LIBDIR \"lib\"@set(CMAKE_INSTALL_LIBDIR \"%{_lib}\"@" share/rocmcmakebuildtools/cmake/ROCMCreatePackage.cmake
sed -i -e "s@set(CMAKE_INSTALL_LIBDIR \"lib\"@set(CMAKE_INSTALL_LIBDIR \"%{_lib}\"@" share/rocmcmakebuildtools/cmake/ROCMInstallTargets.cmake

# Skip ctest because rocm-cmake use private lib path to test
%check
:

%install -a

rm -f %{buildroot}%{_prefix}/share/doc/rocm-cmake/LICENSE

%files
%doc CHANGELOG.md
%license LICENSE
%dir %{_datadir}/rocm
%dir %{_datadir}/rocmcmakebuildtools
%{_datadir}/rocm/*
%{_datadir}/rocmcmakebuildtools/*

%changelog
%autochangelog
