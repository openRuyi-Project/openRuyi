# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           isa-l
Version:        2.31.1
Release:        %autorelease
Summary:        Intelligent Storage Acceleration Library
License:        BSD-3-Clause
URL:            https://github.com/intel/isa-l
#!RemoteAsset
Source0:        https://github.com/intel/isa-l/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:    autotools

BuildOption(conf): --disable-static

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%ifarch x86_64
BuildRequires:  nasm
%endif

%description
Collection of low-level functions used in storage applications.
Contains fast erasure codes that implement a general Reed-Solomon type
encoding for blocks of data that helps protect against erasure of
whole blocks. The general ISA-L library contains an expanded set of
functions used for data protection, hashing, encryption, etc.

This package contains the shared library.

%package        devel
Summary:        Intel(R) Intelligent Storage Acceleration Library - devel files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Collection of low-level functions used in storage applications.
Contains fast erasure codes that implement a general Reed-Solomon type
encoding for blocks of data that helps protect against erasure of
whole blocks. The general ISA-L library contains an expanded set of
functions used for data protection, hashing, encryption, etc.

This package contains the development files needed to build against
the shared library.

%package        tools
Summary:        Intel(R) Intelligent Storage Acceleration Library - tool
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
Collection of low-level functions used in storage applications.
Contains fast erasure codes that implement a general Reed-Solomon type
encoding for blocks of data that helps protect against erasure of
whole blocks. The general ISA-L library contains an expanded set of
functions used for data protection, hashing, encryption, etc.

This package contains CLI tools.

%prep -a
./autogen.sh

%check
%make_build check
%make_build tests

%files
%{_libdir}/libisal.so.2*
%license LICENSE

%files devel
%{_includedir}/isa-l.h
%{_includedir}/isa-l
%{_libdir}/libisal.so
%{_libdir}/pkgconfig/libisal.pc
%doc examples

%files tools
%{_bindir}/igzip
%{_mandir}/man1/igzip.1*

%changelog
%{?autochangelog}
