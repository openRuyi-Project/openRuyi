# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdmtx
Version:        0.7.8
Release:        %autorelease
Summary:        Library for working with Data Matrix 2D bar-codes
License:        BSD-2-Clause-Views
URL:            https://github.com/dmtx/libdmtx
#!RemoteAsset:  sha256:2394bf1d1d693a5a4ca3cfcc1bb28a4d878bdb831ea9ca8f3d5c995d274bdc39
Source0:        https://github.com/dmtx/libdmtx/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake

%description
libdmtx is open source software for reading and writing Data Matrix 2D
bar-codes. This package contains the shared library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
./autogen.sh

%files
%license LICENSE
%doc AUTHORS ChangeLog KNOWNBUG README README.linux TODO
%{_libdir}/libdmtx.so.0*

%files devel
%{_includedir}/*
%{_libdir}/libdmtx.so
%{_libdir}/pkgconfig/libdmtx.pc
%{_mandir}/man3/libdmtx.3*

%changelog
%autochangelog
