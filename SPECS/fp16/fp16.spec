# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit_date  20250817
# there is no release version, so we use the letest commit.
%global commit       3d2de1816307bac63c16a297e8c4dc501b4076df
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

Name:           fp16
Version:        %{commit_date}+git%{shortcommit}
Release:        %autorelease
Summary:        Conversion to/from half-precision floating point format
License:        MIT
URL:            https://github.com/Maratyszcza/FP16
#!RemoteAsset:  sha256:65ace2f05fd9434b0acb7a7d3cc6cd96842ea6236b680594af932b359bedbfc1
Source0:        https://github.com/Maratyszcza/FP16/archive/%{commit}/FP16-%{commit}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DFP16_USE_SYSTEM_LIBS=ON
BuildOption(conf):  -DFP16_BUILD_BENCHMARKS=OFF
BuildOption(conf):  -DFP16_BUILD_TESTS=OFF
BuildOption(conf):  -DFP16_BUILD_SHARED_LIBS=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)

%description
Header-only library for conversion to/from half-precision floating point formats.

%package        devel
Summary:        Conversion to/from half-precision floating point format

%description    devel
Development files for FP16.

%files devel
%{_includedir}/fp16.h
%{_includedir}/fp16/

%changelog
%{?autochangelog}
