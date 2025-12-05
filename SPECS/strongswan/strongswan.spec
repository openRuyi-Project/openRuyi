# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond check 0

Name:           strongswan
Version:        6.0.2
Release:        %autorelease
Summary:        An OpenSource IPsec-based VPN and TNC solution
License:        GPL-2.0-or-later
URL:            https://www.strongswan.org/
VCS:            git:https://github.com/strongswan/strongswan
#!RemoteAsset
Source0:        https://download.strongswan.org/strongswan-%{version}.tar.bz2
Source1:        strongswan.tmpfiles
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-ipsec-script=strongswan
BuildOption(conf):  --sysconfdir=%{_sysconfdir}/strongswan
BuildOption(conf):  --with-ipsecdir=%{_libexecdir}/strongswan
BuildOption(conf):  --bindir=%{_libexecdir}/strongswan
BuildOption(conf):  --with-ipseclibdir=%{_libdir}/strongswan
BuildOption(conf):  --with-piddir=%{_rundir}/strongswan
BuildOption(conf):  --with-nm-ca-dir=%{_sysconfdir}/strongswan/ipsec.d/cacerts/
BuildOption(conf):  --enable-bypass-lan
BuildOption(conf):  --enable-tss-tss2
BuildOption(conf):  --disable-nm
BuildOption(conf):  --enable-systemd
BuildOption(conf):  --enable-openssl
BuildOption(conf):  --enable-unity
BuildOption(conf):  --enable-ctr
BuildOption(conf):  --enable-ccm
BuildOption(conf):  --enable-gcm
BuildOption(conf):  --enable-chapoly
BuildOption(conf):  --enable-md4
BuildOption(conf):  --enable-ml
BuildOption(conf):  --enable-gcrypt
BuildOption(conf):  --enable-newhope
BuildOption(conf):  --enable-xauth-eap
BuildOption(conf):  --enable-xauth-pam
BuildOption(conf):  --enable-xauth-noauth
BuildOption(conf):  --enable-eap-identity
BuildOption(conf):  --enable-eap-md5
BuildOption(conf):  --enable-eap-gtc
BuildOption(conf):  --enable-eap-tls
BuildOption(conf):  --enable-eap-ttls
BuildOption(conf):  --enable-eap-peap
BuildOption(conf):  --enable-eap-mschapv2
BuildOption(conf):  --enable-eap-tnc
BuildOption(conf):  --enable-eap-sim
BuildOption(conf):  --enable-eap-sim-file
BuildOption(conf):  --enable-eap-aka
BuildOption(conf):  --enable-eap-aka-3gpp
BuildOption(conf):  --enable-eap-aka-3gpp2
BuildOption(conf):  --enable-eap-dynamic
BuildOption(conf):  --enable-eap-radius
BuildOption(conf):  --enable-ext-auth
BuildOption(conf):  --enable-ipseckey
BuildOption(conf):  --enable-pkcs11
BuildOption(conf):  --enable-tpm
BuildOption(conf):  --enable-farp
BuildOption(conf):  --enable-dhcp
BuildOption(conf):  --enable-ha
BuildOption(conf):  --enable-led
BuildOption(conf):  --enable-sql
BuildOption(conf):  --enable-sqlite
BuildOption(conf):  --enable-tnc-ifmap
BuildOption(conf):  --enable-tnc-pdp
BuildOption(conf):  --enable-tnc-imc
BuildOption(conf):  --enable-tnc-imv
BuildOption(conf):  --enable-tnccs-20
BuildOption(conf):  --enable-tnccs-11
BuildOption(conf):  --enable-tnccs-dynamic
BuildOption(conf):  --enable-imc-test
BuildOption(conf):  --enable-imv-test
BuildOption(conf):  --enable-imc-scanner
BuildOption(conf):  --enable-imv-scanner
BuildOption(conf):  --enable-imc-attestation
BuildOption(conf):  --enable-imv-attestation
BuildOption(conf):  --enable-imv-os
BuildOption(conf):  --enable-imc-os
BuildOption(conf):  --enable-imc-swima
BuildOption(conf):  --enable-imv-swima
BuildOption(conf):  --enable-imc-hcd
BuildOption(conf):  --enable-imv-hcd
BuildOption(conf):  --enable-curl
BuildOption(conf):  --enable-cmd
BuildOption(conf):  --enable-acert
BuildOption(conf):  --enable-vici
BuildOption(conf):  --enable-swanctl
BuildOption(conf):  --enable-duplicheck
BuildOption(conf):  --enable-selinux
BuildOption(conf):  --enable-stroke
BuildOption(conf):  --enable-kernel-libipsec
BuildOption(conf):  --with-capabilities=libcap
BuildOption(conf):  CPPFLAGS="-DSTARTER_ALLOW_NON_ROOT"

