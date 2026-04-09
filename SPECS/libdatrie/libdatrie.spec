# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdatrie
Version:        0.2.13
Release:        %autorelease
Summary:        Implementation of Double-Array structure for representing trie
License:        LGPL-2.1-or-later
URL:            https://linux.thai.net/~thep/datrie/datrie.html
VCS:            git:https://github.com/tlwg/libdatrie
#!RemoteAsset
Source0:        http://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-html-docdir=%{_docdir}/%{name}-devel

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  autoconf-archive
BuildRequires:  doxygen

%description
datrie is an implementation of double-array structure for representing trie.

Trie is a kind of digital search tree, an efficient indexing method with O(1)
time complexity for searching. Comparably as efficient as hashing, trie also
provides flexibility on incremental matching and key spelling manipulation.
This makes it ideal for lexical analyzers, as well as spelling dictionaries.

Details of the implementation: http://linux.thai.net/~thep/datrie/datrie.html

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoconf -fiv

%files
%license COPYING
%{_libdir}/libdatrie.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README*
%{_includedir}/datrie/
%{_libdir}/libdatrie.so
%{_libdir}/pkgconfig/datrie-0.2.pc
%{_bindir}/trietool*
%{_mandir}/man1/trietool*
%{_docdir}/%{name}-devel/*.{html,css,png,js,svg}

%changelog
%autochangelog
