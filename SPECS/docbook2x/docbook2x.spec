# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           docbook2x
Version:        0.8.8
Release:        %autorelease
Summary:        Convert DocBook into man pages and Texinfo
License:        MIT
URL:            http://docbook2x.sourceforge.net/
#!RemoteAsset
Source:         http://downloads.sourceforge.net/docbook2x/docbook2X-%{version}.tar.gz
BuildSystem:    autotools

# to avoid clashing with docbook2* from docbook-utils
BuildOption(conf):  --program-transform-name='s/docbook2/db2x_docbook2/'

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libxslt
BuildRequires:  openjade
BuildRequires:  texinfo
BuildRequires:  perl(XML::SAX::ParserFactory)

Requires:       libxslt
Requires:       openjade
Requires:       texinfo
Requires:       perl(XML::SAX::ParserFactory)

%description
docbook2X converts DocBook documents into man pages and Texinfo
documents.

%install -a
rm -f %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_datadir}/doc/

rm -rf __dist_html
mkdir -p __dist_html/html
cp -p doc/*.html __dist_html/html

# TODO: Broken check also no distro is checking it - 251
%check

%files
%doc COPYING README THANKS AUTHORS __dist_html/html/
%{_bindir}/db2x_manxml
%{_bindir}/db2x_texixml
%{_bindir}/db2x_xsltproc
%{_bindir}/db2x_docbook2man
%{_bindir}/db2x_docbook2texi
%{_bindir}/sgml2xml-isoent
%{_bindir}/utf8trans
%dir %{_datadir}/docbook2X
%{_datadir}/docbook2X/VERSION
%dir %{_datadir}/docbook2X/charmaps
%dir %{_datadir}/docbook2X/dtd
%dir %{_datadir}/docbook2X/xslt
%{_datadir}/docbook2X/charmaps/*
%{_datadir}/docbook2X/dtd/*
%{_datadir}/docbook2X/xslt/*
%{_mandir}/man1/*.1*
%{_infodir}/docbook2*

%changelog
%autochangelog
