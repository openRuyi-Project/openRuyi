# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           f2fs-tools
Version:        1.16.0
Release:        %autorelease
Summary:        Tools for the Flash-Friendly File System (F2FS)
License:        GPL-2.0-or-later
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git
#!RemoteAsset
Source:         https://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/f2fs-tools-%{version}.tar.gz
BuildSystem:    autotools

Patch0:         0001-f2fs-tools-1.16.0-c23.patch

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  m4
BuildRequires:  util-linux-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  make
BuildRequires:  gcc

%description
This package provides tools for the Flash-Friendly File System (F2FS),
a filesystem designed for NAND flash memory-based storage devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries and header files needed to develop
applications that use the F2FS library.

%conf -p
autoreconf -fiv

%install -a
install -m 644 mkfs/f2fs_format_utils.h %{buildroot}%{_includedir}

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_sbindir}/mkfs.f2fs
%{_sbindir}/fibmap.f2fs
%{_sbindir}/fsck.f2fs
%{_sbindir}/dump.f2fs
%{_sbindir}/parse.f2fs
%{_sbindir}/defrag.f2fs
%{_sbindir}/resize.f2fs
%{_sbindir}/sload.f2fs
%{_sbindir}/f2fs_io
%{_sbindir}/f2fscrypt
%{_sbindir}/f2fslabel
%{_libdir}/*.so.*
%{_mandir}/man8/*f2*.gz

%files devel
%{_includedir}/*.h
%{_libdir}/*.so

%changelog
%autochangelog
