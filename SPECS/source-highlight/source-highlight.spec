# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           source-highlight
Version:        3.1.9
Release:        %autorelease
Summary:        Source Code Highlighter with Support for Many Languages
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/src-highlite
#!RemoteAsset
Source:         https://ftpmirror.gnu.org/gnu/src-highlite/source-highlight-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --with-boost-regex=boost_regex
BuildOption(conf): --disable-rpath --disable-static
BuildOption(build): CXXFLAGS="%{optflags} -std=c++14"

BuildRequires:  bison boost-devel chrpath flex gcc gcc-c++ help2man
BuildRequires:  bash-completion

%description
This program, given a source file, produces a document with syntax highlighting.
Source-highlight reads source language specifications dynamically, so it can be
easily extended for handling new languages and output formats.

%package        devel
Summary:        Header files and development libraries for source-highlight
Requires:       %{name} = %{version}

%description    devel
This package contains the header files, pkg-config files, and development libraries
for the source-highlight library.


%install -a
find %{buildroot} -type f -name "*.la" -delete -print

echo -e "\ncxx = cpp.lang" >> %{buildroot}%{_datadir}/source-highlight/lang.map

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/check-regexp
%{_bindir}/*html
%{_bindir}/source-highlight*
%{_bindir}/src-hilite-lesspipe.sh
%{_libdir}/libsource-*.so*
%{_datadir}/source-highlight/*
%{_mandir}/man1/*.gz
%{_datadir}/info/*.info.gz
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/bash_completion.d/source-highlight

%files devel
%{_includedir}/srchilite/*
%{_libdir}/pkgconfig/*
%{_docdir}/%{name}/

%changelog
%{?autochangelog}
