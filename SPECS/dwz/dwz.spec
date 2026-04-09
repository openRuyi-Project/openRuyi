# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dwz
Version:        0.16
Release:        %autorelease
Summary:        A DWARF optimization and duplicate removal tool
License:        GPL-2.0-or-later OR GPL-3.0-or-later
URL:            https://sourceware.org/dwz/
VCS:            git:https://sourceware.org/git/dwz.git
#!RemoteAsset
Source0:        https://sourceware.org/ftp/dwz/releases/%{name}-%{version}.tar.xz
BuildSystem:    autotools

Patch0:         remove-gold-tests.patch

BuildOption(build):  prefix=%{_prefix}
BuildOption(build):  mandir=%{_mandir}
BuildOption(build):  bindir=%{_bindir}
BuildOption(build):  CFLAGS='%{build_cflags}'
BuildOption(install):  prefix=%{_prefix}
BuildOption(install):  mandir=%{_mandir}
BuildOption(install):  bindir=%{_bindir}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  dejagnu
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libelf)
# For %check
BuildRequires:  gdb

%description
The package contains a program that attempts to optimize DWARF debugging
information contained in ELF shared libraries and ELF executables for size,
by replacing DWARF information representation with equivalent smaller
representation where possible and by reducing the amount of duplication
using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information and
using DW_TAG_imported_unit to import it into each CU that needs it.

# no configure scripts.
%conf

%check -p
# Avoid failure due to dwz warn: Found compressed .debug_info section
export CC='cc -gz=none'
export CXX='g++ -gz=none'

%files
%defattr(-,root,root,-)
%license COPYING COPYING3 COPYING.RUNTIME
%{_bindir}/dwz
%{_mandir}/man1/dwz*

%changelog
%autochangelog
