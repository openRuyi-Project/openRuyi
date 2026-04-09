# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mtd-utils
Version:        2.3.0
Release:        %autorelease
Summary:        Utilities for dealing with MTD (flash) devices
License:        GPL-2.0-or-later
URL:            http://www.linux-mtd.infradead.org/
VCS:            git:git://git.infradead.org/mtd-utils.git
#!RemoteAsset
Source:         https://infraroot.at/pub/mtd/mtd-utils-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf): --without-tests
BuildOption(conf): --disable-unit-tests

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(lzo2)

%description
The mtd-utils package contains utilities for handling MTD devices,
and for dealing with FTL, NFTL, JFFS2, etc.

%package        ubi
Summary:        Utilities for dealing with UBI
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    ubi
The mtd-utils-ubi package contains utilities for manipulating UBI on
MTD (flash) devices.

%conf -p
autoreconf -fiv

%files
%license COPYING
%{_sbindir}/doc*
%{_sbindir}/flash*
%{_sbindir}/ftl*
%{_sbindir}/jffs2dump
%{_sbindir}/jffs2reader
%{_sbindir}/lsmtd
%{_sbindir}/mkfs.jffs2
%{_sbindir}/mtd_debug
%{_sbindir}/nand*
%{_sbindir}/nftl*
%{_sbindir}/recv_image
%{_sbindir}/rfd*
%{_sbindir}/serve_image
%{_sbindir}/sumtool
%{_sbindir}/mkfs.ubifs
%{_sbindir}/mtdinfo
%{_sbindir}/mtdpart
%{_sbindir}/fectest
%{_mandir}/man*/*

%files ubi
%{_sbindir}/ubi*
%{_sbindir}/mount.ubifs
%{_sbindir}/fsck.ubifs

%changelog
%autochangelog
