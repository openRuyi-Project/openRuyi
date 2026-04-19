# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Change to 1 to enable these
%bcond dnstap 0
%bcond redis 0
%bcond ngtcp2 0
%bcond munin 0
%bcond dracut 0

Name:           unbound
Version:        1.24.2
Release:        %autorelease
Summary:        Validating, recursive, and caching DNS(SEC) resolver
License:        BSD-3-Clause
URL:            https://nlnetlabs.nl/projects/unbound
VCS:            git:https://github.com/NLnetLabs/unbound
#!RemoteAsset:  sha256:44e7b53e008a6dcaec03032769a212b46ab5c23c105284aa05a4f3af78e59cdb
Source0:        https://nlnetlabs.nl/downloads/unbound/unbound-%{version}.tar.gz
#!RemoteAsset:  sha256:b9bc1395242e1d22bf8a2bf4504a40b405a6a4fa527db27116b50da317111246
Source1:        https://nlnetlabs.nl/downloads/unbound/unbound-%{version}.tar.gz.asc
Source2:        unbound.service
Source3:        unbound.munin
Source4:        unbound_munin_
Source5:        root.key
Source6:        unbound-keygen.service
Source7:        tmpfiles-unbound.conf
Source8:        example.com.key
Source9:        example.com.conf
Source10:       block-example.com.conf
#!RemoteAsset:  sha256:d4c77eafb8a3bc1d68fb7c171afbd0d2a76870dae81ad18d0c584fa46ecd1eb1
Source11:       https://data.iana.org/root-anchors/icannbundle.pem
Source12:       root.anchor
Source13:       unbound.sysconfig
Source14:       unbound-anchor.timer
Source15:       unbound-munin.README
Source16:       unbound-anchor.service
Source17:       unbound.sysusers
BuildSystem:    autotools

# high version swig change the way to gen code.
Patch0:         0001-adjust-to-high-swig.patch

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --disable-static
BuildOption(conf):  --with-libevent
BuildOption(conf):  --with-pthreads
BuildOption(conf):  --with-ssl
BuildOption(conf):  --enable-relro-now
BuildOption(conf):  --enable-pie
BuildOption(conf):  --enable-subnet
BuildOption(conf):  --enable-ipsecmod
BuildOption(conf):  --with-conf-file=%{_sysconfdir}/%{name}/unbound.conf
BuildOption(conf):  --with-pidfile=%{_rundir}/%{name}/%{name}.pid
BuildOption(conf):  --with-share-dir=%{_datadir}/%{name}
BuildOption(conf):  --enable-sha2
BuildOption(conf):  --disable-gost
BuildOption(conf):  --enable-ecdsa
BuildOption(conf):  --with-rootkey-file=%{_sharedstatedir}/%{name}/root.key
BuildOption(conf):  --with-pythonmodule
BuildOption(conf):  --with-pyunbound PYTHON=%{__python3}
BuildOption(conf):  --enable-systemd
BuildOption(conf):  --with-libnghttp2
%if %{with dnstap}
BuildOption(conf):  --enable-dnstap
%endif
%if %{with redis}
BuildOption(conf):  --with-libhiredis
BuildOption(conf):  --enable-cachedb
%endif
%if %{with ngtcp2}
BuildOption(conf):  --with-libngtcp2
%endif
BuildOption(build):  all streamtcp

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  systemd-rpm-macros
BuildRequires:  swig
BuildRequires:  flex
%if %{with dnstap}
BuildRequires:  pkgconfig(libfstrm)
BuildRequires:  pkgconfig(libprotobuf-c)
%endif
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libsodium)
%if %{with redis}
BuildRequires:  pkgconfig(hiredis)
%endif
%if %{with ngtcp2}
BuildRequires:  pkgconfig(libngtcp2_crypto_ossl)
%endif

Requires:       openssl

%description
Unbound is a validating, recursive, and caching DNS(SEC) resolver.

The C implementation of Unbound is developed and maintained by NLnet
Labs. It is based on ideas and algorithms taken from a java prototype
developed by Verisign labs, Nominet, Kirei and ep.net.

