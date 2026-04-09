# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gnutls
Version:        3.8.10
Release:        %autorelease
Summary:        A TLS protocol implementation
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://www.gnutls.org/
VCS:            git:https://gitlab.com/gnutls/gnutls
#!RemoteAsset
Source0:        https://www.gnupg.org/ftp/gcrypt/%{name}/v3.8/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-openssl-compatibility
BuildOption(conf):  --with-default-trust-store-pkcs11="pkcs11:"
BuildOption(conf):  --disable-gtk-doc

BuildRequires:  bison
BuildRequires:  cmocka-cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(libunbound)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  pkgconfig(zlib)
# trousers-devel for TPM 1.2 is optional, can be added if available
# BuildRequires:  trousers-devel
BuildRequires:  texinfo
# Tests
BuildRequires:  ca-certificates-mozilla

%description
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS
protocols. This package contains the essential shared libraries needed by
applications, as well as the command-line tools for administration.

%package        devel
Summary:        Development files for GnuTLS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libtasn1)
Requires:       pkgconfig(nettle)
Requires:       pkgconfig(p11-kit-1)

%description    devel
This package contains the header files, programming documentation, and
development libraries for GnuTLS.

%install -a
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc THANKS README.md NEWS ChangeLog AUTHORS
%doc %{_datadir}/doc/gnutls/*.png
%{_bindir}/certtool
%{_bindir}/gnutls-cli
%{_bindir}/gnutls-cli-debug
%{_bindir}/gnutls-serv
%{_bindir}/ocsptool
%{_bindir}/psktool
%{_bindir}/p11tool
%{_bindir}/danetool
%{_libdir}/libgnutls.so.30
%{_libdir}/libgnutls.so.30.*
%{_libdir}/libgnutlsxx.so.30
%{_libdir}/libgnutlsxx.so.30.*
%{_libdir}/libgnutls-dane.so.0
%{_libdir}/libgnutls-dane.so.0.*
%{_mandir}/man1/*

%files devel
%{_includedir}/gnutls/
%{_libdir}/libgnutls.so
%{_libdir}/libgnutlsxx.so
%{_libdir}/libgnutls-dane.so
%{_libdir}/pkgconfig/gnutls.pc
%{_libdir}/pkgconfig/gnutls-dane.pc
%{_mandir}/man3/*
%{_infodir}/*

%changelog
%autochangelog
