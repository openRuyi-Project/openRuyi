# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ecbuild
Version:        3.12.0
Release:        %autorelease
Summary:        ECMWF CMake build system
License:        Apache-2.0
URL:            https://github.com/ecmwf/ecbuild
#!RemoteAsset:  sha256:70c7fc9b17f736a3312167c2c36d13b3b5833a255fe2b168b2886ad7c743ffdf
Source0:        %{url}/archive/refs/tags/%{version}/%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-fortran
BuildRequires:  pkgconfig(python3)

%description
ecbuild is the CMake-based build system used by ECMWF software.

%files
%doc AUTHORS
%doc README.rst
%license LICENSE
%{_bindir}/ecbuild
%{_datadir}/ecbuild/
%{_prefix}/lib/cmake/ecbuild/

%changelog
%autochangelog
