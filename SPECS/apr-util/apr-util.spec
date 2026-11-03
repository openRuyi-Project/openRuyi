# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond ldap 1
%bcond openssl 1
%bcond sqlite 1
%bcond odbc 1
%bcond nss 0

Name:           apr-util
Version:        1.6.6
Release:        %autorelease
Summary:        Apache Portable Runtime Utility library
License:        Apache-2.0 AND (Beerware AND LicenseRef-openRuyi-Public-Domain AND OLDAP-2.7 AND BSD-4.3RENO)
URL:            https://apr.apache.org/
VCS:            git:https://github.com/apache/apr-util
#!RemoteAsset:  sha256:aa77dd25f036731b7246abbfbebe6cc813b42799b62c874bc82bd4e1f90f2918
Source:         https://archive.apache.org/dist/apr/apr-util-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --with-apr=%{_prefix}
BuildOption(conf):  --includedir=%{_includedir}/apr-1
%if %{with ldap}
BuildOption(conf):  --with-ldap
%else
BuildOption(conf):  --without-ldap
%endif
BuildOption(conf):  --without-gdbm
%if %{with sqlite}
BuildOption(conf):  --with-sqlite3
%else
BuildOption(conf):  --without-sqlite3
%endif
%if %{with odbc}
BuildOption(conf):  --with-odbc
%else
BuildOption(conf):  --without-odbc
%endif
BuildOption(conf):  --without-sqlite2
%if %{with openssl} || %{with nss}
BuildOption(conf):  --with-crypto
%else
BuildOption(conf):  --without-crypto
%endif
%if %{with openssl}
BuildOption(conf):  --with-openssl
%else
BuildOption(conf):  --without-openssl
%endif
%if %{with nss}
BuildOption(conf):  --with-nss
%else
BuildOption(conf):  --without-nss
%endif
# The tests might fail under multi jobs.
BuildOption(check):  -j1

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  pkgconfig(apr-1)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libxcrypt)

%if %{with ldap}
BuildRequires:  pkgconfig(ldap)
%endif
%if %{with openssl}
BuildRequires:  pkgconfig(openssl)
%endif
%if %{with nss}
BuildRequires:  pkgconfig(nss)
%endif
%if %{with sqlite}
BuildRequires:  pkgconfig(sqlite3)
%endif
%if %{with odbc}
BuildRequires:  pkgconfig(odbc)
%endif

%description
The Apache Portable Runtime (APR) utility library provides support for XML,
LDAP, database interfaces, URI parsing, and more.

%package        devel
Summary:        APR utility library development kit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(apr-1)
%if %{with ldap}
Requires:       pkgconfig(ldap)
%endif
Requires:       pkgconfig(expat)

%description    devel
This package provides the support files for building applications that use
the APR utility library.

%if %{with sqlite}
%package        sqlite
Summary:        APR utility library SQLite DBD driver
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    sqlite
This package provides the SQLite driver for the apr-util DBD interface.
%endif

%if %{with odbc}
%package        odbc
Summary:        APR utility library ODBC DBD driver
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    odbc
This package provides the ODBC driver for the apr-util DBD interface.
%endif

%if %{with ldap}
%package        ldap
Summary:        APR utility library LDAP support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    ldap
This package provides LDAP support for apr-util.
%endif

%if %{with openssl}
%package        openssl
Summary:        APR utility library OpenSSL crypto support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    openssl
This package provides OpenSSL crypto support for apr-util.
%endif

%if %{with nss}
%package        nss
Summary:        APR utility library NSS crypto support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    nss
This package provides NSS crypto support for apr-util.
%endif

%install -a
install -D -m 644 build/find_apu.m4 %{buildroot}%{_datadir}/aclocal/find_apu.m4
rm -f %{buildroot}%{_libdir}/libapr*.a
rm -f %{buildroot}%{_libdir}/apr-util-1/*.*a

%files
%doc CHANGES
%license LICENSE NOTICE
%{_libdir}/libaprutil-1.so.*
%dir %{_libdir}/apr-util-1

%if %{with sqlite}
%files sqlite
%{_libdir}/apr-util-1/apr_dbd_sqlite*
%endif

%if %{with odbc}
%files odbc
%{_libdir}/apr-util-1/apr_dbd_odbc*
%endif

%if %{with ldap}
%files ldap
%{_libdir}/apr-util-1/apr_ldap*
%endif

%if %{with openssl}
%files openssl
%{_libdir}/apr-util-1/apr_crypto_openssl*
%endif

%if %{with nss}
%files nss
%{_libdir}/apr-util-1/apr_crypto_nss*
%endif

%files devel
%{_bindir}/apu-1-config
%{_libdir}/libaprutil-1.so
%{_libdir}/aprutil.exp
%{_includedir}/apr-1/*.h
%{_libdir}/pkgconfig/apr-util-1.pc
%{_datadir}/aclocal/*.m4

%changelog
%autochangelog
