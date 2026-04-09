# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mokutil
Version:        0.7.2
Release:        %autorelease
Summary:        Tools for manipulating machine owner keys
License:        GPL-3.0-or-later
URL:            https://github.com/lcp/mokutil
#!RemoteAsset
Source0:        https://github.com/lcp/mokutil/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(efivar)
BuildRequires:  pkgconfig

%description
The utility to manipulate machine owner keys which are managed by shim.

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc README
%{_bindir}/mokutil
%{_datadir}/bash-completion/completions/mokutil
%{_mandir}/man1/*

%changelog
%autochangelog
