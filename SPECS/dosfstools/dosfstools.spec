# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dosfstools
Version:        4.2
Release:        %autorelease
Summary:        FAT file system userspace tools
License:        GPL-3.0-or-later
URL:            https://github.com/dosfstools/dosfstools
#!RemoteAsset
Source:         https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

Patch:          0001-Fix-vasprintf-implementation.patch

BuildOption(conf):   --enable-compat-symlinks
BuildOption(build):  CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fno-strict-aliasing"

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake

%description
The dosfstools package contains programs mkfs.fat, fsck.fat and fatlabel to
create, check and label FAT family file systems.

%files
%doc %{_docdir}/%{name}
%license COPYING
%{_sbindir}/*
%{_mandir}/man8/*

%changelog
%autochangelog
