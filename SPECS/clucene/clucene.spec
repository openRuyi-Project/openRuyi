# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           clucene
Version:        2.3.3.4
Release:        %autorelease
Summary:        C++ full-text indexing and search library
License:        (LGPL-2.1-or-later OR Apache-2.0) AND Apache-2.0 AND BSD-3-Clause AND RSA-MD AND HPND-sell-variant
URL:            https://sourceforge.net/projects/clucene/
VCS:            git:https://git.code.sf.net/p/clucene/code
#!RemoteAsset:  sha256:ddfdc433dd8ad31b5c5819cc4404a8d2127472a3b720d3e744e8c51d79732eab
Source0:        https://downloads.sourceforge.net/project/clucene/clucene-core-unstable/2.3/clucene-core-%{version}.tar.gz
BuildSystem:    cmake

# Downstream patch for missing gmtime and strftime declarations in 2.3.3.4.
Patch2000:      2000-include-time-declarations-in-DateTools.patch
# Submitted by Vitaliy Filippov, CLucene issue 200.
# https://sourceforge.net/p/clucene/bugs/200/
Patch2001:      2001-install-the-contribs-library-and-public-headers.patch

BuildOption(prep):  -n clucene-core-%{version}
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
BuildOption(conf):  -DBUILD_CONTRIBS_LIB=ON
BuildOption(conf):  -DLUCENE_SYS_INCLUDES=%{_includedir}
# Skip SimpleTest because cl_test lacks POSIX sleep declarations and contribs include paths.
BuildOption(check):  --exclude-regex '^SimpleTest$'

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)

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
rm -rf src/ext/{boost,zlib}

%files
%doc README
%license APACHE.license LGPL.license COPYING
%{_libdir}/libclucene-*.so.*

%files devel
%{_includedir}/CLucene/
%{_includedir}/CLucene.h
%{_libdir}/libclucene-*.so
%{_libdir}/pkgconfig/libclucene-core.pc
%{_libdir}/CLuceneConfig.cmake/

%changelog
%autochangelog
