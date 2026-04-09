# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           genimage
Version:        19
Release:        %autorelease
Summary:        A tool to generate filesystem and disk images
License:        GPL-2.0-only
URL:            https://github.com/pengutronix/genimage/
#!RemoteAsset
Source:         https://github.com/pengutronix/genimage/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  libtool

%description
genimage is a tool to generate multiple filesystem and flash/disk
images from a given root filesystem tree.

%conf -p
autoreconf -fiv

# TODO: enable tests when we have fakeroot.
%check

%files
%license COPYING
%doc README.rst
%{_bindir}/genimage

%changelog
%autochangelog
