# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           less
Version:        702
Release:        %autorelease
Summary:        Text File Browser and Pager Similar to more
License:        BSD-2-Clause OR GPL-3.0-or-later
URL:            https://www.greenwoodsoftware.com/less/
VCS:            git:https://github.com/gwsw/less
#!RemoteAsset:  sha256:242a64c00f02d96f8ee208cf638ae1728b727c7f5fdf82a7d4f4cae32fb084e2
Source0:        https://ftpmirror.gnu.org/gnu/less/less-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(check):  LIBS="-lncurses -ltinfo"

BuildRequires:  automake
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig

%description
less is a text file browser and pager similar to more. It allows
backward as well as forward movement within a file. Also, less does not
have to read the entire input file before starting. It is possible to
start an editor at any time from within less.

%files
%license LICENSE COPYING
%doc NEWS
%{_mandir}/*/*
%{_bindir}/less
%{_bindir}/lesskey
%{_libexecdir}/lessecho
%{_libexecdir}/less-osc8-open

%changelog
%autochangelog