%ifarch x86_64
BuildOption(conf):  --enable-aesni
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pam)
BuildRequires:  json-c-devel
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(xtables)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  tpm2-tss-devel

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
The strongSwan IPsec implementation supports both the IKEv1 and IKEv2 key
exchange protocols in conjunction with the native NETKEY IPsec stack of the
Linux kernel.

%package        tnc-imcvs
Summary:        Trusted network connect (TNC)'s IMC/IMV functionality
Requires:       %{name} = %{version}-%{release}

%description   tnc-imcvs
This package provides Trusted Network Connect's (TNC) architecture support.

%conf -p
export ACLOCAL_PATH=/usr/share/gettext/m4:$ACLOCAL_PATH
autoreconf -fiv

%install -a
# prefix man pages
for i in %{buildroot}%{_mandir}/*/*; do
    if echo "$i" | grep -vq '/strongswan[^\/]*$'; then
        mv "$i" "`echo "$i" | sed -re 's|/([^/]+)$|/strongswan_\1|'`"
    fi
done

# delete unwanted library files - no consumers, so no -devel package
rm -f %{buildroot}%{_libdir}/strongswan/*.so

chmod 644 %{buildroot}%{_sysconfdir}/strongswan/strongswan.conf

install -d -m 700 %{buildroot}%{_sysconfdir}/strongswan/ipsec.d/{aacerts,acerts,certs,cacerts,crls,ocspcerts,private,reqs}
install -d -m 0700 %{buildroot}%{_rundir}/strongswan

install -D -m 0644 %{SOURCE1} %{buildroot}/%{_tmpfilesdir}/strongswan.conf

%pre
%tmpfiles_create_package %{name} %SOURCE1

%post
%systemd_post strongswan.service strongswan-starter.service

%preun
%systemd_preun strongswan.service strongswan-starter.service

%postun
%systemd_postun_with_restart strongswan.service strongswan-starter.service

%files
%license COPYING
%doc README NEWS TODO ChangeLog
%dir %attr(0755,root,root) %{_sysconfdir}/strongswan
%config(noreplace) %{_sysconfdir}/strongswan/*
%dir %{_libdir}/strongswan
%exclude %{_libdir}/strongswan/imcvs
%dir %{_libdir}/strongswan/plugins
%dir %{_libexecdir}/strongswan
%{_unitdir}/strongswan.service
%{_unitdir}/strongswan-starter.service
%{_sbindir}/charon-cmd
%{_sbindir}/charon-systemd
%{_sbindir}/strongswan
%{_sbindir}/swanctl
%{_libdir}/strongswan/*.so.*
%{_libdir}/strongswan/plugins/*.so.*
%exclude %{_libdir}/strongswan/libimcv.so.*
%exclude %{_libdir}/strongswan/libtnccs.so.*
%exclude %{_libdir}/strongswan/libipsec.so.*
%{_libdir}/strongswan/plugins/*.so
%{_libexecdir}/strongswan/*
%exclude %{_libexecdir}/strongswan/attest
%exclude %{_libexecdir}/strongswan/pt-tls-client
%exclude %dir %{_datadir}/strongswan/swidtag
%{_mandir}/man?/*.gz
%{_datadir}/strongswan/templates/config/
%{_datadir}/strongswan/templates/database/
%attr(0755,root,root) %dir %{_rundir}/strongswan
%{_tmpfilesdir}/strongswan.conf
%{_libdir}/strongswan/libipsec.so.*

%files tnc-imcvs
%{_sbindir}/sw-collector
%{_sbindir}/sec-updater
%dir %{_libdir}/strongswan/imcvs
%dir %{_libdir}/strongswan/plugins
%{_libdir}/strongswan/libimcv.so.*
%{_libdir}/strongswan/libtnccs.so.*
%{_libdir}/strongswan/plugins/libstrongswan-*tnc*.so
%{_libexecdir}/strongswan/attest
%{_libexecdir}/strongswan/pt-tls-client
%dir %{_datadir}/strongswan/swidtag
%{_datadir}/strongswan/swidtag/*.swidtag

%changelog
%{?autochangelog}
