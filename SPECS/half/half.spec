# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global rocm_release 7.2
%global rocm_patch   4
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:           half
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm half-precision floating point library
License:        MIT
URL:            https://github.com/ROCm/half
#!RemoteAsset:  sha256:8cbe655d3ef19675e953934cf0cb49fdf899459407fbc6848af52282269fc7f9
Source0:        %{url}/archive/rocm-%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  rocm-cmake

%description
half is a C++ header-only library providing an IEEE-754 conformant
half-precision floating point type along with arithmetic operators,
type conversions, and common mathematical functions. It is part of
the ROCm software stack.

%install -a
rm -f %{buildroot}%{_datadir}/doc/half/LICENSE.txt

%files
%doc README.txt
%license LICENSE.txt
%{_includedir}/half/

%changelog
%autochangelog
