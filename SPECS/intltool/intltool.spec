# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           intltool
Version:        0.51.0
Release:        %autorelease
Summary:        Utility scripts for internationalizing XML
License:        GPL-2.0-or-later
URL:            https://launchpad.net/intltool
# VCS: Bazzar upstream will be deprecated so no upstream?? - 251
#!RemoteAsset
Source:         https://launchpad.net/intltool/trunk/%{version}/+download/intltool-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  perl
BuildRequires:  perl(XML::Parser)

Requires:       automake
Requires:       gettext-devel
Requires:       perl(XML::Parser)
Requires:       perl(Getopt::Long)
Requires:       patch

%description
Intltool is a collection of scripts that helps with extracting translatable
strings from various source files, and merging them back into template files.

%files
%doc README
%license COPYING AUTHORS
%{_bindir}/intltool*
%{_datadir}/intltool
%{_datadir}/aclocal/intltool*
%{_mandir}/man8/*

%changelog
%autochangelog
