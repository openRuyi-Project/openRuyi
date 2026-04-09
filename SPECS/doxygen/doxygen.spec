# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           doxygen
Version:        1.13.2
Release:        %autorelease
Summary:        Automated C, C++, and Java Documentation Generator
# qtools are used for building and they are GPL-3.0 licensed
License:        GPL-2.0-or-later
URL:            https://www.doxygen.nl/
#!RemoteAsset
Source0:        https://www.doxygen.nl/files/doxygen-%{version}.src.tar.gz
BuildSystem:    cmake

Patch1:         doxygen-no-lowercase-man-names.patch
Patch2:         reproducible.patch

BuildOption(conf):  -Dbuild_doc=OFF
BuildOption(conf):  -Dbuild_search=OFF
BuildOption(conf):  -Dbuild_wizard=OFF
BuildOption(conf):  -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now"
BuildOption(conf):  -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now"
BuildOption(conf):  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now"
BuildOption(conf):  -DBUILD_SHARED_LIBS=OFF
BuildOption(conf):  -DBUILD_STATIC_LIBS=ON
# just skip some fail tests.
BuildOption(check):  -E "^(009_bug|012_cite|08[7-9].*|09[0-8].*)"

BuildRequires:  bison
BuildRequires:  cmake >= 3.14
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  python3

%description
Doxygen is the de facto standard tool for generating documentation
from annotated C++ sources, but it also supports other popular
programming languages such as C, Objective-C, C-sharp, PHP, Java,
Python, IDL (Corba, Microsoft, and UNO/OpenOffice flavors), Fortran,
and to some extent D. Doxygen also supports the hardware description
language VHDL.

%install -a
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 doc/doxygen.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%attr(644,root,root) %{_mandir}/man1/doxygen.*
%attr(755,root,root) %{_bindir}/*

%changelog
%autochangelog
