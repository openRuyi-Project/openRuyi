# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define webroot /var/www/lighttpd

%bcond pcre 0
%bcond dbi 0
%bcond mysql 0
%bcond pgsql 0
%bcond mbedtls 0
%bcond nss 0

Name:           lighttpd
Version:        1.4.82
Release:        %autorelease
Summary:        Lightning fast webserver with light system requirements
License:        BSD-3-Clause
URL:            http://www.lighttpd.net/
VCS:            git:https://git.lighttpd.net/lighttpd/lighttpd1.4.git
#!RemoteAsset
Source0:        http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-%{version}.tar.xz
Source1:        lighttpd.logrotate
Source2:        php.d-lighttpd.ini
Source3:        lighttpd.sysusers
Source4:        lighttpd.tmpfiles
BuildSystem:    autotools

BuildOption(conf):  --libdir='%{_libdir}/lighttpd'
BuildOption(conf):  --with-krb5
BuildOption(conf):  --with-ldap
BuildOption(conf):  --with-pam
BuildOption(conf):  --with-sasl
BuildOption(conf):  --with-gnutls
BuildOption(conf):  --with-pcre2
BuildOption(conf):  --with-nettle
BuildOption(conf):  --with-attr
BuildOption(conf):  --with-openssl
BuildOption(conf):  --with-webdav-props
BuildOption(conf):  --with-webdav-locks
BuildOption(conf):  --with-lua=lua
BuildOption(conf):  --with-zlib
BuildOption(conf):  --with-zstd
BuildOption(conf):  --with-bzip2
BuildOption(conf):  --with-brotli
BuildOption(conf):  --with-maxminddb
BuildOption(conf):  --with-unwind
%if %{with mysql}
BuildOption(conf):  --with-mysql
%else
BuildOption(conf):  --without-mysql
%endif
%if %{with pcre}
BuildOption(conf):  --with-pcre
%else
BuildOption(conf):  --without-pcre
%endif
%if %{with pgsql}
BuildOption(conf):  --with-pgsql
%else
BuildOption(conf):  --without-pgsql
%endif
%if %{with dbi}
BuildOption(conf):  --with-dbi
%else
BuildOption(conf):  --without-dbi
%endif
%if %{with mbedtls}
BuildOption(conf):  --with-mbedtls
%else
BuildOption(conf):  --without-mbedtls
%endif
%if %{with nss}
BuildOption(conf):  --with-nss
%else
BuildOption(conf):  --without-nss
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
%if %{with pcre}
BuildRequires:  pkgconfig(libpcre)
%endif
%if %{with mbedtls}
BuildRequires:  mbedtls-devel
%endif
%if %{with nss}
BuildRequires:  pkgconfig(nss)
%endif
%if %{with mysql}
BuildRequires:  mariadb-connector-c-devel
%endif
%if %{with pgsql}
BuildRequires:  libpq-devel
%endif
%if %{with dbi}
BuildRequires:  libdbi-devel
%endif

Requires:       system-logos
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       %{name}-mod_deflate = %{version}-%{release}
Requires:       %{name}-mod_webdav = %{version}-%{release}
Requires:       %{name}-mod_magnet = %{version}-%{release}
Requires:       %{name}-mod_openssl = %{version}-%{release}

%description
lighttpd is a secure, fast, compliant, and very flexible web server that has
been optimized for high-performance environments.

%package        fastcgi
Summary:        FastCGI module and spawning helper for lighttpd
Requires:       %{name} = %{version}-%{release}

%description    fastcgi
This package contains the spawn-fcgi helper and configuration for FastCGI.

%if %{with dbi}
%package        mod_authn_dbi
Summary:        Authentication module for lighttpd that uses DBI
Requires:       %{name} = %{version}-%{release}

%description    mod_authn_dbi
Authentication module for lighttpd that uses DBI.
%endif

%package        mod_authn_gssapi
Summary:        Authentication module for lighttpd that uses GSSAPI
Requires:       %{name} = %{version}-%{release}

%description    mod_authn_gssapi
Authentication module for lighttpd that uses GSSAPI.

%package        mod_authn_ldap
Summary:        Authentication module for lighttpd that uses LDAP
Requires:       %{name} = %{version}-%{release}

%description    mod_authn_ldap
Authentication module for lighttpd that uses LDAP.

%package        mod_authn_pam
Summary:        Authentication module for lighttpd that uses PAM
Requires:       %{name} = %{version}-%{release}

