# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           frozen
Version:        1.2.0
Release:        %autorelease
Summary:        Compile-time associative containers for C++
License:        Apache-2.0
URL:            https://github.com/serge-sans-paille/frozen
#!RemoteAsset:  sha256:ed8339c017d7c5fe019ac2c642477f435278f0dc643c1d69d3f3b1e95915e823
Source0:        https://github.com/serge-sans-paille/frozen/archive/refs/tags/%{version}.tar.gz#/frozen-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    cmake
# The 1.2.0 tag still reports 1.1.0 to downstream CMake consumers.
# https://github.com/serge-sans-paille/frozen/blob/1.2.0/CMakeLists.txt#L21
Patch2000:      2000-report-the-release-version-in-CMake-metadata.patch

BuildOption(conf):  -Dfrozen.tests=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Frozen builds immutable maps and sets at compile time. The unordered
containers use a perfect hash to look up keys without dynamic allocation.

%package        devel
Summary:        Headers and CMake targets for %{name}

%description    devel
C++ headers and CMake targets for using frozen associative containers.

%files devel
%doc README.rst
%license LICENSE
%{_datadir}/cmake/frozen/
%{_includedir}/frozen/

%changelog
%autochangelog
