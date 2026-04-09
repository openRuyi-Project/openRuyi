# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <zhengxingda@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bdfresize
Version:        1.5
Release:        %autorelease
Summary:        Utility for resizing bitmap fonts in BDF format
License:        GPL-2.0-only
URL:            http://openlab.jp/efont/
# VCS: No VCS link available
#!RemoteAsset
Source:         http://openlab.ring.gr.jp/efont/dist/tools/bdfresize/bdfresize-%{version}.tar.gz
BuildSystem:    autotools

# The following patches are from Debian bdfresize 1.5-12
Patch1:         010_ftbfs-gcc4.patch
Patch2:         020_minus-sign.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

%description
This package provides a bdfresize command, which can magnify or reduce bitmap
fonts described with the standard BDF format.

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc README NEWS
%{_bindir}/bdfresize
%{_mandir}/man1/bdfresize.1*

%changelog
%autochangelog
