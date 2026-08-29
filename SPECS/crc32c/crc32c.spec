# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           crc32c
Version:        1.1.2
Release:        %autorelease
Summary:        CRC32C implementation with CPU-specific acceleration
License:        BSD-3-Clause
URL:            https://github.com/google/crc32c
#!RemoteAsset:  sha256:ac07840513072b7fcebda6e821068aa04889018f24e10e46181068fb214d7e56
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

# Fix CMake 4.0 compatibility
# https://github.com/google/crc32c/pull/68
Patch1000:      1000-Fix-CMake-4.0-compatibility.patch
# Use system libraries for missing third-party submodules.
Patch2000:      2000-use-system-deps-fix-missing-thirdparty.patch

BuildRequires:  cmake
BuildRequires:  cmake(glog)
BuildRequires:  pkgconfig(benchmark)
BuildRequires:  pkgconfig(gflags)
BuildRequires:  pkgconfig(gtest)

%description
CRC32C is a portable implementation of the CRC32C checksum with
CPU-specific acceleration.

%package        devel
Summary:        Development files for crc32c
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and CMake metadata for developing applications using crc32c.

%files
%doc AUTHORS
%doc README.md
%license LICENSE
%{_libdir}/libcrc32c.so.*

%files devel
%{_includedir}/crc32c/
%{_libdir}/cmake/Crc32c/
%{_libdir}/libcrc32c.so

%changelog
%autochangelog
