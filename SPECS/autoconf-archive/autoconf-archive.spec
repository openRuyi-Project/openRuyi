# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           autoconf-archive
Version:        2024.10.16
Release:        %autorelease
Summary:        A Collection of macros for GNU autoconf
License:        GPL-3.0-or-later WITH Autoconf-exception-3.0
URL:            https://www.gnu.org/software/autoconf-archive/
VCS:            git:https://git.savannah.gnu.org/git/autoconf-archive.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/autoconf-archive/autoconf-archive-%{version}.tar.xz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/autoconf-archive/autoconf-archive-%{version}.tar.xz.sig
BuildSystem:    autotools

%description
The GNU Autoconf Archive is a collection of more than 450 macros for
GNU Autoconf that have been contributed as free software by friendly
supporters of the cause from all over the Internet.

%files
%doc AUTHORS NEWS README TODO
%license COPYING*
%{_datadir}/aclocal/*.m4
%{_infodir}/autoconf-archive.info*
%{_docdir}/autoconf-archive

%changelog
%autochangelog
