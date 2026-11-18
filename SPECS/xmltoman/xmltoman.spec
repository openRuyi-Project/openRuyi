# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xmltoman
Version:        0.6
Release:        %autorelease
Summary:        Scripts to convert XML to man pages or HTML
License:        GPL-2.0-only
URL:            https://github.com/atsb/xmltoman
#!RemoteAsset:  sha256:cdd5063ca8beb6fe51ec6ab85f70d31fc8ed034e85e32dd9b7c0b7142bb72fb6
Source:         https://github.com/atsb/xmltoman/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  prefix="%{_prefix}"
BuildOption(install):  prefix="%{_prefix}"

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
%doc ChangeLog README
%license COPYING
%{_bindir}/xmlmantohtml
%{_bindir}/xmltoman
%{_mandir}/man1/xmlmantohtml.1*
%{_mandir}/man1/xmltoman.1*
%dir %{_datadir}/xmltoman
%{_datadir}/xmltoman/xmltoman.css
%{_datadir}/xmltoman/xmltoman.dtd
%{_datadir}/xmltoman/xmltoman.xsl

%changelog
%autochangelog
