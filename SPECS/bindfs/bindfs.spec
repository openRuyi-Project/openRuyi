# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bindfs
Version:        1.18.4
Release:        %autorelease
Summary:        A FUSE filesystem for mirroring a directory with altered permissions
License:        GPL-2.0-or-later
URL:            https://bindfs.org/
VCS:            git:https://github.com/mpartel/bindfs
#!RemoteAsset:  sha256:3266d0aab787a9328bbb0ed561a371e19f1ff077273e6684ca92a90fedb2fe24
Source:         https://bindfs.org/downloads/bindfs-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  pkgconfig(fuse)
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake

Requires:       fuse

%description
bindfs is a FUSE filesystem for mirroring a directory to another directory
and altering permission bits in the mirror.

# Our build system doesn't provide /dev/fuse in the build environment
%check

%files
%doc ChangeLog README.md
%license COPYING
%{_bindir}/bindfs
%{_mandir}/man1/bindfs.1*

%changelog
%autochangelog
