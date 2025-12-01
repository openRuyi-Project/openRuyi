# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           isa-l_crypto
Version:        2.25.0
Release:        %autorelease
Summary:        Intelligent Storage Acceleration Library with crypto
License:        BSD-3-Clause
URL:            https://github.com/intel/isa-l_crypto
#!RemoteAsset
Source0:        https://github.com/intel/isa-l_crypto/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz


Patch1: 0001-fips-enable-aes-self-tests-only-on-x86-and-aarch64.patch
Patch2: 0002-build-add-riscv64-support.patch
Patch3: 0003-sha1_mb-Add-missing-ISAL_-prefixes-to-base-aliases.patch

BuildSystem:    autotools

BuildOption(conf): --disable-static

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# for tests.
BuildRequires:  openssl-devel
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
%make_build tests

%files
%{_libdir}/libisal_crypto.so.2*
%license LICENSE

%files devel
%{_includedir}/isa-l_crypto.h
%{_includedir}/isa-l_crypto
%{_libdir}/libisal_crypto.so
%{_libdir}/pkgconfig/libisal_crypto.pc

%changelog
%{?autochangelog}
