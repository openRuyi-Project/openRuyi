# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           assimp
Version:        6.0.5
Release:        %autorelease
Summary:        Library for importing and exporting 3D asset formats
License:        BSD-3-Clause AND BSL-1.0 AND ISC AND MIT AND Unlicense AND Zlib
URL:            https://assimp.org/
VCS:            git:https://github.com/assimp/assimp.git
#!RemoteAsset:  git+https://github.com/assimp/assimp.git#v%{version}
#!CreateArchive
Source0:        %{name}-%{version}.tar.gz
BuildSystem:    cmake

# Use system zlib and retain the upstream unit tests; avoid compiler-version
# dependent failures from treating third-party warnings as errors.
BuildOption(conf):  -DASSIMP_BUILD_ZLIB=OFF
BuildOption(conf):  -DASSIMP_BUILD_TESTS=ON
BuildOption(conf):  -DASSIMP_WARNINGS_AS_ERRORS=OFF
BuildOption(conf):  -DASSIMP_IGNORE_GIT_HASH=ON

BuildRequires:  cmake
BuildRequires:  pkgconfig(zlib)

%description
The Open Asset Import Library imports a wide range of 3D asset formats into a
common in-memory representation. It also provides post-processing operations
and exports to several popular formats.

%package        devel
Summary:        Development files for the Open Asset Import Library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, CMake configuration and pkg-config metadata for developing applications
with the Open Asset Import Library.

%check
# Upstream builds the tests without enable_testing(), so CTest finds no tests.
cd %{__cmake_builddir}/test
../bin/unit

%files
%doc CHANGES.md Readme.md
%license LICENSE
%{_libdir}/libassimp.so.*

%files devel
%{_includedir}/assimp/
%{_libdir}/cmake/assimp-*/
%{_libdir}/libassimp.so
%{_libdir}/pkgconfig/assimp.pc

%changelog
%autochangelog
