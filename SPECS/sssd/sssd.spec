# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Determine the location of the LDB modules directory
%global ldb_modulesdir %(pkg-config --variable=modulesdir ldb)

Name:           sssd
Version:        2.11.1
Release:        %autorelease
Summary:        System Security Services Daemon
License:        GPL-3.0-or-later
URL:            https://github.com/SSSD/sssd/
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-rpath
BuildOption(conf):  --without-oidc-child
BuildOption(conf):  --with-db-path=%{_localstatedir}/lib/sss/db
BuildOption(conf):  --with-gpo-cache-path=%{_localstatedir}/lib/sss/gpo_cache
BuildOption(conf):  --with-pipe-path=%{_localstatedir}/lib/sss/pipes
BuildOption(conf):  --with-pubconf-path=%{_localstatedir}/lib/sss/pubconf
BuildOption(conf):  --with-initscript=systemd
BuildOption(conf):  --with-syslog=journald
BuildOption(conf):  --without-python2-bindings
BuildOption(conf):  --with-sssd-user=sssd
BuildOption(conf):  --with-subid
BuildOption(build):  all

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  bind-utils
BuildRequires:  cifs-utils-devel
BuildRequires:  docbook-xsl
BuildRequires:  docbook-style-dsssl
BuildRequires:  libunistring-devel
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(augeas)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(collection)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dhash)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(ini_config)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(ldb)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(libnfsidmap)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libsemanage)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ndr_krb5pac)
BuildRequires:  pkgconfig(ndr_nbt)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  pkgconfig(tdb)
BuildRequires:  pkgconfig(tevent)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  shadow-devel

%description
This package provides a set of daemons to manage access to remote directories
and authentication mechanisms. It provides an NSS and PAM interface toward
the system and a pluggable back end system to connect to multiple different
account sources. It is also the basis to provide client auditing and policy
services for projects like FreeIPA.

%package        ad
Summary:        The ActiveDirectory backend plugin for sssd
Requires:       %{name}-krb5 = %{version}-%{release}

%description    ad
A back-end provider that the SSSD can utilize to fetch identity data
from, and authenticate with, an Active Directory server.

%package        dbus
Summary:        The D-Bus responder of sssd
Requires:       %{name} = %{version}-%{release}

%description    dbus
D-Bus responder of sssd, called InfoPipe, which allows
information from sssd to be transmitted over the system bus.

%package        ipa
Summary:        FreeIPA backend plugin for sssd
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-ad = %{version}-%{release}

%description    ipa
A back-end provider that the SSSD can utilize to fetch identity data
from, and authenticate with, an IPA server.

%package        kcm
Summary:        SSSD's Kerberos cache manager
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}

%description    kcm
KCM is a process that stores, tracks and manages Kerberos credential
caches.

%package        krb5
Summary:        The Kerberos authentication back end for the SSSD
Requires:       %{name} = %{version}-%{release}

%description    krb5
Provides the Kerberos back end that the SSSD can utilize authenticate
against a Kerberos server.

%package        ldap
Summary:        The LDAP backend plugin for sssd
Requires:       %{name}-krb5 = %{version}-%{release}

%description    ldap
A back-end provider that the SSSD can utilize to fetch identity data
from, and authenticate with, an LDAP server.

%package        proxy
Summary:        The proxy backend plugin for sssd

%description    proxy
A back-end provider which can be used to wrap existing NSS and/or PAM
modules to leverage SSSD caching. (This can replace nscd.)

%package        nfs-idmap
Summary:        SSSD plug-in for NFSv4 rpc.idmapd

%description    nfs-idmap
The libnfsidmap sssd module provides a way for rpc.idmapd to call SSSD to map
UIDs/GIDs to names and vice versa. It can be also used for mapping principal
(user) name to IDs(UID or GID) or to obtain groups which user are member of.

%package        winbind-idmap
Summary:        The sss idmap backend for Winbind

%description    winbind-idmap
The idmap_sss module provides a way for Winbind to call SSSD to map
UIDs/GIDs and SIDs.

%package     -n sss-sudo
Summary:        A library to allow communication between SUDO and SSSD
License:        LGPL-3.0-or-later

%description -n sss-sudo
A utility library to allow communication between SUDO and SSSD

%package     -n sss-idmap
Summary:        FreeIPA Idmap library
Provides:       sss-idmap-devel

%description -n sss-idmap
Utility library to convert SIDs to Unix uids and gids

%package     -n ipa-hbac
Summary:        FreeIPA HBAC Evaluator library
Provides:       ipa-hbac-devel

