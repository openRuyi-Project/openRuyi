# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Change to 1 to enable
# elasticsearch on riscv64 when?
%bcond elasticsearch 0
%bcond mysql 0
%bcond pgsql 0
%bcond gssapi 1
%bcond gnutls 1
%bcond openssl 1
%bcond snmp 0
%bcond rdkafka 0
%bcond hiredis 0
%bcond mongodb 0
%bcond relp 0

Name:           rsyslog
Version:        8.2510.0
Release:        %autorelease
Summary:        Enhanced system logging and kernel message trapping daemon
License:        Apache-2.0 AND GPL-3.0-or-later
URL:            https://www.rsyslog.com/
VCS:            git:https://github.com/rsyslog/rsyslog
#!RemoteAsset
Source0:        https://www.rsyslog.com/files/download/%{name}/%{name}-%{version}.tar.gz
Source1:        rsyslog.conf
Source2:        rsyslog.logrotate.conf
Source3:        rsyslog.service
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-testbench
# For default we enable these
BuildOption(conf):  --enable-clickhouse
BuildOption(conf):  --enable-imdocker
BuildOption(conf):  --enable-libcap-ng
BuildOption(conf):  --enable-impstats
BuildOption(conf):  --enable-imptcp
BuildOption(conf):  --enable-imfile
BuildOption(conf):  --enable-imjournal
BuildOption(conf):  --enable-mail
BuildOption(conf):  --enable-mmanon
BuildOption(conf):  --enable-mmaudit
BuildOption(conf):  --enable-mmcount
BuildOption(conf):  --enable-mmfields
BuildOption(conf):  --enable-mmkubernetes
BuildOption(conf):  --enable-mmjsonparse
BuildOption(conf):  --enable-mmnormalize
BuildOption(conf):  --enable-mmutf8fix
BuildOption(conf):  --enable-omjournal
BuildOption(conf):  --enable-omprog
BuildOption(conf):  --enable-omstdout
BuildOption(conf):  --enable-omuxsock
BuildOption(conf):  --enable-pmaixforwardedfrom
BuildOption(conf):  --enable-pmcisconames
BuildOption(conf):  --enable-pmlastmsg
BuildOption(conf):  --enable-pmsnare
BuildOption(conf):  --enable-unlimited-select
BuildOption(conf):  --enable-usertools
BuildOption(conf):  --enable-omhttp
BuildOption(conf):  --enable-improg
BuildOption(conf):  --disable-libgcrypt
%if %{with elasticsearch}
BuildOption(conf):  --enable-elasticsearch
%endif
%if %{with gnutls}
BuildOption(conf):  --enable-gnutls
%endif
%if %{with gssapi}
BuildOption(conf):  --enable-gssapi-krb5
%endif
%if %{with hiredis}
BuildOption(conf):  --enable-omhiredis
%endif
%if %{with rdkafka}
BuildOption(conf):  --enable-imkafka
BuildOption(conf):  --enable-omkafka
%endif
%if %{with mongodb}
BuildOption(conf):  --enable-ommongodb
%endif
%if %{with mysql}
BuildOption(conf):  --enable-mysql
%endif
%if %{with openssl}
BuildOption(conf):  --enable-openssl
%endif
%if %{with pgsql}
BuildOption(conf):  --enable-pgsql
%endif
%if %{with snmp}
BuildOption(conf):  --enable-mmsnmptrapd
%endif
%if %{with relp}
BuildOption(conf):  --enable-relp
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(libestr)
BuildRequires:  pkgconfig(libfastjson)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(lognorm)
%if %{with relp}
BuildRequires:  pkgconfig(librelp)
%endif

%description
Rsyslog is an enhanced, multi-threaded syslog daemon. It supports MySQL,
syslog/TCP, RFC 3195, permitted sender lists, filtering on any message part,
and fine grain output format control. It is compatible with stock sysklogd
and can be used as a drop-in replacement. Rsyslog is simple to set up, with
advanced features suitable for enterprise-class, encryption-protected syslog
relay chains.

%package        doc
Summary:        HTML documentation for rsyslog
BuildArch:      noarch

%description    doc
This subpackage contains documentation for rsyslog.

%if %{with elasticsearch}
%package        elasticsearch
Summary:        ElasticSearch output module for rsyslog
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    elasticsearch
This subpackage provides the capability for rsyslog to feed logs directly
into Elasticsearch.
%endif

