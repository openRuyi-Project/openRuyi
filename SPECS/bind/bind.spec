# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond geoip2 1
%bcond dnstap 0
%bcond jemalloc 1

Name:           bind
Version:        9.20.31
Release:        %autorelease
Summary:        Domain Name System (DNS) Server
License:        MPL-2.0 AND ISC AND MIT AND BSD-2-Clause AND BSD-3-Clause
URL:            https://www.isc.org/bind/
VCS:            git:https://gitlab.isc.org/isc-projects/bind9.git
#!RemoteAsset:  sha256:9bfecd503ec79209d321053689c794da9f8dba993a24e9cd6bd7aa87cdf4122f
Source0:        https://downloads.isc.org/isc/bind9/%{version}/%{name}-%{version}.tar.xz
Source1:        bind.sysusers
Source2:        bind.tmpfiles
Source3:        named.service
Source4:        named.conf
Source5:        127.0.0.zone
Source6:        localhost.zone
Source7:        localhost.ip6.zone
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-cmocka
BuildOption(conf):  --with-gssapi
BuildOption(conf):  --with-openssl
BuildOption(conf):  --with-libidn2
BuildOption(conf):  --with-json-c
BuildOption(conf):  --with-libxml2
BuildOption(conf):  --with-lmdb
%if %{with geoip2}
BuildOption(conf):  --with-maxminddb
%else
BuildOption(conf):  --disable-geoip
%endif
%if %{with dnstap}
BuildOption(conf):  --enable-dnstap
%endif
%if %{with jemalloc}
BuildOption(conf):  --with-jemalloc
%else
BuildOption(conf):  --without-jemalloc
%endif
BuildOption(conf):  --enable-fixed-rrset
BuildOption(conf):  --enable-full-report
# Bound lock benchmark iterations under the upstream test timeout.
BuildOption(check):  ISC_BENCHMARK_LOOPS=10

BuildRequires:  pkgconfig(cmocka) >= 1.1.3
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(openssl)
%if %{with jemalloc}
BuildRequires:  pkgconfig(jemalloc)
%endif
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libidn2)
%if %{with geoip2}
BuildRequires:  pkgconfig(libmaxminddb)
%endif
%if %{with dnstap}
BuildRequires:  protobuf-c-compiler
BuildRequires:  pkgconfig(libfstrm)
BuildRequires:  pkgconfig(libprotobuf-c)
%endif
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lmdb)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(dnspython)
BuildRequires:  python3dist(gssapi)
BuildRequires:  python3dist(h2)
BuildRequires:  python3dist(hypothesis) >= 4.41.2
BuildRequires:  python3dist(jinja2) >= 3.0.0
BuildRequires:  python3dist(pytest) >= 7
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)

%description
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses; a resolver library
(routines for applications to use when interfacing with DNS); and
tools for verifying that the DNS server is operating properly.

%package        utils
Summary:        Utilities for querying DNS name servers
# For compatibility with Debian package
Provides:       dnsutils = %{version}-%{release}

%description    utils
This package includes the utilities "host", "dig", and "nslookup" used to
test and query the Domain Name System (DNS) and also the libraries rquired
for the base "bind" package.

%package        devel
Summary:        Header files and libraries for developing applications with BIND
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains full version of the header files and libraries
required for developing applications with BIND.

%install -a
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/bind.conf

mkdir -p %{buildroot}%{_tmpfilesdir}
install -p -m 644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/bind.conf

mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/named.service

mkdir -p %{buildroot}%{_sysconfdir}
install -m 640 %{SOURCE4} %{buildroot}%{_sysconfdir}/named.conf
mkdir -p %{buildroot}%{_localstatedir}/named/data
install -m 644 %{SOURCE5} %{buildroot}%{_localstatedir}/named/127.0.0.zone
install -m 644 %{SOURCE6} %{buildroot}%{_localstatedir}/named/localhost.zone
install -m 644 %{SOURCE7} %{buildroot}%{_localstatedir}/named/localhost.ip6.zone

