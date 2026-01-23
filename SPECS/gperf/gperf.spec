# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gperf
Version:        3.3
Release:        %autorelease
Summary:        A Compiler Tool for Generating Perfect Hash Functions
License:        GPL-3.0-or-later
URL:            https://gnu.org/software/gperf/
VCS:            git:https://https.git.savannah.gnu.org/git/gperf.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/gperf/gperf-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/gperf/gperf-%{version}.tar.gz.sig
BuildSystem:    autotools

BuildOption(conf):   --htmldir=%{_defaultdocdir}/%{name}

BuildRequires:  gcc-c++

%description
A perfect hash function is simply: a hash function and a data structure
that allows recognition of a key word in a set of words using exactly
one probe into the data structure.

%files
%license COPYING
%doc README NEWS AUTHORS ChangeLog doc/*.html
%{_docdir}/gperf/*
%{_bindir}/gperf
%{_infodir}/gperf.info*
%{_mandir}/man1/gperf.1*

%changelog
%{?autochangelog}
