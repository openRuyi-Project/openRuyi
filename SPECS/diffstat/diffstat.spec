# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           diffstat
Version:        1.68
Release:        %autorelease
Summary:        A utility for displaying a histogram of diff output
License:        X11
URL:            https://invisible-island.net/diffstat
# VCS: No VCS link available
#!RemoteAsset
Source:         https://invisible-mirror.net/archives/diffstat/diffstat-%{version}.tgz
BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

%description
diffstat reads the output of the diff command and displays a histogram of the
insertions, deletions, and modifications in each file. It is commonly used
to provide a summary of changes in large, complex patch files.

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc CHANGES README
%{_bindir}/diffstat
%{_mandir}/man1/diffstat.1*

%changelog
%autochangelog
