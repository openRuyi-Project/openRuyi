# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%ifarch riscv64
# GCC 15 ICEs on RVV intrinsics in xxhash.h under LTO (riscv-vector-builtins.cc:4470).
%define _lto_cflags %{nil}
%endif

Name:           rocksdb
Version:        10.5.1
Release:        %autorelease
Summary:        A Persistent Key-Value Store for Flash and RAM Storage
License:        GPL-2.0-only OR Apache-2.0 AND BSD-2-Clause
URL:            https://github.com/facebook/rocksdb
#!RemoteAsset:  sha256:7ec942baab802b2845188d02bc5d4e42c29236e61bcbc08f5b3a6bdd92290c22
Source:         https://github.com/facebook/rocksdb/archive/refs/tags/v10.5.1.tar.gz
BuildSystem:    cmake

Patch0:         0001-no_rpath.patch
Patch1:         0002-disable_static.patch
# https://github.com/facebook/rocksdb/pull/14604
Patch1000:      1000-util-sync-xxhash.h-with-upstream-dev-for-RISC-V-RVV.patch

BuildOption(conf):  -DWITH_BZ2=ON
BuildOption(conf):  -DWITH_SNAPPY=ON
BuildOption(conf):  -DWITH_LZ4=ON
BuildOption(conf):  -DWITH_ZSTD=ON
BuildOption(conf):  -DWITH_ZLIB=ON
BuildOption(conf):  -DZSTD_INCLUDE_DIRS=%{_includedir}
BuildOption(conf):  -DWITH_BENCHMARK_TOOLS=ON
BuildOption(conf):  -DWITH_CORE_TOOLS=ON
BuildOption(conf):  -DWITH_TOOLS=ON
BuildOption(conf):  -DUSE_RTTI=ON
BuildOption(conf):  -DPORTABLE=1
BuildOption(conf):  -DFAIL_ON_WARNINGS=OFF
BuildOption(conf):  -DWITH_TESTS=ON

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  cmake(Snappy)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(gflags)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  perl
BuildRequires:  pkgconfig(python3)

%description
RocksDB is a library that forms the core building block for a fast key value
server, especially suited for storing data on flash drives. It has a
Log-Structured-Merge-Database (LSM) design with flexible trade offs between
Write-Amplification-Factor (WAF), Read-Amplification-Factor (RAF) and
Space-Amplification-Factor (SAF). It has multi-threaded compaction, making it
specially suitable for storing multiple terabytes of data in a single database.

%package        devel
Summary:        Development files for RocksDB
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for RocksDB.

%install -a
# Missing steps in build script
install -dD -m 755 %{buildroot}%{_bindir}
install -m 755 %{__cmake_builddir}/cache_bench %{buildroot}%{_bindir}/cache_bench
install -m 755 %{__cmake_builddir}/db_bench %{buildroot}%{_bindir}/db_bench
install -m 755 %{__cmake_builddir}/tools/ldb %{buildroot}%{_bindir}/ldb
install -m 755 %{__cmake_builddir}/tools/sst_dump %{buildroot}%{_bindir}/sst_dump

%files
%doc README.md
%doc HISTORY.md
%doc AUTHORS
%license COPYING
%license LICENSE.Apache
%license LICENSE.leveldb
%{_libdir}/librocksdb.so.10
%{_libdir}/librocksdb.so.10.5.1
%{_bindir}/cache_bench
%{_bindir}/db_bench
%{_bindir}/ldb
%{_bindir}/sst_dump

%files devel
%doc README.md
%doc LANGUAGE-BINDINGS.md
%license COPYING
%license LICENSE.Apache
%license LICENSE.leveldb
%{_libdir}/librocksdb.so
%{_libdir}/cmake/rocksdb
%{_libdir}/pkgconfig/rocksdb.pc
%{_includedir}/rocksdb

%changelog
%autochangelog