%check -a
# Automake can report success when pytest exits before writing its results.
for result in bin/tests/system/*.trs; do
    grep -q '^:test-result: ' "$result" || exit 1
done

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%systemd_post named.service

%preun
%systemd_preun named.service

%postun
%systemd_postun_with_restart named.service

%files
%license LICENSE COPYRIGHT
%dir %{_localstatedir}/named
%dir %attr(0750,named,named) %{_localstatedir}/named/data
%config(noreplace) %attr(0640,root,named) %{_sysconfdir}/named.conf
%config(noreplace) %verify(not link) %{_localstatedir}/named/127.0.0.zone
%config(noreplace) %verify(not link) %{_localstatedir}/named/localhost.zone
%config(noreplace) %verify(not link) %{_localstatedir}/named/localhost.ip6.zone
%{_bindir}/named-rrchecker
%{_bindir}/named-checkconf
%{_bindir}/named-checkzone
%{_bindir}/named-compilezone
%{_bindir}/named-journalprint
%{_sbindir}/named
%{_sysusersdir}/bind.conf
%{_tmpfilesdir}/bind.conf
%{_unitdir}/named.service
%{_libdir}/bind/filter-a.so
%{_libdir}/bind/filter-aaaa.so
%{_mandir}/man1/named-rrchecker.1*
%{_mandir}/man5/named.conf.5*
%{_mandir}/man1/named-checkconf.1*
%{_mandir}/man1/named-checkzone.1*
%{_mandir}/man8/named.8*
%{_mandir}/man1/named-compilezone.1*
%{_mandir}/man1/named-journalprint.1*
%{_mandir}/man8/filter-aaaa.8*
%{_mandir}/man8/filter-a.8*

%files utils
%license LICENSE COPYRIGHT
%{_libdir}/libisccc-%{version}.so
%{_libdir}/libns-%{version}.so
%{_libdir}/libdns-%{version}.so
%{_libdir}/libisc-%{version}.so
%{_libdir}/libisccfg-%{version}.so
%{_bindir}/named-nzd2nzf
%{_bindir}/dig
%{_bindir}/delv
%{_bindir}/host
%{_bindir}/nslookup
%{_bindir}/nsupdate
%{_bindir}/arpaname
%{_sbindir}/ddns-confgen
%{_sbindir}/tsig-keygen
%{_bindir}/nsec3hash
%{_bindir}/mdig
%{_bindir}/dnssec-cds
%{_bindir}/dnssec-dsfromkey
%{_bindir}/dnssec-importkey
%{_bindir}/dnssec-keyfromlabel
%{_bindir}/dnssec-keygen
%{_bindir}/dnssec-ksr
%{_bindir}/dnssec-revoke
%{_bindir}/dnssec-settime
%{_bindir}/dnssec-signzone
%{_bindir}/dnssec-verify
%{_sbindir}/rndc
%{_sbindir}/rndc-confgen
%if %{with dnstap}
%{_bindir}/dnstap-read
%{_mandir}/man1/dnstap-read.1*
%endif
%{_mandir}/man1/host.1*
%{_mandir}/man1/mdig.1*
%{_mandir}/man1/nsupdate.1*
%{_mandir}/man1/dig.1*
%{_mandir}/man1/delv.1*
%{_mandir}/man1/nslookup.1*
%{_mandir}/man1/dnssec-dsfromkey.1*
%{_mandir}/man1/dnssec-importkey.1*
%{_mandir}/man1/dnssec-keyfromlabel.1*
%{_mandir}/man1/dnssec-keygen.1*
%{_mandir}/man1/dnssec-revoke.1*
%{_mandir}/man1/dnssec-settime.1*
%{_mandir}/man1/dnssec-signzone.1*
%{_mandir}/man1/dnssec-verify.1*
%{_mandir}/man1/arpaname.1*
%{_mandir}/man1/dnssec-cds.1*
%{_mandir}/man8/ddns-confgen.8*
%{_mandir}/man8/tsig-keygen.8*
%{_mandir}/man1/nsec3hash.1*
%{_mandir}/man8/rndc.8*
%{_mandir}/man8/rndc-confgen.8*
%{_mandir}/man1/dnssec-ksr.1*
%{_mandir}/man5/rndc.conf.5*
%{_mandir}/man1/named-nzd2nzf.1*

%files devel
%license LICENSE COPYRIGHT
%{_libdir}/libisccc.so
%{_libdir}/libns.so
%{_libdir}/libdns.so
%{_libdir}/libisc.so
%{_libdir}/libisccfg.so
%{_includedir}/isccc
%{_includedir}/ns
%{_includedir}/dns
%{_includedir}/dst
%{_includedir}/irs
%{_includedir}/isc
%{_includedir}/isccfg

%changelog
%autochangelog
