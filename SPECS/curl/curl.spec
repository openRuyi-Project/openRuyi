# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Avoid tests marked as "flaky"
%global _test_target test-nonflaky

%bcond_with openssl

Name:           curl
Version:        8.20.0
Release:        %autorelease
Summary:        A Tool for Transferring Data from URLs
License:        curl
URL:            https://curl.se
VCS:            git:https://github.com/curl/curl
#!RemoteAsset:  sha256:63fe2dc148ba0ceae89922ef838f7e5c946272c2e78b7c59fab4b79d3ce2b896
Source0:        https://curl.se/download/curl-%{version}.tar.xz
BuildSystem:    autotools

%if %{with openssl}
BuildOption(conf):  --enable-hsts
BuildOption(conf):  --enable-ipv6
BuildOption(conf):  --with-openssl
BuildOption(conf):  --with-ca-fallback
BuildOption(conf):  --without-ca-path
BuildOption(conf):  --without-ca-bundle
BuildOption(conf):  --with-libidn2
BuildOption(conf):  --with-nghttp2
BuildOption(conf):  --enable-docs
BuildOption(conf):  --with-gssapi=$(krb5-config --prefix)
BuildOption(conf):  --with-brotli
BuildOption(conf):  --with-libssh
BuildOption(conf):  --enable-symbol-hiding
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-threaded-resolver
%else
BuildOption(conf):  --enable-hsts
BuildOption(conf):  --enable-ipv6
BuildOption(conf):  --with-gnutls
BuildOption(conf):  --with-libidn2
BuildOption(conf):  --with-nghttp2
BuildOption(conf):  --enable-docs
BuildOption(conf):  --without-libssh
BuildOption(conf):  --without-brotli
BuildOption(conf):  --without-gssapi
BuildOption(conf):  --enable-symbol-hiding
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-threaded-resolver
BuildOption(conf):  --with-ca-bundle=%{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
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
# Test requires
BuildRequires:  python3

%description
Curl is a client to get documents and files from or send documents to a
server using any of the supported protocols (HTTP, HTTPS, FTP, FTPS,
TFTP, DICT, TELNET, LDAP, or FILE). The command is designed to work
without user interaction or any kind of interactivity.

%package        devel
Summary:        Development files for the curl library
Requires:       glibc-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
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

%files devel
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
%autochangelog