%if %{with gnutls}
%package        gnutls
Summary:        TLS protocol support for rsyslog via GnuTLS library
BuildRequires:  pkgconfig(gnutls)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gnutls
This subpackage contains the rsyslog plugins that provide the ability
to send and receive syslog messages via TCP or RELP using TLS encryption
via GnuTLS library. For details refer to rsyslog doc on imtcp and omfwd
modules.
%endif

%if %{with gssapi}
%package        gssapi
Summary:        GSSAPI authentication and encryption support for rsyslog
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  pkgconfig(krb5)

%description    gssapi
This subpackage contains the rsyslog plugins which support GSSAPI
authentication and secure connections. GSSAPI is commonly used for Kerberos
authentication.
%endif

%if %{with hiredis}
%package        hiredis
Summary:        Redis support for rsyslog
BuildRequires:  pkgconfig(hiredis)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    hiredis
This subpackage provides output to Redis.
%endif

%if %{with rdkafka}
%package        kafka
Summary:        Provides the omkafka module
BuildRequires:  pkgconfig(rdkafka)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    kafka
This subpackage provides module for Apache Kafka output.
%endif

%if %{with mongodb}
%package        mongodb
Summary:        MongoDB support for rsyslog
BuildRequires:  pkgconfig(libmongoc-1.0)
BuildRequires:  snappy-devel
BuildRequires:  pkgconfig(libsasl2)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    mongodb
This subpackage contains a dynamic shared object that will add MongoDB
database support to rsyslog.
%endif

%if %{with mysql}
%package        mysql
Summary:        MySQL support for rsyslog
BuildRequires:  pkgconfig(libmariadb)
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description    mysql
This subpackage contains a dynamic shared object that will add MySQL
database support to rsyslog.
%endif

%if %{with openssl}
%package        openssl
Summary:        TLS protocol support for rsyslog via OpenSSL library
BuildRequires:  pkgconfig(openssl)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl

%description    openssl
This subpackage contains the rsyslog plugins that provide the ability
to send and receive syslog messages via TCP or RELP using TLS encryption
via OpenSSL library. For details refer to rsyslog doc on imtcp and omfwd
modules.
%endif

%if %{with pgsql}
%package        pgsql
Summary:        PostgresSQL support for rsyslog
BuildRequires:  pkgconfig(libpq)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    pgsql
This subpackage contains a dynamic shared object that will add PostgreSQL
database support to rsyslog.
%endif

%if %{with snmp}
%package        snmp
Summary:        SNMP protocol support for rsyslog
BuildRequires:  pkgconfig(netsnmp)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    snmp
This subpackage contains the rsyslog plugin that provides the ability
to send syslog messages as SNMPv1 and SNMPv2c traps.
%endif

%conf -p
autoreconf -fiv

%install -a
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -d -m 755 %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_sysconfdir}/rsyslog.d
install -d -m 700 %{buildroot}%{_sharedstatedir}/rsyslog
install -d -m 700 %{buildroot}%{_sysconfdir}/pki/rsyslog
install -d -m 755 %{buildroot}%{_docdir}/rsyslog/html

install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rsyslog.conf
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/rsyslog
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/rsyslog.service

%if %{with mysql}
install -p -m 644 plugins/ommysql/createDB.sql %{buildroot}%{rsyslog_docdir}/mysql-createDB.sql
%endif

%if %{with pgsql}
install -p -m 644 plugins/ompgsql/createDB.sql %{buildroot}%{rsyslog_docdir}/pgsql-createDB.sql
%endif

