# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           flex
Version:        2.6.4
Release:        %autorelease
Summary:        Fast Lexical Analyzer Generator
License:        BSD-3-Clause
URL:            https://github.com/westes/flex
#!RemoteAsset
Source:         https://github.com/westes/flex/releases/download/v%{version}/flex-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  m4

Requires:       m4

%description
FLEX is a tool for generating scanners: programs that recognize lexical
patterns in text.

%package        devel
Summary:        Development files for flex
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
FLEX is a tool for generating scanners: programs that recognize lexical
patterns in text.

This package contains files required to build programs with flex libraries.

%install -a
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS ONEWS README.md THANKS
%exclude %_docdir/%{name}/COPYING
%exclude %_docdir/%{name}/NEWS
%exclude %_docdir/%{name}/ONEWS
%exclude %_docdir/%{name}/README.md
%exclude %_docdir/%{name}/AUTHORS
%{_bindir}/flex
%{_bindir}/flex++
%{_mandir}/man1/*
%{_infodir}/*
%{_libdir}/libfl.so.*

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS ONEWS README.md THANKS
%{_includedir}/FlexLexer.h
%{_libdir}/libfl.so
%{_libdir}/libfl.a

%changelog
%autochangelog
