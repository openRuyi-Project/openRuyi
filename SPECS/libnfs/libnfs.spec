# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libnfs
Version:        6.0.2
Release:        %autorelease
Summary:        Client library for accessing NFS shares over a network
License:        LGPL-2.1-or-later AND BSD-2-Clause AND GPL-3.0-or-later
URL:            https://github.com/sahlberg/libnfs
#!RemoteAsset
Source:         https://github.com/sahlberg/libnfs/archive/refs/tags/libnfs-%{version}.tar.gz
BuildSystem:    autotools

# https://github.com/sahlberg/libnfs/pull/518
Patch0:         0001-libnfs-6.0.2-fix_gnutls_undefined_symbols.patch
# https://github.com/sahlberg/libnfs/commit/2cdfedaba379cbb512d3c203a1b9eae795f4fb23
Patch1:         0002-libnfs-6.0.2-fix_missing_include.patch
# https://github.com/sahlberg/libnfs/pull/558
# https://github.com/sahlberg/libnfs/pull/582
Patch2:         0003-libnfs-6.0.2-fix_getlogin_null_segfault.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-examples
BuildOption(conf):  --disable-werror
BuildOption(conf):  --enable-pthread

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  libtool
BuildRequires:  make

%description
The libnfs package contains a library of functions for accessing NFSv2,
NFSv3, and NFSv4 servers from user space.

%package        devel
Summary:        Development files for libnfs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libnfs-devel package contains libraries, header files, and examples
for developing applications that use libnfs.

%prep -a
autoreconf -vif

%build -p
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%files
%license COPYING LICENCE-*.txt
%doc README
%{_libdir}/libnfs.so.16*
%{_bindir}/nfs-*
%{_mandir}/man1/nfs-*.1*

%files devel
%doc examples/*.c
%{_includedir}/nfsc/
%{_libdir}/libnfs.so
%{_libdir}/pkgconfig/libnfs.pc

%changelog
%autochangelog