%description    mod_authn_pam
Authentication module for lighttpd that uses PAM.

%package        mod_authn_sasl
Summary:        Authentication module for lighttpd that uses SASL
Requires:       %{name} = %{version}-%{release}

%description    mod_authn_sasl
Authentication module for lighttpd that uses SASL.

%package        mod_deflate
Summary:        Compression module for lighttpd
Requires:       %{name} = %{version}-%{release}

%description    mod_deflate
Compression module for lighttpd.

%package        mod_gnutls
Summary:        TLS module for lighttpd that uses GnuTLS
Requires:       %{name} = %{version}-%{release}

%description    mod_gnutls
TLS module for lighttpd that uses GnuTLS.

%package        mod_magnet
Summary:        Lua module for lighttpd
Requires:       %{name} = %{version}-%{release}

%description    mod_magnet
Lua module for lighttpd.

%package        mod_maxminddb
Summary:        GeoIP2 module for lighttpd
Requires:       %{name} = %{version}-%{release}

%description    mod_maxminddb
GeoIP2 module for lighttpd to use for location lookups.

%if %{with mbedtls}
%package        mod_mbedtls
Summary:        TLS module for lighttpd that uses mbedTLS
Requires:       %{name} = %{version}-%{release}

%description    mod_mbedtls
TLS module for lighttpd that uses mbedTLS.
%endif

%if %{with nss}
%package        mod_nss
Summary:        TLS module for lighttpd that uses NSS
Requires:       %{name} = %{version}-%{release}

%description    mod_nss
TLS module for lighttpd that uses NSS.
%endif

%package        mod_openssl
Summary:        TLS module for lighttpd that uses OpenSSL
Requires:       %{name} = %{version}-%{release}

%description    mod_openssl
TLS module for lighttpd that uses OpenSSL.

%if %{with dbi}
%package        mod_vhostdb_dbi
Summary:        Virtual host module for lighttpd that uses DBI
Requires:       %{name} = %{version}-%{release}

%description    mod_vhostdb_dbi
Virtual host module for lighttpd that uses DBI.
%endif

%package        mod_vhostdb_ldap
Summary:        Virtual host module for lighttpd that uses LDAP
Requires:       %{name} = %{version}-%{release}

%description    mod_vhostdb_ldap
Virtual host module for lighttpd that uses LDAP.

%if %{with mysql}
%package        mod_vhostdb_mysql
Summary:        Virtual host module for lighttpd that uses MySQL
Requires:       %{name} = %{version}-%{release}

%description    mod_vhostdb_mysql
Virtual host module for lighttpd that uses MySQL.
%endif

%if %{with pgsql}
%package        mod_vhostdb_pgsql
Summary:        Virtual host module for lighttpd that uses PostgreSQL
Requires:       %{name} = %{version}-%{release}

%description    mod_vhostdb_pgsql
Virtual host module for lighttpd that uses PostgreSQL.
%endif

%package        mod_webdav
Summary:        WebDAV module for lighttpd
Requires:       %{name} = %{version}-%{release}

%description    mod_webdav
WebDAV module for lighttpd.

%package        filesystem
Summary:        The basic directory layout for lighttpd

%description    filesystem
The lighttpd-filesystem package contains the basic directory layout
for the lighttpd server.

%conf -p
autoreconf -fiv

%install -a

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/lighttpd
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/php.d/lighttpd.ini
install -D -p -m 0644 doc/systemd/lighttpd.service %{buildroot}%{_unitdir}/lighttpd.service

# Install default web page
mkdir -p %{buildroot}%{webroot}

