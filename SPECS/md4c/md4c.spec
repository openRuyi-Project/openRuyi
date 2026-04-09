# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           md4c
Version:        0.5.2
Release:        %autorelease
Summary:        Markdown for C
License:        MIT
URL:            https://github.com/mity/md4c
#!RemoteAsset
Source0:        https://github.com/mity/md4c/archive/refs/tags/release-%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  python3

%description
MD4C is Markdown parser implementation in C.
This package contains the shared libraries and the md2html utility.

%package        devel
Summary:        Development files for md4c
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The md4c-devel package contains libraries and header files for
developing applications that use md4c.

%check
cd %{__cmake_builddir}
../scripts/run-tests.sh

%files
%doc README.md CHANGELOG.md
%license LICENSE.md
%{_bindir}/md2html
%{_libdir}/libmd4c.so.0*
%{_libdir}/libmd4c-html.so.0*
%{_mandir}/man1/md2html.1*

%files devel
%{_includedir}/md4c.h
%{_includedir}/md4c-html.h
%{_libdir}/libmd4c.so
%{_libdir}/libmd4c-html.so
%{_libdir}/cmake/md4c/
%{_libdir}/pkgconfig/md4c.pc
%{_libdir}/pkgconfig/md4c-html.pc

%changelog
%autochangelog