cp -r doc/* %{buildroot}%{_docdir}/rsyslog/html

%post
for n in /var/log/{messages,secure,maillog,spooler}
do
    [ -f $n ] && continue
    umask 066 && touch $n
done
%systemd_post rsyslog.service

%preun
%systemd_preun rsyslog.service

%postun
%systemd_postun_with_restart rsyslog.service

%files
%license COPYING*
%doc AUTHORS ChangeLog README.md
%dir %{_libdir}/rsyslog
%dir %{_sysconfdir}/rsyslog.d
%dir %{_sharedstatedir}/rsyslog
%dir %{_sysconfdir}/pki/rsyslog
%{_sbindir}/rsyslogd
%{_mandir}/man5/rsyslog.conf.5.gz
%{_mandir}/man8/rsyslogd.8.gz
%{_unitdir}/rsyslog.service
%config(noreplace) %{_sysconfdir}/rsyslog.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/rsyslog
# plugins
%{_libdir}/rsyslog/fmhash.so
%{_libdir}/rsyslog/fmhttp.so
%{_libdir}/rsyslog/imfile.so
%{_libdir}/rsyslog/imjournal.so
%{_libdir}/rsyslog/imklog.so
%{_libdir}/rsyslog/immark.so
%{_libdir}/rsyslog/impstats.so
%{_libdir}/rsyslog/imptcp.so
%{_libdir}/rsyslog/imtcp.so
%{_libdir}/rsyslog/imudp.so
%{_libdir}/rsyslog/imuxsock.so
%{_libdir}/rsyslog/lmnet.so
%{_libdir}/rsyslog/lmnetstrms.so
%{_libdir}/rsyslog/lmnsd_ptcp.so
%{_libdir}/rsyslog/lmregexp.so
%{_libdir}/rsyslog/lmtcpclt.so
%{_libdir}/rsyslog/lmtcpsrv.so
%{_libdir}/rsyslog/lmzlibw.so
%{_libdir}/rsyslog/mmanon.so
%{_libdir}/rsyslog/mmcount.so
%{_libdir}/rsyslog/mmexternal.so
%{_libdir}/rsyslog/mmleefparse.so
%{_libdir}/rsyslog/mmutf8fix.so
%{_libdir}/rsyslog/omhttp.so
%{_libdir}/rsyslog/omjournal.so
%{_libdir}/rsyslog/ommail.so
%{_libdir}/rsyslog/omprog.so
%{_libdir}/rsyslog/omstdout.so
%{_libdir}/rsyslog/omtesting.so
%{_libdir}/rsyslog/omuxsock.so
%{_libdir}/rsyslog/pmaixforwardedfrom.so
%{_libdir}/rsyslog/pmcisconames.so
%{_libdir}/rsyslog/pmlastmsg.so
%{_libdir}/rsyslog/pmsnare.so
%{_libdir}/rsyslog/imdocker.so
%{_libdir}/rsyslog/improg.so
%{_libdir}/rsyslog/omclickhouse.so
%{_libdir}/rsyslog/mmaudit.so
%{_libdir}/rsyslog/mmfields.so
%{_libdir}/rsyslog/mmjsonparse.so
%{_libdir}/rsyslog/mmkubernetes.so
%{_libdir}/rsyslog/mmnormalize.so
%if %{with relp}
%{_libdir}/rsyslog/imrelp.so
%{_libdir}/rsyslog/omrelp.so
%endif

%files doc
%dir %{_docdir}/rsyslog
%{_docdir}/rsyslog/html

%if %{with elasticsearch}
%files elasticsearch
%{_libdir}/rsyslog/omelasticsearch.so
%endif

%if %{with gnutls}
%files gnutls
%{_libdir}/rsyslog/lmnsd_gtls.so
%endif

%if %{with gssapi}
%files gssapi
%{_libdir}/rsyslog/lmgssutil.so
%{_libdir}/rsyslog/imgssapi.so
%{_libdir}/rsyslog/omgssapi.so
%endif

%if %{with hiredis}
%files hiredis
%{_libdir}/rsyslog/omhiredis.so
%endif

%if %{with rdkafka}
%files kafka
%{_libdir}/rsyslog/imkafka.so
%{_libdir}/rsyslog/omkafka.so
%endif

%if %{with mongodb}
%files mongodb
%{_bindir}/logctl
%{_libdir}/rsyslog/ommongodb.so
%endif

%if %{with snmp}
%files snmp
%{_libdir}/rsyslog/mmsnmptrapd.so
%endif

%if %{with mysql}
%files mysql
%doc %{rsyslog_docdir}/mysql-createDB.sql
%{_libdir}/rsyslog/ommysql.so
%endif

%if %{with openssl}
%files openssl
%{_libdir}/rsyslog/lmnsd_ossl.so
%endif

%if %{with pgsql}
%files pgsql
%doc %{rsyslog_docdir}/pgsql-createDB.sql
%{_libdir}/rsyslog/ompgsql.so
%endif

%if %{with snmp}
%files snmp
%{_libdir}/rsyslog/omsnmp.so
%endif

%changelog
%autochangelog
