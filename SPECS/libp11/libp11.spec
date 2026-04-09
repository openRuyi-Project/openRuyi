# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libp11
Version:        0.4.13
Release:        %autorelease
Summary:        Library Implementing a Small Layer on Top of PKCS#11 API
License:        LGPL-2.1-or-later AND BSD-2-Clause AND OpenSSL
URL:            https://github.com/OpenSC/libp11
#!RemoteAsset
Source0:        %{url}/releases/download/libp11-%{version}/libp11-%{version}.tar.gz
#!RemoteAsset
Source1:        %{url}/releases/download/libp11-%{version}/libp11-%{version}.tar.gz.asc
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API to
make using PKCS#11 implementations easier.

The official name for PKCS#11 is "RSA Security Inc. PKCS #11
Cryptographic Token Interface (Cryptoki)".

Libp11 source code includes the official header files (version 2.20)
and thus is "derived from the RSA Security Inc. PKCS #11 Cryptographic
Token Interface (Cryptoki)".

%package        devel
Summary:        Files for developing with libp11
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(openssl)

%description    devel
This devel package contains libraries and header files for
developing applications that use libp11.

%conf -p
autoreconf -fvi

%files
%license COPYING
%doc NEWS
%{_libdir}/libp11.so.*
%{_libdir}/libpkcs11.so.*

%files devel
%doc %{_docdir}/libp11
%{_libdir}/libp11.so
%{_libdir}/libpkcs11.so
%{_libdir}/engines-3/libpkcs11.so
%{_libdir}/engines-3/pkcs11.so
%{_libdir}/pkgconfig/libp11.pc
%{_includedir}/*.h

%changelog
%autochangelog
