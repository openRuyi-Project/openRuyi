# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rdfind
Version:        1.7.0
Release:        %autorelease
Summary:        Find duplicate files utility
License:        GPL-2.0-or-later
URL:            https://rdfind.pauldreik.se/
VCS:            git:https://github.com/pauldreik/rdfind
#!RemoteAsset:  sha256:bd17dbd9c6c9fc0c0b016b3e77ecf5cd718eee428172c767f429ba30405816d8
Source0:        https://github.com/pauldreik/rdfind/archive/refs/tags/releases/%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  m4
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(nettle)

%description
Rdfind is a program that finds duplicate files. It is useful for compressing
backup directories or just finding duplicate files. It compares files based on
their content, NOT on their file names.

%conf -p
autoreconf -vif

%files
%license COPYING LICENSE
%doc AUTHORS ChangeLog
%{_bindir}/rdfind
%{_mandir}/man1/rdfind.1*

%changelog
%autochangelog
