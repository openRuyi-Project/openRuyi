# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define byaccdate 20260126

Name:           byacc
Version:        2.0.%{byaccdate}
Release:        %autorelease
Summary:        A parser generator
License:        LicenseRef-openRuyi-Public-Domain
URL:            https://invisible-island.net/byacc/byacc.html
# VCS: No VCS link available
#!RemoteAsset:  sha256:b618c5fb44c2f5f048843db90f7d1b24f78f47b07913c8c7ba8c942d3eb24b00
Source:         https://invisible-mirror.net/archives/byacc/byacc-%{byaccdate}.tgz
BuildSystem:    autotools

BuildRequires:  gcc

%description
Berkeley Yacc is an LALR(1) parser generator, made as compatible as possible
with AT&T Yacc. It can accept any input specification that conforms to the
AT&T Yacc documentation.

%prep -a
find . -type f -name \*.c -print0 | xargs -0 sed -i 's/YYSTACKSIZE 500/YYSTACKSIZE 10000/g'

# as same as ncurses,configure: error: unrecognized option: --docdir=/usr/share/doc/byacc
%conf
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --disable-dependency-tracking \
    --program-prefix=b

%files
%doc ACKNOWLEDGEMENTS NEW_FEATURES NO_WARRANTY README CHANGES NOTES
%license AUTHORS
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
