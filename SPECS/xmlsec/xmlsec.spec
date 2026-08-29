# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xmlsec
Version:        1.3.10
Release:        %autorelease
Summary:        Library providing support for "XML Signature" and "XML Encryption" standards
License:        MIT
URL:            https://www.aleksey.com/xmlsec
VCS:            git:https://github.com/lsh123/xmlsec
#!RemoteAsset:  sha256:5915590780566dae4b5d13d51a42fc0e34b30b26fda6f2c5f744ec31b363ee1a
Source:         https://github.com/lsh123/xmlsec/releases/download/%{version}/xmlsec1-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.13
BuildRequires:  pkgconfig(libxslt) >= 1.1.35
BuildRequires:  pkgconfig(openssl) >= 3.0.13
BuildRequires:  pkgconfig(nss) >= 3.91
BuildRequires:  pkgconfig(nspr) >= 4.34.1
BuildRequires:  pkgconfig(gnutls) >= 3.8.3
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel

%description
XML Security Library is a C library based on LibXML2 and OpenSSL.
The library was created with a goal to support major XML security
standards "XML Digital Signature" and "XML Encryption".

%package        devel
Summary:        Libraries, includes, etc. to develop applications with XML Digital Signatures and XML Encryption support
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel%{?_isa} >= 1.0.0

%description    devel
Libraries, includes, etc. you can use to develop applications with XML Digital
Signatures and XML Encryption support.

%package        openssl
Summary:        OpenSSL crypto plugin for XML Security Library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    openssl
OpenSSL plugin for XML Security Library provides OpenSSL based crypto services
for the xmlsec library.

%package        openssl-devel
Summary:        OpenSSL crypto plugin for XML Security Library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-openssl%{?_isa} = %{version}-%{release}

%description    openssl-devel
Libraries, includes, etc. for developing XML Security applications with OpenSSL.

%package        gnutls
Summary:        GNUTls crypto plugin for XML Security Library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gnutls
GNUTls plugin for XML Security Library provides GNUTls based crypto services
for the xmlsec library.

%package        gnutls-devel
Summary:        GNUTls crypto plugin for XML Security Library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-openssl-devel%{?_isa} = %{version}-%{release}
Requires:       gnutls-devel%{?_isa} >= 1.0.20

%description    gnutls-devel
Libraries, includes, etc. for developing XML Security applications with GNUTls.

%package        nss
Summary:        NSS crypto plugin for XML Security Library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    nss
NSS plugin for XML Security Library provides NSS based crypto services
for the xmlsec library

%package        nss-devel
Summary:        NSS crypto plugin for XML Security Library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-nss%{?_isa} = %{version}-%{release}

%description    nss-devel
Libraries, includes, etc. for developing XML Security applications with NSS.

%conf -p
autoreconf -vfi

%install -a
# move installed docs to include them in -devel package via %%doc magic
rm -rf __tmp_doc ; mkdir __tmp_doc
mv %{buildroot}%{_docdir}/xmlsec/* __tmp_doc

# No tests.
%check

%files
%license Copyright
%doc AUTHORS ChangeLog NEWS README.md
%{_bindir}/xmlsec1
%{_libdir}/libxmlsec1.so.*
%{_mandir}/man1/xmlsec1.1*

%files devel
%doc HACKING __tmp_doc/*
%{_bindir}/xmlsec1-config
%dir %{_includedir}/xmlsec1
%dir %{_includedir}/xmlsec1/xmlsec
%{_includedir}/xmlsec1/xmlsec/*.h
%{_libdir}/libxmlsec1.so
%{_libdir}/pkgconfig/xmlsec1.pc
%{_libdir}/xmlsec1Conf.sh
%{_datadir}/aclocal/xmlsec1.m4
%{_mandir}/man1/xmlsec1-config.1*

%files openssl
%{_libdir}/libxmlsec1-openssl.so.*
%{_libdir}/libxmlsec1-openssl.so

%files openssl-devel
%{_includedir}/xmlsec1/xmlsec/openssl/
%{_libdir}/pkgconfig/xmlsec1-openssl.pc

%files gnutls
%{_libdir}/libxmlsec1-gnutls.so.*
%{_libdir}/libxmlsec1-gnutls.so

%files gnutls-devel
%{_includedir}/xmlsec1/xmlsec/gnutls/
%{_libdir}/pkgconfig/xmlsec1-gnutls.pc

%files nss
%{_libdir}/libxmlsec1-nss.so.*
%{_libdir}/libxmlsec1-nss.so

%files nss-devel
%{_includedir}/xmlsec1/xmlsec/nss/
%{_libdir}/pkgconfig/xmlsec1-nss.pc

%changelog
%autochangelog
