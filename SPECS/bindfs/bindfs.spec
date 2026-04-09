# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bindfs
Version:        1.17.7
Release:        %autorelease
Summary:        A FUSE filesystem for mirroring a directory with altered permissions
License:        GPL-2.0-or-later
URL:            https://bindfs.org/
VCS:            git:https://github.com/mpartel/bindfs
#!RemoteAsset
Source:         https://bindfs.org/downloads/bindfs-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  pkgconfig(fuse)
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake

Requires:       fuse

%description
bindfs is a FUSE filesystem for mirroring a directory to another directory
and altering permission bits in the mirror.

# TODO: enabel when we have ruby.
%check

%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/bindfs
%{_mandir}/man1/bindfs.1*

%changelog
%autochangelog
