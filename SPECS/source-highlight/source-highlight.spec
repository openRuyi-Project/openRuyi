# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           source-highlight
Version:        3.1.9
Release:        %autorelease
Summary:        Source Code Highlighter with Support for Many Languages
License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/src-highlite
VCS:            git:https://https.git.savannah.gnu.org/git/src-highlite.git
#!RemoteAsset:  sha256:3a7fd28378cb5416f8de2c9e77196ec915145d44e30ff4e0ee8beb3fe6211c91
Source:         https://ftpmirror.gnu.org/gnu/src-highlite/source-highlight-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --with-boost-regex=boost_regex
BuildOption(conf):  --disable-rpath --disable-static
BuildOption(build):  CXXFLAGS="%{optflags} -std=c++14"

BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  bash-completion

%description
This program, given a source file, produces a document with syntax highlighting.
Source-highlight reads source language specifications dynamically, so it can be
easily extended for handling new languages and output formats.

%package        devel
Summary:        Header files and development libraries for source-highlight
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config files, and development libraries
for the source-highlight library.

%install -a
echo -e "\ncxx = cpp.lang" >> %{buildroot}%{_datadir}/source-highlight/lang.map

# TODO: Broken check also no distro is checking it - 251
%check

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
%{_libdir}/pkgconfig/source-highlight.pc
%{_docdir}/%{name}/

%changelog
%autochangelog
