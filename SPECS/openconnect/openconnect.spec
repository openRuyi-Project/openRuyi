# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openconnect
Version:        9.12
Release:        %autorelease
Summary:        Open multi-protocol SSL VPN client
License:        LGPL-2.1-or-later
URL:            https://gitlab.com/openconnect/openconnect
#!RemoteAsset:  sha256:a2bedce3aa4dfe75e36e407e48e8e8bc91d46def5335ac9564fbf91bd4b2413e
Source0:        https://www.infradead.org/openconnect/download/openconnect-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-dsa-tests
BuildOption(conf):  --with-default-gnutls-priority="@OPENCONNECT,SYSTEM"
BuildOption(conf):  --with-vpnc-script=/etc/vpnc/vpnc-script
BuildOption(conf):  --without-gnutls-version-check
BuildOption(check):  XFAIL_TESTS=obsolete-server-crypto

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  pkgconfig(krb5)
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(socket_wrapper)
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(uid_wrapper)
BuildRequires:  xdg-utils

%description
This package provides a multi-protocol VPN client for Cisco AnyConnect, Juniper
SSL VPN, Pulse/Ivanti Pulse Connect Secure, F5 BIG-IP, Fortinet Palo Alto
Networks GlobalProtect SSL VPN, Array Networks SSL VPN.

%package        devel
Summary:        Development package for OpenConnect VPN authentication tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides the core HTTP and authentication support from the
OpenConnect VPN client, to be used by GUI authentication dialogs for
NetworkManager etc.

%install -a
rm -f %{buildroot}/%{_libexecdir}/%{name}/tncc-wrapper.py
rm -f %{buildroot}/%{_libexecdir}/%{name}/hipreport-android.sh

# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license COPYING.LGPL
%{_datadir}/bash-completion/completions/openconnect
%{_mandir}/man8/*
%{_libdir}/libopenconnect.so.5*
%{_libexecdir}/openconnect/
%{_sbindir}/openconnect

%files devel
%{_includedir}/openconnect.h
%{_libdir}/libopenconnect.so
%{_libdir}/pkgconfig/openconnect.pc

%changelog
%autochangelog