%description -n ipa-hbac
Utility library to validate FreeIPA HBAC rules for authorization requests

%package     -n sss-nss-idmap
Summary:        Library for SID and certificate based lookups
Provides:       sss-nss-idmap-devel

%description -n sss-nss-idmap
Utility library for SID and certificate based lookups

%package     -n sss-certmap
Summary:        SSSD Certificate Mapping Library
Provides:       sss-certmap-devel

%description -n sss-certmap
Library to map certificates to users based on rules

%package     -n python-sssdconfig
Summary:        SSSD and IPA configuration file manipulation classes and functions
%python_provide python3-sssdconfig

%description -n python-sssdconfig
Provides python3 files for manipulation SSSD and IPA configuration files.

%package     -n python-sss-murmur
Summary:        Python3 bindings for murmur hash function
License:        LGPL-3.0-or-later
%python_provide python3-sss-murmur

%description -n python-sss-murmur
Provides python3 module for calculating the murmur hash version 3

%package     -n python-ipa-hbac
Summary:        Python3 bindings for the FreeIPA HBAC Evaluator library
License:        LGPL-3.0-or-later
Requires:       ipa-hbac = %{version}-%{release}
%python_provide python-ipa-hbac

%description -n python-ipa-hbac
The python-ipa-hbac contains the bindings so that ipa-hbac can be
used by Python applications.

%package     -n python-sss-nss-idmap
Summary:        Python3 bindings for sss-nss-idmap
License:        LGPL-3.0-or-later
Requires:       sss-nss-idmap = %{version}-%{release}
%python_provide python-sss-nss-idmap

%description -n python-sss-nss-idmap
The python-sss-nss-idmap contains the bindings so that sss-nss-idmap can
be used by Python applications.

%conf -p
autoreconf -fiv

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/cifs-utils

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m644 src/examples/logrotate %{buildroot}%{_sysconfdir}/logrotate.d/sssd

mkdir -p %{buildroot}%{_sysconfdir}/krb5.conf.d/
cp %{buildroot}%{_datadir}/sssd/krb5-snippets/enable_sssd_conf_dir \
   %{buildroot}%{_sysconfdir}/krb5.conf.d/enable_sssd_conf_dir

install -Dm0644 contrib/sssd-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dpm0644 contrib/sssd.sysusers %{buildroot}%{_sysusersdir}/sssd.conf

%find_lang %{name} --generate-subpackages

%post
if [ -x /usr/bin/systemd-sysusers ]; then
   systemd-sysusers %{_sysusersdir}/sssd.conf || :
fi
if [ -x /usr/bin/systemd-tmpfiles ]; then
   systemd-tmpfiles --create %{_tmpfilesdir}/sssd.conf || :
fi

%systemd_post sssd.service
%systemd_post sssd-autofs.socket
%systemd_post sssd-nss.socket
%systemd_post sssd-ssh.socket
%systemd_post sssd-sudo.socket
%__rm -f %{_localstatedir}/lib/sss/mc/passwd
%__rm -f %{_localstatedir}/lib/sss/mc/group
%__rm -f %{_localstatedir}/lib/sss/mc/initgroups
%__rm -f %{_localstatedir}/lib/sss/mc/sid
%__rm -f %{_localstatedir}/lib/sss/pubconf/known_hosts

%preun
%systemd_preun sssd.service
%systemd_preun sssd-autofs.socket
%systemd_preun sssd-nss.socket
%systemd_preun sssd-pam.socket
%systemd_preun sssd-ssh.socket
%systemd_preun sssd-sudo.socket

%postun
%__rm -f %{_localstatedir}/lib/sss/mc/passwd
%__rm -f %{_localstatedir}/lib/sss/mc/group
%__rm -f %{_localstatedir}/lib/sss/mc/initgroups
%__rm -f %{_localstatedir}/lib/sss/mc/sid
%systemd_postun_with_restart sssd-autofs.socket
%systemd_postun_with_restart sssd-nss.socket
%systemd_postun_with_restart sssd-pam.socket
%systemd_postun_with_restart sssd-ssh.socket
%systemd_postun_with_restart sssd-sudo.socket

%systemd_postun sssd-autofs.service
%systemd_postun sssd-nss.service
%systemd_postun sssd-pam.service
%systemd_postun sssd-ssh.service
%systemd_postun sssd-sudo.service

%post dbus
%systemd_post sssd-ifp.service

%preun dbus
%systemd_preun sssd-ifp.service

%postun dbus
%systemd_postun_with_restart sssd-ifp.service

%post kcm
%systemd_post sssd-kcm.socket

%preun kcm
%systemd_preun sssd-kcm.socket

