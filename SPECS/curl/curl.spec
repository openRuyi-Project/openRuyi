# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond_with openssl

Name:           curl
Version:        8.15.0
Release:        %autorelease
Summary:        A Tool for Transferring Data from URLs
License:        curl
URL:            https://curl.se
#!RemoteAsset
Source0:        https://curl.se/download/curl-%{version}.tar.xz
#!RemoteAsset
Source1:        https://curl.se/download/curl-%{version}.tar.xz.asc
#!RemoteAsset
Source2:        https://daniel.haxx.se/mykey.asc#/curl.keyring
BuildSystem:    autotools

%if %{with openssl}
BuildOption(conf): --enable-hsts --enable-ipv6 --with-openssl --with-ca-fallback --without-ca-path --without-ca-bundle --with-libidn2 --with-nghttp2 --enable-docs --with-gssapi=$(krb5-config --prefix) --with-brotli --with-libssh --enable-symbol-hiding --disable-static --enable-threaded-resolver
%else
BuildOption(conf): --enable-hsts --enable-ipv6 --with-gnutls --with-libidn2 --with-nghttp2 --enable-docs --without-libssh --without-brotli --without-gssapi --enable-symbol-hiding --disable-static --enable-threaded-resolver --with-ca-bundle=%{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
%endif

BuildRequires:  groff
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
%if %{with openssl}
BuildRequires:  pkgconfig(libssl)
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libssh)
%else
BuildRequires:  pkgconfig(gnutls)
%endif

%description
Curl is a client to get documents and files from or send documents to a
server using any of the supported protocols (HTTP, HTTPS, FTP, FTPS,
TFTP, DICT, TELNET, LDAP, or FILE). The command is designed to work
without user interaction or any kind of interactivity.

%package -n     libcurl-devel
Summary:        Development files for the curl library
Requires:       glibc-devel
Requires:       %{name} = %{version}
Provides:       curl-devel = %{version}
Obsoletes:      curl-devel < %{version}

%description -n libcurl-devel
Curl is a client to get documents and files from or send documents to a
server using any of the supported protocols (HTTP, HTTPS, FTP, GOPHER,
DICT, TELNET, LDAP, or FILE). The command is designed to work without
user interaction or any kind of interactivity.


%build -p
CPPFLAGS="-D_FORTIFY_SOURCE=2"
CFLAGS=$(echo "%{optflags}" | sed -e 's/-D_FORTIFY_SOURCE=2//')
export CPPFLAGS
export CFLAGS="$CFLAGS -fPIE"
export LDFLAGS="$LDFLAGS -Wl,-z,defs,-z,now,-z,relro -pie"
autoreconf -fiv

%install -a
rm -f %{buildroot}%{_libdir}/libcurl.la
install -Dm 0644 docs/libcurl/libcurl.m4 %{buildroot}%{_datadir}/aclocal/libcurl.m4
pushd scripts
%make_install
popd

%files
%license COPYING
%doc README RELEASE-NOTES CHANGES.md
%doc docs/{BUGS.md,FAQ,FEATURES.md,TODO,TheArtOfHttpScripting.md}
%{_bindir}/curl
%{_bindir}/wcurl
%{_mandir}/man1/curl.*
%{_mandir}/man1/wcurl.*
%{_libdir}/libcurl.so.4*

%files -n libcurl-devel
%license COPYING
%{_bindir}/curl-config
%{_includedir}/curl
%dir %{_datadir}/aclocal/
%{_datadir}/aclocal/libcurl.m4
%{_libdir}/libcurl.so
%{_libdir}/pkgconfig/libcurl.pc
%{_mandir}/man1/curl-config.*
%{_mandir}/man3/*
%doc docs/libcurl/symbols-in-versions

%changelog
%{?autochangelog}
