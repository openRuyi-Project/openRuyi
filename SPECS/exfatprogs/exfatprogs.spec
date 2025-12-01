# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           exfatprogs
Version:        1.2.9
Release:        %autorelease
Summary:        Userspace utilities for exFAT filesystems
License:        GPL-2.0-only
URL:            https://github.com/exfatprogs/exfatprogs
#!RemoteAsset
Source:         https://github.com/exfatprogs/exfatprogs/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --enable-shared=yes
BuildOption(conf): --enable-static=no

BuildRequires:  autoconf automake gcc libtool make

%description
Utilities for creating, checking, and repairing exFAT filesystems.
This package contains the command-line tools.

%conf -p
autoreconf -vif

%files
%license COPYING
%doc README.md
%{_sbindir}/dump.exfat
%{_sbindir}/exfat2img
%{_sbindir}/exfatlabel
%{_sbindir}/fsck.exfat
%{_sbindir}/mkfs.exfat
%{_sbindir}/tune.exfat
%{_mandir}/man8/dump.exfat.*
%{_mandir}/man8/exfat2img.*
%{_mandir}/man8/exfatlabel.*
%{_mandir}/man8/fsck.exfat.*
%{_mandir}/man8/mkfs.exfat.*
%{_mandir}/man8/tune.exfat.*

%changelog
%{?autochangelog}
