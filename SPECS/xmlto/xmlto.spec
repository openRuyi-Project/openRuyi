# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xmlto
Version:        0.0.29
Release:        %autorelease
Summary:        Tool for Converting XML Files to Various Formats
License:        GPL-2.0-or-later
URL:            https://pagure.io/xmlto/
VCS:            git:https://pagure.io/xmlto.git
#!RemoteAsset:  sha256:40504db68718385a4eaa9154a28f59e51e59d006d1aa14f5bc9d6fded1d6017a
Source:         https://anduin.linuxfromscratch.org/BLFS/xmlto/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  XMLTO_BASH_PATH=/bin/bash

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-dtds
BuildRequires:  docbook-xsl
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libxslt

Requires:       docbook-dtds
Requires:       docbook-xsl
Requires:       findutils
Requires:       libxml2
Requires:       libxslt
Requires:       util-linux

%description
This is a package for converting XML files to various formats using XSL
stylesheets. As a processor it depends on xsltproc and as a formatter
for print output it makes use of passivetex.

%conf -p
autoreconf -fi
export CFLAGS="%{build_cflags} -Wno-error=implicit-int"

%install -a
install -d %{buildroot}%{_datadir}/xmlto/xsl
%fdupes %{buildroot}%{_datadir}/xmlto

%files
%doc AUTHORS.md README.md ChangeLog FAQ.md THANKS.md NEWS.md
%license COPYING
%{_bindir}/xmlto
%{_bindir}/xmlif
%{_mandir}/man1/xmlto.1%{?ext_man}
%{_mandir}/man1/xmlif.1%{?ext_man}
%{_datadir}/xmlto

%changelog
%autochangelog
