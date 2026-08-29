# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ragel
Version:        6.10
Release:        %autorelease
Summary:        Compile finite state machines from regular languages into executable code
License:        GPL-2.0-or-later
URL:            https://www.colm.net/open-source/ragel/
VCS:            git:https://github.com/adrian-thurston/ragel
#!RemoteAsset:  sha256:5f156edb65d20b856d638dd9ee2dfb43285914d9aa2b6ec779dac0270cd56c3f
Source0:        https://www.colm.net/files/ragel/ragel-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

%description
Ragel compiles executable finite state machines from regular languages.
Ragel targets C, C++, Objective-C, D, Java, Go and Ruby. Ragel state
machines can not only recognize byte sequences as regular expression
machines do, but can also execute code at arbitrary points in the
recognition of a regular language. Code embedding is done using inline
operators that do not disrupt the regular language syntax.

%conf -p
autoreconf -fiv

%files
%doc README ChangeLog AUTHORS CREDITS
%license COPYING
%{_bindir}/ragel
%{_mandir}/man1/ragel.1*

%changelog
%autochangelog
