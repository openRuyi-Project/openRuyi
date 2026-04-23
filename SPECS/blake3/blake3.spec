# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           blake3
Version:        1.8.4
Release:        %autorelease
Summary:        Official C implementation of the BLAKE3 cryptographic hash function
License:        Apache-2.0
URL:            https://github.com/BLAKE3-team/BLAKE3
#!RemoteAsset:  sha256:b5ee5f5c5e025eb2733ae3af8d4c0e53bb66dff35095decfd377f1083e8ac9be
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# Add support for RISC-V V extension
# see https://github.com/BLAKE3-team/BLAKE3/pull/542
Patch0:         riscv-v.patch

BuildOption(conf):  -S c
BuildOption(conf):  -DBLAKE3_USE_TBB=ON

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(tbb)

%description
BLAKE3 is a cryptographic hash function that is:
- Much faster than MD5, SHA-1, SHA-2, SHA-3, and BLAKE2.
- Secure, unlike MD5 and SHA-1. And secure against length extension, unlike
  SHA-2.
- Highly parallelizable across any number of threads and SIMD lanes, because
  it's a Merkle tree on the inside.
- Capable of verified streaming and incremental updates, again because it's a
  Merkle tree.
- A PRF, MAC, KDF, and XOF, as well as a regular hash.
- One algorithm with no variants, which is fast on x86-64 and also on smaller
  architectures.

%package        devel
Summary:        Development files for the %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides the development files for the %{name} library.

%build -p
export ASMFLAGS="%{build_cflags}"

%files
%license LICENSE_A2
%{_libdir}/libblake3.so.0
%{_libdir}/libblake3.so.%{version}

%files devel
%doc c/example.c
%doc c/README.md
%{_includedir}/blake3.h
%{_libdir}/libblake3.so
%{_libdir}/cmake/blake3/
%{_libdir}/pkgconfig/libblake3.pc

%changelog
%autochangelog
