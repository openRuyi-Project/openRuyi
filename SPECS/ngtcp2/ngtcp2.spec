# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

Name:           ngtcp2
Version:        1.16.0
Release:        %autorelease
Summary:        Implementation of RFC 9000 QUIC protocol
License:        MIT
URL:            https://github.com/ngtcp2/ngtcp2
#!RemoteAsset
Source:         https://github.com/ngtcp2/ngtcp2/releases/download/v%{version}/ngtcp2-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf): --with-gnutls
BuildOption(conf): --with-openssl
BuildOption(conf): --with-libev
BuildOption(conf): --disable-static
BuildOption(conf): --enable-werror
%if %{without doc}
BuildOption(conf): --disable-docs
%endif

BuildRequires:  autoconf gcc make libtool
BuildRequires:  pkgconfig(libev)
BuildRequires:  gnutls-devel >= 3.7.5
BuildRequires:  openssl-devel >= 3.5.0
%if %{with doc}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%endif

%description
"Call it TCP/2. One More Time."
ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

%package devel
Summary:        The ngtcp2 development files
Requires:       %{name} = %{version}
Recommends:     %{name}-crypto-gnutls-devel = %{version}
Recommends:     %{name}-crypto-ossl-devel = %{version}

%description devel
Development headers and libraries for the ngtcp2 QUIC protocol implementation.

%package crypto-gnutls
Summary:        The ngtcp2 GnuTLS crypto backend
Requires:       %{name} = %{version}

%description crypto-gnutls
GnuTLS crypto backend for the ngtcp2 QUIC protocol implementation.

%package crypto-gnutls-devel
Summary:        Development files for the ngtcp2 GnuTLS crypto backend
Requires:       %{name}-devel = %{version}
Requires:       %{name}-crypto-gnutls = %{version}
Requires:       gnutls-devel >= 3.7.5

%description crypto-gnutls-devel
Development files for the GnuTLS crypto backend for ngtcp2.

%package crypto-ossl
Summary:        The ngtcp2 OpenSSL crypto backend
Requires:       %{name} = %{version}

%description crypto-ossl
OpenSSL crypto backend for the ngtcp2 QUIC protocol implementation.

%package crypto-ossl-devel
Summary:        Development files for the ngtcp2 OpenSSL crypto backend
Requires:       %{name}-devel = %{version}
Requires:       %{name}-crypto-ossl = %{version}
Requires:       openssl-devel >= 3.5.0

%description crypto-ossl-devel
Development files for the OpenSSL crypto backend for ngtcp2.

%conf -p
autoreconf -fsi

%install -a
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc AUTHORS
%doc %{_docdir}/ngtcp2
%{_libdir}/libngtcp2.so.16*

%files crypto-gnutls
%{_libdir}/libngtcp2_crypto_gnutls.so.8*

%files crypto-ossl
%{_libdir}/libngtcp2_crypto_ossl.so.0*

%files devel
%doc ChangeLog
%{_libdir}/libngtcp2.so
%{_libdir}/pkgconfig/libngtcp2.pc
%{_includedir}/ngtcp2/
%exclude %{_includedir}/ngtcp2/ngtcp2_crypto_*.h

%files crypto-gnutls-devel
%{_libdir}/libngtcp2_crypto_gnutls.so
%{_libdir}/pkgconfig/libngtcp2_crypto_gnutls.pc
%{_includedir}/ngtcp2/ngtcp2_crypto_gnutls.h

%files crypto-ossl-devel
%{_libdir}/libngtcp2_crypto_ossl.so
%{_libdir}/pkgconfig/libngtcp2_crypto_ossl.pc
%{_includedir}/ngtcp2/ngtcp2_crypto_ossl.h

%changelog
%{?autochangelog}
