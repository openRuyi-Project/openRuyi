# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wolfssl
Version:        5.8.2
Release:        %autorelease
Summary:        wolfSSL Embedded SSL/TLS Library
License:        GPLv3+
URL:            https://github.com/wolfSSL/wolfssl
#!RemoteAsset
Source0:        https://github.com/wolfssl/wolfssl/archive/refs/tags/v%{version}-stable.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glibc

%description
The wolfSSL library is a small, fast, portable implementation of TLS/SSL
for embedded devices to the cloud. wolfSSL supports up to TLS 1.3 and DTLS 1.3!

This package contains the shared library.

%package        devel
Summary:        Development files for the wolfSSL encryption library

%description    devel
The wolfSSL embedded SSL library (formerly CyaSSL) is a lightweight
SSL/TLS library written in ANSI C and targeted for embedded, RTOS,
and resource-constrained environments - primarily because of its small
size, speed, and feature set. It is commonly used in standard operating
environments as well because of its royalty-free pricing and excellent
cross platform support. wolfSSL supports industry standards up to the
current TLS 1.3 and DTLS 1.3, is up to 20 times smaller than OpenSSL,
and offers progressive ciphers such as ChaCha20, Curve25519, Blake2b
and Post-Quantum TLS 1.3 groups. User benchmarking and feedback reports
dramatically better performance when using wolfSSL over OpenSSL.

%prep -a
./autogen.sh

%conf
# wolfssl don't support `--disable-rpath` option
%configure \
        --enable-jni \
        --enable-memcached \
        --enable-pkcs11 \
        --disable-asm \
        --disable-crl-monitor \
        --disable-examples \
        --disable-silent-rules

%check
%make_build check
%make_build tests

%files
%{_bindir}/wolfssl-config
%{_libdir}/libwolfssl.so.44*
%license LICENSING
%doc %{_docdir}/%{name}

%files devel
%{_includedir}/wolfssl
%{_libdir}/libwolfssl.so
%{_libdir}/pkgconfig/wolfssl.pc

%changelog
%{?autochangelog}