Unbound is designed as a set of modular components, so that also
DNSSEC (secure DNS) validation and stub-resolvers (that do not run
as a server, but are linked into an application) are easily possible.

%if %{with munin}
%package        munin
Summary:        Plugin for the munin / munin-node monitoring package
Requires:       munin-node
Requires:       %{name} = %{version}-%{release}
Requires:       bc
BuildArch:      noarch

%description    munin
Plugin for the munin / munin-node monitoring package
%endif

%package        devel
Summary:        Development package that includes the unbound header files
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pkgconfig(openssl)
Requires:       pkgconfig

%description    devel
The devel package contains the unbound library and the include files

%package        libs
Summary:        Libraries used by the unbound server and client applications
Provides:       group(unbound)
Provides:       user(unbound)
Recommends:     %{name}-anchor

%description    libs
Contains libraries used by the unbound server and client applications.

%package        anchor
Requires:       %{name}-libs = %{version}-%{release}
Summary:        DNSSEC trust anchor maintaining tool

%description    anchor
Contains tool maintaining trust anchor using RFC 5011 key rollover algorithm.

%package        utils
Requires:       %{name}-libs = %{version}-%{release}
Summary:        Unbound DNS lookup utilities

%description    utils
Contains tools for making DNS queries. Can make queries to DNS servers
also over TLS connection or validate DNSSEC signatures. Similar to
bind-utils.

%package     -n python3-unbound
Summary:        Python 3 modules and extensions for unbound
Requires:       %{name}-libs = %{version}-%{release}

%description -n python3-unbound
Python 3 modules and extensions for unbound

%conf -p
# always regenerate configure
autoreconf -fiv

%install -a
install -d -m 0755 %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/unbound.service
# Install root key
install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/unbound/
install -p -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/unbound-keygen.service
# Install tmpfiles.d config
install -d -m 0755 %{buildroot}%{_tmpfilesdir}/ %{buildroot}%{_sharedstatedir}/unbound
install -m 0644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/unbound.conf
# Install directories for easier config file drop in
mkdir -p %{buildroot}%{_sysconfdir}/unbound/{keys.d,conf.d,local.d}
install -m 0640 -p %{SOURCE8} %{buildroot}%{_sysconfdir}/unbound/keys.d/
install -m 0640 -p %{SOURCE9} %{buildroot}%{_sysconfdir}/unbound/conf.d/
install -m 0640 -p %{SOURCE10} %{buildroot}%{_sysconfdir}/unbound/local.d/
install -p -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/unbound
# We keep a copy of the root key in old location
# In case user has changed the configuration and we wouldn't update it there
install -m 0644 %{SOURCE12} %{buildroot}%{_sharedstatedir}/unbound/root.key
install -D -p -m 0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/sysconfig/unbound

install -p -m 0644 %{SOURCE14} %{buildroot}%{_unitdir}/unbound-anchor.timer
install -p -m 0644 %{SOURCE15} .
install -p -m 0644 %{SOURCE16} %{buildroot}%{_unitdir}/unbound-anchor.service
# sysusers.d
install -Dm0644 %{SOURCE17} %{buildroot}%{_sysusersdir}/unbound.conf

%if %{with munin}
# Install munin plugin and its softlinks
install -d 0755 %{buildroot}%{_sysconfdir}/munin/plugin-conf.d
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/munin/plugin-conf.d/unbound
install -d 0755 %{buildroot}%{_datadir}/munin/plugins/
install -p -m 0755 %{SOURCE4} %{buildroot}%{_datadir}/munin/plugins/unbound
for plugin in unbound_munin_hits unbound_munin_queue unbound_munin_memory unbound_munin_by_type unbound_munin_by_class unbound_munin_by_opcode unbound_munin_by_rcode unbound_munin_by_flags unbound_munin_histogram; do
    ln -s unbound %{buildroot}%{_datadir}/munin/plugins/$plugin
done
%endif

# install streamtcp used for monitoring / debugging unbound's port 80/443 modes
install -m 0755 streamtcp %{buildroot}%{_sbindir}/unbound-streamtcp
# install streamtcp man page
install -m 0644 testcode/streamtcp.1 %{buildroot}/%{_mandir}/man1/unbound-streamtcp.1
install -D -m 0644 contrib/libunbound.pc %{buildroot}/%{_libdir}/pkgconfig/libunbound.pc