%postun kcm
%systemd_postun_with_restart sssd-kcm.socket
%systemd_postun_with_restart sssd-kcm.service

%posttrans
%systemd_postun_with_restart sssd.service
%__chown -f -R root:sssd %{_sysconfdir}/sssd || true
%__chmod -f -R g+r %{_sysconfdir}/sssd || true
%__chown -f -h sssd:sssd %{_localstatedir}/lib/sss/db/* || true
%__chown -f -h sssd:sssd %{_localstatedir}/log/%{name}/*.log* || true
%__chown -f -h sssd:sssd %{_localstatedir}/lib/sss/secrets/*.ldb || true
%__chown -f -R sssd:sssd %{_localstatedir}/lib/sss/gpo_cache || true

%files
%license src/sss_client/COPYING src/sss_client/COPYING.LESSER
%doc src/examples/sssd-example.conf
%{_sbindir}/sssd
%{_unitdir}/sssd.service
%{_unitdir}/sssd-autofs.socket
%{_unitdir}/sssd-autofs.service
%{_unitdir}/sssd-nss.socket
%{_unitdir}/sssd-nss.service
%{_unitdir}/sssd-pam.socket
%{_unitdir}/sssd-pam.service
%{_unitdir}/sssd-ssh.socket
%{_unitdir}/sssd-ssh.service
%{_unitdir}/sssd-sudo.socket
%{_unitdir}/sssd-sudo.service
%{_tmpfilesdir}/%{name}.conf
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/sssd_be
%{_libexecdir}/%{name}/sssd_nss
%attr(0750,root,sssd) %caps(cap_dac_read_search=p) %{_libexecdir}/%{name}/sssd_pam
%{_libexecdir}/%{name}/sssd_autofs
%{_libexecdir}/%{name}/sssd_ssh
%{_libexecdir}/%{name}/sssd_sudo
%{_libexecdir}/%{name}/p11_child
%{_libexecdir}/%{name}/sssd_check_socket_activated_responders
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libsss_simple.so
%{_libdir}/%{name}/libsss_child.so
%{_libdir}/%{name}/libsss_crypt.so
%{_libdir}/%{name}/libsss_cert.so
%{_libdir}/%{name}/libsss_debug.so
%{_libdir}/%{name}/libsss_krb5_common.so
%{_libdir}/%{name}/libsss_ldap_common.so
%{_libdir}/%{name}/libsss_util.so
%{_libdir}/%{name}/libifp_iface.so
%{_libdir}/%{name}/libifp_iface_sync.so
%{_libdir}/%{name}/libsss_iface.so
%{_libdir}/%{name}/libsss_iface_sync.so
%{_libdir}/%{name}/libsss_sbus.so
%{_libdir}/%{name}/libsss_sbus_sync.so
%{ldb_modulesdir}/memberof.so
%{_bindir}/sss_ssh_authorizedkeys
%{_bindir}/sss_ssh_knownhosts
%{_bindir}/sss_ssh_knownhostsproxy
%{_sbindir}/sss_cache
%{_libexecdir}/%{name}/sss_signal
%attr(775,sssd,sssd) %dir %{_localstatedir}/lib/sss
%attr(770,sssd,sssd) %dir %{_localstatedir}/lib/sss/db
%attr(775,sssd,sssd) %dir %{_localstatedir}/lib/sss/mc
%attr(770,sssd,sssd) %dir %{_localstatedir}/lib/sss/secrets
%attr(771,sssd,sssd) %dir %{_localstatedir}/lib/sss/deskprofile
%attr(775,sssd,sssd) %dir %{_localstatedir}/lib/sss/pipes
%attr(770,sssd,sssd) %dir %{_localstatedir}/lib/sss/pipes/private
%attr(775,sssd,sssd) %dir %{_localstatedir}/lib/sss/pubconf
%attr(770,sssd,sssd) %dir %{_localstatedir}/lib/sss/gpo_cache
%attr(770,sssd,sssd) %dir %{_localstatedir}/log/%{name}
%attr(750,root,sssd) %dir %{_sysconfdir}/sssd
%attr(750,root,sssd) %dir %{_sysconfdir}/sssd/conf.d
%attr(750,root,sssd) %dir %{_sysconfdir}/sssd/pki
%ghost %attr(0640,root,sssd) %config(noreplace) %{_sysconfdir}/sssd/sssd.conf
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/sssd
%dir %{_datadir}/sssd
%config(noreplace) %{_sysconfdir}/pam.d/sssd-shadowutils
%dir %{_libdir}/%{name}/conf
%{_libdir}/%{name}/conf/sssd.conf
%{_datadir}/sssd/cfg_rules.ini
%{_mandir}/man1/sss_ssh_authorizedkeys.1*
%{_mandir}/man1/sss_ssh_knownhosts.1*
%{_mandir}/man5/sssd.conf.5*
%{_mandir}/man5/sssd-simple.5*
%{_mandir}/man5/sssd-sudo.5*
%{_mandir}/man5/sssd-session-recording.5*
%{_mandir}/man8/sssd.8*
%{_mandir}/man8/sss_cache.8*
%{_sysusersdir}/sssd.conf
%{_datadir}/polkit-1/rules.d/*
# Client
%{_libdir}/libnss_sss.so.2
%{_libdir}/libsubid_sss.so
%{_libdir}/security/pam_sss.so
%{_libdir}/security/pam_sss_gss.so
%{_libdir}/krb5/plugins/libkrb5/sssd_krb5_locator_plugin.so
%dir %{_libdir}/cifs-utils
%{_libdir}/cifs-utils/cifs_idmap_sss.so
%dir %{_sysconfdir}/cifs-utils
%ghost %{_sysconfdir}/cifs-utils/idmap-plugin
%dir %{_libdir}/%{name}/modules
%{_libdir}/%{name}/modules/sssd_krb5_localauth_plugin.so
%{_mandir}/man8/pam_sss.8*
%{_mandir}/man8/pam_sss_gss.8*
%{_mandir}/man8/sssd_krb5_locator_plugin.8*
%{_mandir}/man8/sssd_krb5_localauth_plugin.8*
# sss-auto
%{_libdir}/%{name}/modules/libsss_autofs.so
# tools
%{_sbindir}/sss_obfuscate
%{_sbindir}/sss_override
%{_sbindir}/sss_debuglevel
%{_sbindir}/sss_seed
%{_sbindir}/sssctl
%{_libexecdir}/%{name}/sss_analyze
%{python3_sitelib}/sssd/
%{_mandir}/man8/sss_obfuscate.8*
%{_mandir}/man8/sss_override.8*
%{_mandir}/man8/sss_debuglevel.8*
%{_mandir}/man8/sss_seed.8*
%{_mandir}/man8/sssctl.8*
# TODO: %%find_lang failed us - 251
%{_mandir}/*/man1/sss_ssh_authorizedkeys.1*
%{_mandir}/*/man1/sss_ssh_knownhosts.1*
%{_mandir}/*/man5/sssd.conf.5*
%{_mandir}/*/man5/sssd-sudo.5*
%{_mandir}/*/man5/sssd-session-recording.5*
%{_mandir}/*/man5/sssd-systemtap.5*
%{_mandir}/*/man8/sssd.8*
%{_mandir}/*/man8/sss_cache.8*
# Emm why only for ru & sv - 251
%{_mandir}/*/man8/sss_debuglevel.8.gz
%{_mandir}/*/man8/sss_obfuscate.8*
%{_mandir}/*/man8/sss_override.8*
%{_mandir}/*/man8/sss_seed.8*
%{_mandir}/*/man8/sssctl.8*
%{_mandir}/*/man8/sssd_krb5_locator_plugin.8*
%{_mandir}/*/man8/sssd_krb5_localauth_plugin.8*
%{_mandir}/*/man8/pam_sss.8*
%{_mandir}/*/man8/pam_sss_gss.8*
# sssd-idp
%exclude %{_libdir}/sssd/libsss_idp.so
%exclude %{_libdir}/%{name}/modules/sssd_krb5_idp_plugin.so
%exclude %{_mandir}/man5/sssd-idp*

