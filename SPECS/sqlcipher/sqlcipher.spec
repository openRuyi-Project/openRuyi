# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target fuzztest

Name:           sqlcipher
Version:        4.6.1
Release:        %autorelease
Summary:        SQLite extension that provides 256-bit AES encryption
License:        BSD-3-Clause
URL:            https://github.com/sqlcipher/sqlcipher
#!RemoteAsset:  sha256:d8f9afcbc2f4b55e316ca4ada4425daf3d0b4aab25f45e11a802ae422b9f53a3
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(zlib)

BuildOption(conf):  --enable-tempstore
BuildOption(conf):  --enable-releasemode
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-tcl
BuildOption(conf):  --enable-fts3
BuildOption(conf):  --enable-fts4
BuildOption(conf):  --enable-fts5
BuildOption(conf):  --enable-rtree

%description
SQLCipher is a standalone fork of the SQLite database library that adds
256-bit AES encryption of database files and other security features.

%package        devel
Summary:        Development files for SQLCipher
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for developing applications that use SQLCipher.

%files
%license LICENSE.md
%{_bindir}/sqlcipher
%{_libdir}/libsqlcipher*.so.*

%files devel
%{_includedir}/sqlcipher/
%{_libdir}/libsqlcipher.so
%{_libdir}/pkgconfig/sqlcipher.pc

%changelog
%autochangelog
