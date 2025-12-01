# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libressl
Version:        4.2.0
Release:        %autorelease
Summary:        An SSL/TLS protocol implementation
License:        OpenSSL
URL:            https://www.libressl.org/
#!RemoteAsset
Source:         https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --enable-libtls
BuildOption(conf): --with-openssldir=%{_sysconfdir}/libressl
BuildOption(conf): --disable-static

BuildRequires:  automake autoconf libtool fdupes pkg-config

%description
LibreSSL is an implementation of the Secure Sockets Layer (SSL) and
Transport Layer Security (TLS) protocols, forked from OpenSSL.
This package contains the command-line tool and configuration.

%package -n     libcrypto56
Summary:        LibreSSL cryptographic library

%description -n libcrypto56
This package provides the 'crypto' library from LibreSSL, which implements a
wide range of cryptographic algorithms.

%package -n     libssl59
Summary:        LibreSSL SSL/TLS library

%description -n libssl59
This package provides the 'ssl' library from LibreSSL for the Secure Sockets
Layer (SSL) and Transport Layer Security (TLS) protocols.

%package -n     libtls32
Summary:        A simplified interface for the LibreSSL TLS protocol

%description -n libtls32
This package provides the 'tls' library from LibreSSL, offering a modern and
simplified interface for secure client and server communications.

%package        devel
Summary:        Development files for LibreSSL
Requires:       libcrypto56 = %{version}
Requires:       libssl59 = %{version}
Requires:       libtls32 = %{version}

%description devel
This package contains the header files, pkg-config files, and API documentation
needed to develop applications that use LibreSSL.

%conf -p
autoreconf -fiv

%install -a

for i in %{buildroot}%{_mandir}/man*; do
      cd "$i"
      for j in *.*; do
              if [ -L "$j" ]; then
                      target=$(readlink "$j")
                      ln -fs "${target}ssl" "$j"
              fi
              mv "$j" "${j}ssl"
      done
      cd - >/dev/null
done
rm -v "%{buildroot}%{_sysconfdir}/libressl/cert.pem"

%files
%license COPYING
%dir %{_sysconfdir}/libressl/
%config(noreplace) %{_sysconfdir}/libressl/openssl.cnf
%config(noreplace) %{_sysconfdir}/libressl/x509v3.cnf
%{_bindir}/ocspcheck
%{_bindir}/openssl
%{_mandir}/man1/*.1ssl*
%{_mandir}/man5/*.5ssl*
%{_mandir}/man8/*.8ssl*

%files -n libcrypto56
%{_libdir}/libcrypto.so.*

%files -n libssl59
%{_libdir}/libssl.so.*

%files -n libtls32
%{_libdir}/libtls.so.*

%files devel
%{_includedir}/openssl/
%{_includedir}/tls.h
%{_libdir}/libcrypto.so
%{_libdir}/libssl.so
%{_libdir}/libtls.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3ssl*

%changelog
%{?autochangelog}
