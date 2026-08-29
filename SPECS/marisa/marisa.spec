# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           marisa
Version:        0.3.0
Release:        %autorelease
Summary:        Static and space-efficient trie data structure library
License:        BSD-2-Clause OR LGPL-2.1-or-later
URL:            https://github.com/s-yata/marisa-trie
#!RemoteAsset:  sha256:a3057d0c2da0a9a57f43eb8e07b73715bc5ff053467ee8349844d01da91b5efb
Source0:        https://github.com/s-yata/marisa-trie/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

# Fix cmake to use GNUInstallDirs for correct lib64 path and install shared libraries
Patch2000:      2000-marisa-fix-cmake.patch

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DENABLE_TOOLS=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Matching Algorithm with Recursively Implemented StorAge (MARISA) is a
static and space-efficient trie data structure. libmarisa is a C++
library to provide an implementation of MARISA.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license COPYING.md
%{_libdir}/libmarisa.so.*
%{_bindir}/marisa-*

%files devel
%{_includedir}/marisa*
%{_libdir}/*.so
%{_libdir}/pkgconfig/marisa.pc
%{_libdir}/cmake/Marisa/

%changelog
%autochangelog
