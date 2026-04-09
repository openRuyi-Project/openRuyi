# SPDX-FileCopyrightText: (C) 2025-2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025-2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           asn1c
Version:        0.9.28
Release:        %autorelease
Summary:        ASN.1 Compiler
License:        BSD-2-Clause
URL:            http://lionet.info/asn1c/
VCS:            git:https://github.com/vlm/asn1c
#!RemoteAsset
Source:         https://github.com/vlm/asn1c/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  gcc

%description
Compiles ASN.1 data structures into C source structures that can be
simply marshalled to/unmarshalled from various encoding rules.

%conf -p
autoreconf -fiv

%files
%license LICENSE
%doc BUGS ChangeLog FAQ README.md TODO doc/asn1c-quick.pdf doc/asn1c-usage.pdf
%{_bindir}/*
%{_datadir}/asn1c
%{_mandir}/man1/*
%doc %{_docdir}/asn1c

%changelog
%autochangelog
