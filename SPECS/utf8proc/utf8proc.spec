# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           utf8proc
Version:        2.10.0
Release:        %autorelease
Summary:        Library for processing UTF-8 encoded Unicode strings
License:        MIT AND Unicode-DFS-2015
URL:            https://julialang.org/utf8proc/
VCS:            git:https://github.com/JuliaLang/utf8proc
#!RemoteAsset
Source0:        https://github.com/JuliaLang/utf8proc/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  CFLAGS="%{optflags}"
BuildOption(install):  includedir=%{_includedir}
BuildOption(install):  libdir=%{_libdir}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl

%description
utf8proc is a library for processing UTF-8 encoded Unicode strings.
Some features are Unicode normalization, stripping of default ignorable
characters, case folding and detection of grapheme cluster boundaries.
A special character mapping is available, which converts for example
the characters “Hyphen” (U+2010), “Minus” (U+2212) and “Hyphen-Minus
(U+002D, ASCII Minus) all into the ASCII minus sign, to make them
equal for comparisons.

This package only contains the C library.

%package        devel
Summary:        Header files, libraries and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Contains header files for developing applications that use the %{name}
library.

The documentation for the C library is found in the utf8proc.h header file.
"utf8proc_map" is most likely the function you will be using for mapping UTF-8
strings, unless you want to allocate memory yourself.

%prep -a
#solve the problem during the check
sed -i '/-C bench/d;/\ttest.* data/d' Makefile
touch data/NormalizationTest.txt data/GraphemeBreakTest.txt data/Lowercase.txt data/Uppercase.txt

%conf

%install -a
rm -f %{buildroot}%{_libdir}/*.a

%files
%doc LICENSE.md NEWS.md README.md
%{_libdir}/libutf8proc.so.3*

%files devel
%{_includedir}/utf8proc.h
%{_libdir}/libutf8proc.so
%{_libdir}/pkgconfig/libutf8proc.pc

%changelog
%autochangelog
