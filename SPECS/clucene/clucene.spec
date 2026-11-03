# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           clucene
Version:        2.3.3.4
Release:        %autorelease
Summary:        C++ full-text indexing and search library
License:        (LGPL-2.1-or-later OR Apache-2.0) AND Apache-2.0 AND BSD-3-Clause AND RSA-MD AND BSL-1.0 AND HPND-sell-variant
URL:            https://sourceforge.net/projects/clucene/
VCS:            git:https://git.code.sf.net/p/clucene/code
#!RemoteAsset:  sha256:ddfdc433dd8ad31b5c5819cc4404a8d2127472a3b720d3e744e8c51d79732eab
Source0:        https://downloads.sourceforge.net/project/clucene/clucene-core-unstable/2.3/clucene-core-%{version}.tar.gz
#!RemoteAsset:  sha256:10c7be71949bbc44ef6d8e509508887dcaf593e2f122d23ba71e339fd6faa5c7
Source1:        https://raw.githubusercontent.com/snowballstem/snowball/e76a7160ffe365f678bb082a5955df7d90d5f27f/COPYING#/COPYING.snowball
#!RemoteAsset:  sha256:c9bff75738922193e67fa726fa225535870d2aa1059f91452c411736284ad566
Source2:        https://raw.githubusercontent.com/boostorg/boost/boost-1.42.0/LICENSE_1_0.txt#/LICENSE.boost
BuildSystem:    cmake

BuildOption(prep):  -n clucene-core-%{version}
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
BuildOption(conf):  -DBUILD_CONTRIBS_LIB=ON
BuildOption(conf):  -DLUCENE_SYS_INCLUDES=%{_includedir}
# The upstream test executable is excluded from the default build target.
BuildOption(build):  --target all cl_test

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)

%patchlist
# Downstream patch for missing gmtime and strftime declarations in 2.3.3.4.
2000-include-time-declarations-in-DateTools.patch
# Downstream fix for the Linux build with distribution compiler flags.
2001-include-usleep-declaration-in-search-test.patch
# Downstream fix for tests configured before the contribs library subproject.
2002-use-contribs-headers-in-tests.patch
# Downstream fix for escaped range endpoints covered by testEscaped.
2003-copy-overlapping-quoted-range-endpoints-safely.patch
# Submitted by Vitaliy Filippov, CLucene issue 200.
# https://sourceforge.net/p/clucene/bugs/200/
2004-install-the-contribs-library-and-public-headers.patch
# C++ port of the upstream Lucene token-stream correction for LUCENE-973.
# https://github.com/apache/lucene/commit/835c405be09d20f0b174e7ce96bd675e9400c946
2005-stop-after-the-final-cjk-bigram.patch

%description
CLucene implements indexing, tokenization and querying of full-text
search indexes in C++. Its contributed analyzers support multiple
languages and text formats.

%package        devel
Summary:        Development files for CLucene
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and build metadata for C++ applications using CLucene.

%prep -a
cp -p %{SOURCE1} COPYING.snowball
cp -p %{SOURCE2} LICENSE.boost

%files
%doc README
%license APACHE.license LGPL.license COPYING COPYING.snowball LICENSE.boost
%{_libdir}/libclucene-*.so.*

%files devel
%{_includedir}/CLucene/
%{_includedir}/CLucene.h
%{_libdir}/libclucene-*.so
%{_libdir}/pkgconfig/libclucene-core.pc
%{_libdir}/CLuceneConfig.cmake/

%changelog
%autochangelog