mkdir -p %{buildroot}%{_rundir}/unbound

# Link unbound-control-setup.8 manpage to unbound-control.8
echo ".so man8/unbound-control.8" > %{buildroot}/%{_mandir}/man8/unbound-control-setup.8

%pre -n %{name}-libs
%sysusers_create_package unbound %{SOURCE17}

%pre
%sysusers_create_package unbound %{SOURCE17}

%preun
%systemd_preun unbound.service
%systemd_preun unbound-keygen.service

%preun anchor
%systemd_preun unbound-anchor.service unbound-anchor.timer

%postun
%systemd_postun_with_restart unbound.service
%systemd_postun unbound-keygen.service

%postun anchor
%systemd_postun_with_restart unbound-anchor.service unbound-anchor.timer

%files
%doc doc/CREDITS doc/FEATURES
%{_unitdir}/unbound.service
%{_unitdir}/unbound-keygen.service
%attr(0775,unbound,root) %dir %{_rundir}/%{name}
%attr(0644,root,root) %{_tmpfilesdir}/unbound.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/unbound.conf
%dir %attr(0755,root,unbound) %{_sysconfdir}/%{name}/keys.d
%attr(0644,root,unbound) %config(noreplace) %{_sysconfdir}/%{name}/keys.d/*.key
%dir %attr(0755,root,unbound) %{_sysconfdir}/%{name}/conf.d
%attr(0644,root,unbound) %config(noreplace) %{_sysconfdir}/%{name}/conf.d/*.conf
%dir %attr(0755,root,unbound) %{_sysconfdir}/%{name}/local.d
%attr(0644,root,unbound) %config(noreplace) %{_sysconfdir}/%{name}/local.d/*.conf
%ghost %attr(0640,root,unbound) %{_sysconfdir}/%{name}/unbound_control.pem
%ghost %attr(0640,root,unbound) %{_sysconfdir}/%{name}/unbound_control.key
%ghost %attr(0640,root,unbound) %{_sysconfdir}/%{name}/unbound_server.pem
%ghost %attr(0600,root,unbound) %{_sysconfdir}/%{name}/unbound_server.key
%{_sbindir}/unbound
%{_sbindir}/unbound-checkconf
%{_sbindir}/unbound-control
%{_sbindir}/unbound-control-setup
%{_mandir}/man5/*
%exclude %{_mandir}/man8/unbound-anchor*
%{_mandir}/man8/*

%files -n python3-unbound
%license pythonmod/LICENSE
%{python3_sitearch}/*
%doc libunbound/python/examples/*
%doc pythonmod/examples/*

%if %{with munin}
%files munin
%doc unbound-munin.README
%config(noreplace) %{_sysconfdir}/munin/plugin-conf.d/unbound
%{_datadir}/munin/plugins/unbound*
%endif

%files devel
%{_libdir}/libunbound.so
%{_includedir}/unbound.h
%{_mandir}/man3/*
%{_libdir}/pkgconfig/libunbound.pc

%files libs
%doc doc/README
%license doc/LICENSE
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%{_sysusersdir}/%{name}.conf
%{_libdir}/libunbound.so.8*
%dir %attr(0755,unbound,unbound) %{_sharedstatedir}/%{name}
%config %verify(not link owner group size mtime mode md5) %{_sharedstatedir}/%{name}/root.key
# just left for backwards compat with user changed unbound.conf files - format is different!
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/root.key

%files anchor
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sbindir}/unbound-anchor
%{_mandir}/man8/unbound-anchor*
# icannbundle and root.key(s) should be replaced from package
# intentionally not using noreplace
%config %{_sysconfdir}/%{name}/icannbundle.pem
%{_unitdir}/unbound-anchor.timer
%{_unitdir}/unbound-anchor.service

%files utils
%{_sbindir}/unbound-host
%{_sbindir}/unbound-streamtcp
%{_mandir}/man1/unbound-*

%changelog
%autochangelog
