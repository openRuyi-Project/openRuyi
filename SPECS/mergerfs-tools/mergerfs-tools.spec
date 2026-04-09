# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit  80d6c9511da554009415d67e7c0ead1256c1fc41
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mergerfs-tools
Version:        0+git20260202.%{shortcommit}
Release:        %autorelease
Summary:        Optional tools for mergerfs
License:        ISC
URL:            https://github.com/trapexit/mergerfs-tools
#!RemoteAsset
Source:         https://github.com/trapexit/mergerfs-tools/archive/%{commit}/mergerfs-tools-%{commit}.tar.gz
BuildSystem:    autotools

BuildOption(install):  PREFIX=%{_prefix}

BuildRequires:  make

Requires:       python3
Requires:       rsync

%description
A set of tools to help manage data in a mergerfs pool.
Includes tools for balancing, duplication, consolidation, and more.

# No configure.
%conf

# No build.
%build

# No tests.
%check

%files
%license LICENSE
%doc README.md
%{_bindir}/mergerfs.balance
%{_bindir}/mergerfs.consolidate
%{_bindir}/mergerfs.ctl
%{_bindir}/mergerfs.dedup
%{_bindir}/mergerfs.dup
%{_bindir}/mergerfs.fsck
%{_bindir}/mergerfs.mktrash

%changelog
%autochangelog
