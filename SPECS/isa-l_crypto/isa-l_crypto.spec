# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# It's a known issue that LTO causes test failure,
# and the workaround is to disable LTO for now.
# https://github.com/intel/isa-l_crypto/issues/165
%define _lto_cflags %{nil}

Name:           isa-l_crypto
Version:        2.26
Release:        %autorelease
Summary:        Intelligent Storage Acceleration Library with crypto
License:        BSD-3-Clause
URL:            https://github.com/intel/isa-l_crypto
#!RemoteAsset
Source0:        https://github.com/intel/isa-l_crypto/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

# https://github.com/intel/isa-l_crypto/pull/168
Patch1:         0001-mh_sha1-add-an-mh_sha1-assembly-implementation-with-.patch
# https://github.com/intel/isa-l_crypto/pull/172
Patch2:         0001-mh_sha1_murmur3_x64_128-add-an-mh_sha1_murmur3_x64_1.patch

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# for tests.
BuildRequires:  pkgconfig(openssl)
%ifarch x86_64
BuildRequires:  nasm
%endif

%description
ISA-L_crypto is a collection of optimized low-level functions
targeting storage applications.

This package contains the shared library.

%package        devel
Summary:        Intelligent Storage Acceleration Library with crypto - devel files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
ISA-L_crypto is a collection of optimized low-level functions targeting storage applications.

This package contains the development files needed to build against the shared library.

%prep -a
./autogen.sh

%check
%make_build check
%make_build test

%files
%{_libdir}/libisal_crypto.so.2*
%license LICENSE

%files devel
%{_includedir}/isa-l_crypto.h
%{_includedir}/isa-l_crypto
%{_libdir}/libisal_crypto.so
%{_libdir}/pkgconfig/libisal_crypto.pc

%changelog
%autochangelog
