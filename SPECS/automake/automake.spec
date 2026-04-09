# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           automake
Version:        1.18.1
Release:        %autorelease
Summary:        A Program for Automatically Generating GNU-Style Makefile.in Files
License:        GFDL-1.3-or-later AND GPL-2.0-or-later AND Public-Domain AND MIT
URL:            https://www.gnu.org/software/automake
VCS:            git:https://git.savannah.gnu.org/git/automake.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/automake/automake-%{version}.tar.xz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/automake/automake-%{version}.tar.xz.sig
BuildArch:      noarch
BuildSystem:    autotools

BuildRequires:  autoconf >= 2.69
BuildRequires:  bison
BuildRequires:  perl
BuildRequires:  xz

Requires:       autoconf >= 2.69
Requires:       perl

%description
Automake is a tool for automatically generating "Makefile.in" files
from "Makefile.am" files.  "Makefile.am" is a series of "make" macro
definitions (with rules occasionally thrown in).  The generated
"Makefile.in" files are compatible with the GNU Makefile standards.

%files
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man1/*
%{_datadir}/aclocal*
%{_datadir}/automake-*

%changelog
%autochangelog
