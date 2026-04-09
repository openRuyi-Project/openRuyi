# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libmaxminddb
Version:        1.12.2
Release:        %autorelease
Summary:        C library for reading MaxMind DB files
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/maxmind/libmaxminddb
#!RemoteAsset
Source0:        https://github.com/maxmind/libmaxminddb/releases/download/%{version}/libmaxminddb-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
The libmaxminddb library provides a C library for reading MaxMind DB
files, including the GeoIP2 databases from MaxMind.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license LICENSE
%doc Changes.md README.md
%{_bindir}/mmdblookup
%{_libdir}/libmaxminddb.so.*
%{_mandir}/man1/mmdblookup.1*

%files devel
%{_libdir}/libmaxminddb.so
%{_libdir}/pkgconfig/libmaxminddb.pc
%{_includedir}/maxminddb.h
%{_includedir}/maxminddb_config.h
%{_mandir}/man3/libmaxminddb.3*
%{_mandir}/man3/MMDB_*.3*

%changelog
%autochangelog
