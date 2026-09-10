# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           genimage
Version:        20
Release:        %autorelease
Summary:        A tool to generate filesystem and disk images
License:        GPL-2.0-only
URL:            https://github.com/pengutronix/genimage/
#!RemoteAsset:  sha256:4cadce884f920a4663c59652f1b87787772628ee4e2867a48e94c69f122fae57
Source:         https://github.com/pengutronix/genimage/archive/refs/tags/v%{version}.tar.gz
# Upstream official patch
# https://github.com/pengutronix/genimage/issues/309
Patch1000:         1000-test-erofs-add-support-for-more-erofs-utils-versions.patch
Patch2000:         2000-util-make-seeded-UUID-generation-deterministic.patch
Patch2001:         2001-util-handle-short-writes.patch
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libconfuse)
# Tests
BuildRequires:  btrfs-progs
BuildRequires:  cpio
BuildRequires:  dosfstools
BuildRequires:  e2fsprogs
BuildRequires:  erofs-utils
BuildRequires:  f2fs-tools
BuildRequires:  fakeroot
BuildRequires:  genext2fs
BuildRequires:  jq
BuildRequires:  mdadm
BuildRequires:  mtd-utils
BuildRequires:  mtd-utils-ubi
BuildRequires:  mtools
BuildRequires:  openssl
BuildRequires:  qemu-tools
BuildRequires:  squashfs-tools
BuildRequires:  veritysetup

%description
genimage is a tool to generate multiple filesystem and flash/disk
images from a given root filesystem tree.

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc README.rst
%{_bindir}/genimage

%changelog
%autochangelog
