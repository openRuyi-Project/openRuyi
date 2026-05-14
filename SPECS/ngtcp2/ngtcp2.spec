# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

Name:           ngtcp2
Version:        1.16.0
Release:        %autorelease
Summary:        Implementation of RFC 9000 QUIC protocol
License:        MIT
URL:            https://github.com/ngtcp2/ngtcp2
#!RemoteAsset:  sha256:367cbcecaca539f76453c49454d8e7b38ecb162acf89cd571535ac4acf82a2b4
Source:         https://github.com/ngtcp2/ngtcp2/releases/download/v%{version}/ngtcp2-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --with-gnutls
BuildOption(conf):  --with-openssl
BuildOption(conf):  --with-libev
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-werror
%if %{without doc}
BuildOption(conf):  --disable-docs
%endif

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(openssl)
%if %{with doc}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

%description
"Call it TCP/2. One More Time."
ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

%package        devel
Summary:        The ngtcp2 development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-crypto-gnutls-devel = %{version}-%{release}
Recommends:     %{name}-crypto-ossl-devel = %{version}-%{release}

%description    devel
Development headers and libraries for the ngtcp2 QUIC protocol implementation.

%package        crypto-gnutls
Summary:        The ngtcp2 GnuTLS crypto backend
Requires:       %{name} = %{version}-%{release}

%description    crypto-gnutls
GnuTLS crypto backend for the ngtcp2 QUIC protocol implementation.

%package        crypto-gnutls-devel
Summary:        Development files for the ngtcp2 GnuTLS crypto backend
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-crypto-gnutls = %{version}-%{release}
Requires:       pkgconfig(gnutls)

%description    crypto-gnutls-devel
Development files for the GnuTLS crypto backend for ngtcp2.

%package        crypto-ossl
Summary:        The ngtcp2 OpenSSL crypto backend
Requires:       %{name} = %{version}-%{release}

%description    crypto-ossl
OpenSSL crypto backend for the ngtcp2 QUIC protocol implementation.

%package        crypto-ossl-devel
Summary:        Development files for the ngtcp2 OpenSSL crypto backend
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-crypto-ossl = %{version}-%{release}
Requires:       pkgconfig(openssl)

%description    crypto-ossl-devel
Development files for the OpenSSL crypto backend for ngtcp2.

%conf -p
autoreconf -fsi

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
%autochangelog