# Config examples
rm -rf config
cp -a doc/config config
find config -name 'Makefile*' | xargs rm -f
chmod -x doc/scripts/*.sh

# Install sample config files
mkdir -p %{buildroot}%{_sysconfdir}/lighttpd
cp -a config/*.conf config/*.d %{buildroot}%{_sysconfdir}/lighttpd/

# Modules load config
mkdir -p %{buildroot}/usr/lib/modules-load.d
echo tls > %{buildroot}/usr/lib/modules-load.d/lighttpd-mod_gnutls.conf
echo tls > %{buildroot}/usr/lib/modules-load.d/lighttpd-mod_openssl.conf

# Create directories
mkdir -p %{buildroot}%{_var}/log/lighttpd
mkdir -p %{buildroot}%{_var}/run/lighttpd
mkdir -p %{buildroot}%{_var}/lib/lighttpd/

install -m0644 -D %{SOURCE3} %{buildroot}%{_sysusersdir}/lighttpd.conf

mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m0644 -D %{SOURCE4} %{buildroot}/usr/lib/tmpfiles.d/lighttpd.conf

%pre
%sysusers_create_package %{name} %{SOURCE3}

%post
%systemd_post lighttpd.service

%preun
%systemd_preun lighttpd.service

%postun
%systemd_postun_with_restart lighttpd.service

%files
%license COPYING
%doc AUTHORS README
%config(noreplace) %{_sysconfdir}/lighttpd/*.conf
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/*.conf
%exclude %{_sysconfdir}/lighttpd/conf.d/deflate.conf
%exclude %{_sysconfdir}/lighttpd/conf.d/fastcgi.conf
%exclude %{_sysconfdir}/lighttpd/conf.d/magnet.conf
%exclude %{_sysconfdir}/lighttpd/conf.d/webdav.conf
%config %{_sysconfdir}/lighttpd/conf.d/mod.template
%config %{_sysconfdir}/lighttpd/vhosts.d/vhosts.template
%config(noreplace) %{_sysconfdir}/logrotate.d/lighttpd
%{_unitdir}/lighttpd.service
%{_tmpfilesdir}/lighttpd.conf
%{_sbindir}/lighttpd
%{_sbindir}/lighttpd-angel
%{_libdir}/lighttpd/

%exclude %{_libdir}/lighttpd/mod_webdav.so
%{_mandir}/man8/lighttpd*8*

%files fastcgi
%config(noreplace) %{_sysconfdir}/php.d/lighttpd.ini
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/fastcgi.conf

%if %{with dbi}
%files mod_authn_dbi
%{_libdir}/lighttpd/mod_authn_dbi.so
%endif

%files mod_authn_gssapi
%{_libdir}/lighttpd/mod_authn_gssapi.so

%files mod_authn_ldap
%{_libdir}/lighttpd/mod_authn_ldap.so

%files mod_authn_pam
%{_libdir}/lighttpd/mod_authn_pam.so

%files mod_authn_sasl
%{_libdir}/lighttpd/mod_authn_sasl.so

%files mod_deflate
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/deflate.conf
%{_libdir}/lighttpd/mod_deflate.so

%files mod_gnutls
%{_prefix}/lib/modules-load.d/lighttpd-mod_gnutls.conf
%{_libdir}/lighttpd/mod_gnutls.so

%files mod_magnet
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/magnet.conf
%{_libdir}/lighttpd/mod_magnet.so

%files mod_maxminddb
%{_libdir}/lighttpd/mod_maxminddb.so

%if %{with mbedtls}
%files mod_mbedtls
%{_libdir}/lighttpd/mod_mbedtls.so
%endif

%if %{with nss}
%files mod_nss
%{_libdir}/lighttpd/mod_nss.so
%endif

%files mod_openssl
%{_prefix}/lib/modules-load.d/lighttpd-mod_openssl.conf
%{_libdir}/lighttpd/mod_openssl.so

%if %{with dbi}
%files mod_vhostdb_dbi
%{_libdir}/lighttpd/mod_vhostdb_dbi.so
%endif

%files mod_vhostdb_ldap
%{_libdir}/lighttpd/mod_vhostdb_ldap.so

%if %{with mysql}
%files mod_vhostdb_mysql
%{_libdir}/lighttpd/mod_vhostdb_mysql.so
%endif

%if %{with pgsql}
%files mod_vhostdb_pgsql
%{_libdir}/lighttpd/mod_vhostdb_pgsql.so
%endif

%files mod_webdav
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/webdav.conf
%{_libdir}/lighttpd/mod_webdav.so

%files filesystem
%dir %{_sysconfdir}/lighttpd/
%dir %{_sysconfdir}/lighttpd/conf.d/
%dir %{_sysconfdir}/lighttpd/vhosts.d/
%ghost %attr(0750, lighttpd, lighttpd) %{_var}/run/lighttpd/
%attr(0750, lighttpd, lighttpd) %{_var}/lib/lighttpd/
%attr(0750, lighttpd, lighttpd) %{_var}/log/lighttpd/
%attr(0700, lighttpd, lighttpd) %dir %{webroot}/
%{_sysusersdir}/lighttpd.conf

%changelog
%{?autochangelog}
