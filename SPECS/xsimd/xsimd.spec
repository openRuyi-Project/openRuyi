# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xsimd
Version:        14.2.0
Release:        %autorelease
Summary:        C++ wrappers for SIMD intrinsics and parallelized, optimized math implementations
License:        BSD-3-Clause
URL:            https://github.com/xtensor-stack/xsimd
#!RemoteAsset:  sha256:21e841ab684b05331e81e7f782431753a029ef7b7d9d6d3ddab837e7782a40ee
Source0:        https://github.com/xtensor-stack/xsimd/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# fix pkgconfig path
Patch0:         0001-install-pkgconfig-to-libdir.patch

BuildOption(conf):  -DBUILD_TESTS=ON

BuildRequires:  cmake
# for testing
BuildRequires:  doctest

%description
xsimd provides a unified means for using SIMD features for library authors.
It is a header-only C++ library providing wrappers for SIMD intrinsics and
parallelized, optimized mathematical functions.

%files
%license LICENSE
%doc README.md
%{_includedir}/xsimd/
%{_datadir}/cmake/xsimd/
%{_libdir}/pkgconfig/xsimd.pc

%changelog
%autochangelog
