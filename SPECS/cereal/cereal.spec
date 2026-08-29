# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cereal
Version:        1.3.2
Release:        %autorelease
Summary:        Header-only C++11 serialization library
License:        BSD-3-Clause AND BSL-1.0 AND Zlib AND MIT AND (MIT OR BSL-1.0)
URL:            https://github.com/USCiLab/cereal
#!RemoteAsset:  sha256:16a7ad9b31ba5880dac55d62b5d6f243c3ebc8d46a3514149e56b5e7ea81f85f
Source0:        https://github.com/USCiLab/cereal/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    cmake

BuildOption(conf):  -DSKIP_PORTABILITY_TEST=ON
BuildOption(conf):  -DWITH_WERROR=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  boost-devel

%description
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

%package        devel
Summary:        Development headers and CMake files for %{name}

%description    devel
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

This package contains development headers and CMake files for cereal.

%files devel
%doc README.md
%license LICENSE
%{_includedir}/cereal
%{_libdir}/cmake/cereal

%changelog
%autochangelog
