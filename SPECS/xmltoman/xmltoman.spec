# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xmltoman
Version:        0.4
Release:        %autorelease
Summary:        Scripts to convert XML to man pages or HTML
License:        GPL-2.0-only
URL:            https://github.com/Distrotech/xmltoman
#!RemoteAsset
Source:         https://github.com/Distrotech/xmltoman/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  PREFIX="%{_prefix}"
BuildOption(install):  PREFIX="%{_prefix}"

BuildRequires:  perl(XML::Parser)
BuildRequires:  make

Requires:       perl(XML::Parser)

%description
xmltoman and xmlmantohtml are two very simple scripts for converting XML
to groff (man pages) or HTML.

# No configure
%conf

# No tests.
%check

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/xmlmantohtml
%{_bindir}/xmltoman
%dir %{_datadir}/xmltoman
%{_datadir}/xmltoman/xmltoman.css
%{_datadir}/xmltoman/xmltoman.dtd
%{_datadir}/xmltoman/xmltoman.xsl

%changelog
%autochangelog
