# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dwarfs
Version:        0.14.1
Release:        %autorelease
Summary:        Deduplicating compressed read-only file system
License:        GPL-3.0-or-later AND MIT
URL:            https://github.com/mhx/dwarfs
#!RemoteAsset
Source0:        https://github.com/mhx/dwarfs/releases/download/v%{version}/dwarfs-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_EXE_LINKER_FLAGS="-lboost_filesystem -lboost_process"
BuildOption(conf):  -DWITH_TESTS=ON
BuildOption(conf):  -DPREFER_SYSTEM_GTEST=ON

BuildRequires:  bison flex
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  boost-devel
BuildRequires:  parallel-hashmap
BuildRequires:  double-conversion-devel
BuildRequires:  range-v3-devel
BuildRequires:  utf8cpp
# the following dependency is disabled
# BuildRequires:  pkgconfig(benchmark)
# BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  glog-devel
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(nlohmann_json)
# check requirements
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  fuse3

%description
The Deduplicating Warp-speed Advanced Read-only File System.
DwarFS is a deduplicating compressed read-only file system
particularly suited for very redundant data.
Compared to SquashFS, it is typically more efficient.

%package        devel
Summary:        DwarFS development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The Deduplicating Warp-speed Advanced Read-only File System.
DwarFS is a deduplicating compressed read-only file system
particularly suited for very redundant data.
Compared to SquashFS, it is typically more efficient.
This package contains the development files for DwarFS.

# disable check, in qemu-system env, all tests could be passed
%check

%files
%license LICENSE
%doc README.md
%{_mandir}/*/*dwarfs*
%{_bindir}/*dwarfs*
%{_libdir}/*.so.*
%{_libdir}/libdwarfs*.so
%{_sbindir}/mount.dwarfs
%{_datadir}/applications/*.desktop
%{_datadir}/mime/*
%{_datadir}/bash-completion/*
%{_datadir}/zsh/*

%files devel
%{_includedir}/dwarfs
%{_libdir}/cmake/dwarfs

%changelog
%autochangelog
