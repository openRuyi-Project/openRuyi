# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           leveldb
Version:        1.23
Release:        %autorelease
Summary:        A fast and lightweight key/value database library by Google
License:        BSD-3-Clause
URL:            https://github.com/google/leveldb
#!RemoteAsset
Source:         https://github.com/google/leveldb/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_SHARED_LIBS:BOOL=ON
BuildOption(conf):  -DLEVELDB_BUILD_TESTS:BOOL=OFF
BuildOption(conf):  -DLEVELDB_BUILD_BENCHMARKS:BOOL=OFF
BuildOption(conf):  -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake(Snappy)

%description
LevelDB is a fast key-value storage library written at Google that provides an
ordered mapping from string keys to string values.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and development libraries for leveldb.

%files
%license LICENSE
%doc AUTHORS README.md NEWS
%{_libdir}/libleveldb.so.*

%files devel
%doc CONTRIBUTING.md TODO
%{_includedir}/leveldb/
%dir %{_libdir}/cmake
%{_libdir}/cmake/leveldb
%{_libdir}/libleveldb.so

%changelog
%autochangelog