%files ldap
%{_libdir}/%{name}/libsss_ldap.so
%{_mandir}/man5/sssd-ldap.5*
%{_mandir}/man5/sssd-ldap-attributes.5*
# TODO: %%find_lang failed us - 251
%{_mandir}/*/man5/sssd-ldap.5*
%{_mandir}/*/man5/sssd-ldap-attributes.5*

%files krb5
%{_libdir}/%{name}/libsss_krb5.so
%{_mandir}/man5/sssd-krb5.5*
%attr(775,sssd,sssd) %dir %{_localstatedir}/lib/sss/pubconf/krb5.include.d
%attr(0750,root,sssd) %caps(cap_dac_read_search=p) %{_libexecdir}/%{name}/ldap_child
%attr(0750,root,sssd) %caps(cap_dac_read_search,cap_setuid,cap_setgid=p) %{_libexecdir}/%{name}/krb5_child
%config(noreplace) %{_sysconfdir}/krb5.conf.d/enable_sssd_conf_dir
%dir %{_datadir}/sssd/krb5-snippets
%{_datadir}/sssd/krb5-snippets/enable_sssd_conf_dir
%{_datadir}/sssd/krb5-snippets/sssd_enable_idp
# TODO: %%find_lang failed us - 251
%{_mandir}/*/man5/sssd-krb5.5*

%files ipa
%attr(770,sssd,sssd) %dir %{_localstatedir}/lib/sss/keytabs
%{_libdir}/%{name}/libsss_ipa.so
%attr(0750,root,sssd) %caps(cap_setuid,cap_setgid=p) %{_libexecdir}/%{name}/selinux_child
%{_mandir}/man5/sssd-ipa.5*
# TODO: %%find_lang failed us - 251
%{_mandir}/*/man5/sssd-ipa.5*

