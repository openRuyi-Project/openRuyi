# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# there is no release version, so we use the letest commit.
%global commit       63058eff77e11aa15bf531df5dd34395ec3017c8
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

Name:           fxdiv
Version:        0+git20260202.%{shortcommit}
Release:        %autorelease
Summary:        Header for division via fixed-point math
License:        MIT
URL:            https://github.com/Maratyszcza/FXdiv
#!RemoteAsset:  sha256:ec74d882a0a47cfd9c0f95bc4fae9901a4ade802a96a3b76e02671bb7340a4c5
Source0:        https://github.com/Maratyszcza/FXdiv/archive/%{commit}/FXdiv-%{commit}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DFXDIV_USE_SYSTEM_LIBS=ON
BuildOption(conf):  -DFXDIV_BUILD_BENCHMARKS=OFF
BuildOption(conf):  -DFXDIV_BUILD_TESTS=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Header-only library for division via fixed-point multiplication by inverse.
This package contains the header file.

%package        devel
Summary:        Header for division via fixed-point math

%description    devel
Development files for fxdiv.

%files
%license LICENSE
%doc README.md

%files devel
%{_includedir}/fxdiv.h

%changelog
%autochangelog
