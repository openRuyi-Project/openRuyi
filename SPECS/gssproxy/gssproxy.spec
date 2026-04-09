# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global pubconfpath %{_sysconfdir}/gssproxy
%global gpstatedir %{_sharedstatedir}/gssproxy
%global gpsockpath %{_rundir}/gssproxy.default.sock

Name:           gssproxy
Version:        0.9.2
Release:        %autorelease
Summary:        GSSAPI Proxy
License:        MIT
URL:            https://github.com/gssapi/gssproxy
#!RemoteAsset
Source0:        https://github.com/gssapi/gssproxy/releases/download/v%{version}/gssproxy-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --with-pubconf-path=%{pubconfpath}
BuildOption(conf):  --with-socket-name=%{gpsockpath}
BuildOption(conf):  --with-initscript=systemd
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-rpath
BuildOption(conf):  --with-gpp-default-behavior=REMOTE_FIRST
BuildOption(conf):  --without-manpages

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(krb5) >= 1.12.0
BuildRequires:  keyutils-devel
BuildRequires:  pkgconfig(ini_config)
BuildRequires:  pkgconfig(libverto)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  gettext-devel

Requires:       ding-libs

%description
A proxy for GSSAPI credential handling.

%conf -p
autoreconf -fiv

%build -a
make test_proxymech

%install -a
install -d -m755 %{buildroot}%{_sysconfdir}/gssproxy
install -m644 examples/gssproxy.conf %{buildroot}%{_sysconfdir}/gssproxy/gssproxy.conf
install -m644 examples/99-network-fs-clients.conf %{buildroot}%{_sysconfdir}/gssproxy/99-network-fs-clients.conf

mkdir -p -m755 %{buildroot}%{_sysconfdir}/gss/mech.d
install -m644 examples/proxymech.conf %{buildroot}%{_sysconfdir}/gss/mech.d/proxymech.conf

mkdir -p %{buildroot}%{gpstatedir}/rcache
mkdir -p %{buildroot}%{gpstatedir}/clients

%check
# skip the tests as we don't have kdb5_ldap_util yet.

%post
%systemd_post gssproxy.service

%preun
%systemd_preun gssproxy.service

%postun
%systemd_postun_with_restart gssproxy.service

%files
%license COPYING
%{_unitdir}/gssproxy.service
%{_userunitdir}/gssuserproxy.service
%{_userunitdir}/gssuserproxy.socket
%{_sbindir}/gssproxy
%dir %{pubconfpath}
%dir %{gpstatedir}
%dir %{gpstatedir}/clients
%dir %{gpstatedir}/rcache
%config(noreplace) %{_sysconfdir}/gssproxy/gssproxy.conf
%config(noreplace) %{_sysconfdir}/gssproxy/99-network-fs-clients.conf
%config(noreplace) %{_sysconfdir}/gss/mech.d/proxymech.conf
%dir %{_libdir}/gssproxy
%{_libdir}/gssproxy/proxymech.so

%changelog
%autochangelog
