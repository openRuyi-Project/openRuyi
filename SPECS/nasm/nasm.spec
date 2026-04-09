# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           nasm
Version:        3.01
Release:        %autorelease
Summary:        The Netwide Assembler, a portable x86 assembler with Intel-like syntax
License:        BSD-2-Clause
URL:            https://www.nasm.us/
VCS:            git:https://github.com/netwide-assembler/nasm.git
#!RemoteAsset
Source0:        https://www.nasm.us/pub/nasm/releasebuilds/%{version}/nasm-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  perl
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(zlib)

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%files
%license LICENSE
%doc AUTHORS CHANGES README.md
%{_bindir}/nasm
%{_bindir}/ndisasm
%{_mandir}/man1/nasm*
%{_mandir}/man1/ndisasm*

%changelog
%autochangelog