%files ad
%{_libdir}/%{name}/libsss_ad.so
%{_libexecdir}/%{name}/gpo_child
%{_mandir}/man5/sssd-ad.5*
# TODO: %%find_lang failed us - 251
%{_mandir}/*/man5/sssd-ad.5*

%files proxy
%attr(0750,root,sssd) %{_libexecdir}/%{name}/proxy_child
%{_libdir}/%{name}/libsss_proxy.so

%files dbus
%{_libexecdir}/%{name}/sssd_ifp
%{_mandir}/man5/sssd-ifp.5*
%{_unitdir}/sssd-ifp.service
%{_datadir}/dbus-1/system.d/org.freedesktop.sssd.infopipe.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.sssd.infopipe.service
# TODO: %%find_lang failed us - 251
%{_mandir}/*/man5/sssd-ifp.5*

%files kcm
%{_libexecdir}/%{name}/sssd_kcm
%dir %{_datadir}/sssd-kcm
%{_datadir}/sssd-kcm/kcm_default_ccache
%{_unitdir}/sssd-kcm.socket
%{_unitdir}/sssd-kcm.service
%{_mandir}/man8/sssd-kcm.8*
# TODO: %%find_lang failed us - 251
%{_mandir}/*/man8/sssd-kcm.8*

%files nfs-idmap
%{_mandir}/man5/sss_rpcidmapd.5*
%{_libdir}/libnfsidmap/sss.so
# TODO: %%find_lang failed us - 251
%{_mandir}/*/man5/sss_rpcidmapd.5*

%files winbind-idmap
%dir %{_libdir}/samba/idmap
%{_libdir}/samba/idmap/sss.so
%{_mandir}/man8/idmap_sss.8*
# TODO: %%find_lang failed us - 251
%{_mandir}/*/man8/idmap_sss.8*

%files -n sss-sudo
%{_libdir}/libsss_sudo.so*

%files -n python-sssdconfig
%dir %{python3_sitelib}/SSSDConfig
%{python3_sitelib}/SSSDConfig/*
%dir %{python3_sitelib}/SSSDConfig-*.egg-info
%{python3_sitelib}/SSSDConfig-*.egg-info/*
%dir %{_datadir}/sssd
%{_datadir}/sssd/sssd.api.conf
%{_datadir}/sssd/sssd.api.d
%{python3_sitearch}/pysss.so

%files -n python-sss-murmur
%{python3_sitearch}/pysss_murmur.so

%files -n sss-idmap
%{_libdir}/libsss_idmap.so.*
%{_includedir}/sss_idmap.h
%{_libdir}/libsss_idmap.so
%{_libdir}/pkgconfig/sss_idmap.pc

%files -n ipa-hbac
%{_libdir}/libipa_hbac.so.*
%{_includedir}/ipa_hbac.h
%{_libdir}/libipa_hbac.so
%{_libdir}/pkgconfig/ipa_hbac.pc

%files -n sss-nss-idmap
%{_libdir}/libsss_nss_idmap.so.*
%{_includedir}/sss_nss_idmap.h
%{_libdir}/libsss_nss_idmap.so
%{_libdir}/pkgconfig/sss_nss_idmap.pc

%files -n python-sss-nss-idmap
%{python3_sitearch}/pysss_nss_idmap.so

%files -n python-ipa-hbac
%{python3_sitearch}/pyhbac.so

%files -n sss-certmap
%{_libdir}/libsss_certmap.so.*
%{_mandir}/man5/sss-certmap.5*
%{_includedir}/sss_certmap.h
%{_libdir}/libsss_certmap.so
%{_libdir}/pkgconfig/sss_certmap.pc
# TODO: %%find_lang failed us - 251
%{_mandir}/*/man5/sss-certmap.5*

%changelog
%{?autochangelog}
