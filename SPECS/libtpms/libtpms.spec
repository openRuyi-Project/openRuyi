# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libtpms
Version:        0.10.2
Release:        %autorelease
Summary:        Library providing Trusted Platform Module (TPM) functionality
License:        BSD-3-Clause
URL:            https://github.com/stefanberger/libtpms
#!RemoteAsset:  sha256:edac03680f8a4a1c5c1d609a10e3f41e1a129e38ff5158f0c8deaedc719fb127
Source:         https://github.com/stefanberger/libtpms/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

# Fix const-qualifier build failure with newer GCC/glibc toolchains.
Patch2000:      2000-fix-const-qualifier-build-error.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-tpm2
BuildOption(conf):  --with-openssl

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig
BuildRequires:  sed

%description
A library providing TPM functionality for VMs. Targeted for integration
into Qemu.

%package        devel
Summary:        Development files for libtpms
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description   devel
Libtpms header files and documentation.

%conf -p
NOCONFIGURE=1 ./autogen.sh

%files
%license LICENSE
%doc README CHANGES
%{_libdir}/libtpms.so.*

%files devel
%{_includedir}/libtpms/
%{_libdir}/libtpms.so
%{_libdir}/pkgconfig/libtpms.pc
%{_mandir}/man3/TPM*

%changelog
%autochangelog
