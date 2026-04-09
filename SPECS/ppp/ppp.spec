# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ppp
Version:        2.5.2
Release:        %autorelease
Summary:        The Point-to-Point Protocol daemon
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://www.samba.org/ppp
VCS:            git:https://github.com/ppp-project/ppp.git
#!RemoteAsset
Source0:        https://github.com/ppp-project/ppp/archive/refs/tags/v%{version}.tar.gz
Source1:        ppp.pam
Source2:        ppp.logrotate
Source3:        ppp.tmpfiles
Source4:        ip-down
Source5:        ip-down.ipv6to4
Source6:        ip-up
Source7:        ip-up.ipv6to4
Source8:        ipv6-down
Source9:        ipv6-up
Source10:       ipv6-up.initscripts
Source11:       ipv6-down.initscripts
Source12:       ppp.sysusers
BuildSystem:    autotools

# update function to high version of gcc.
Patch0:         0001-ppp-2.5.1-gcc15.patch

BuildOption(conf):  --enable-systemd
BuildOption(conf):  --enable-cbcp
BuildOption(conf):  --with-pam
BuildOption(conf):  --disable-openssl-engine
BuildOption(conf):  CFLAGS="%{build_cflags} -fno-strict-aliasing"

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libxcrypt)

Requires:       glibc
Requires:       libpcap
Requires:       systemd
Requires:       pam

%description
The ppp package contains the PPP (Point-to-Point Protocol) daemon and
documentation for PPP support.

%package        devel
Summary:        Headers for ppp plugin development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files for building plugins for ppp.

%conf -p
autoreconf -fiv

%install -a
find scripts -type f -exec chmod a-x {} +

install -d %{buildroot}%{_localstatedir}/log/ppp
install -d %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/ppp
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/ppp
install -d %{buildroot}%{_tmpfilesdir}
install -m 644 -p %{SOURCE3} %{buildroot}%{_tmpfilesdir}/ppp.conf

install -d %{buildroot}%{_sysconfdir}/ppp
install -p %{SOURCE4} %{buildroot}%{_sysconfdir}/ppp/ip-down
install -p %{SOURCE5} %{buildroot}%{_sysconfdir}/ppp/ip-down.ipv6to4
install -p %{SOURCE6} %{buildroot}%{_sysconfdir}/ppp/ip-up
install -p %{SOURCE7} %{buildroot}%{_sysconfdir}/ppp/ip-up.ipv6to4
install -p %{SOURCE8} %{buildroot}%{_sysconfdir}/ppp/ipv6-down
install -p %{SOURCE9} %{buildroot}%{_sysconfdir}/ppp/ipv6-up
install -p %{SOURCE10} %{buildroot}%{_sysconfdir}/ppp/ipv6-down.initscripts
install -p %{SOURCE11} %{buildroot}%{_sysconfdir}/ppp/ipv6-up.initscripts
# mkdir -p %{buildroot}%{_sysusersdir}
install -m0644 -D %{SOURCE12} %{buildroot}%{_sysusersdir}/ppp.conf

mkdir -p %{buildroot}%{_rundir}/pppd/lock

for f in %{buildroot}%{_sysconfdir}/ppp/*.example; do
  mv "$f" "${f%%.example}"
done

%post
%tmpfiles_create ppp.conf

%files
%doc FAQ README scripts sample
%license README
%{_sbindir}/chat
%{_sbindir}/pppd
%{_sbindir}/pppdump
%{_sbindir}/pppoe-discovery
%{_sbindir}/pppstats
%{_sysconfdir}/ppp/chap-secrets
%{_sysconfdir}/ppp/pap-secrets
%dir %{_sysconfdir}/ppp
%{_sysconfdir}/ppp/ip*
%{_sysconfdir}/ppp/openssl.cnf
%{_mandir}/man8/*.8*
%{_libdir}/pppd
%ghost %dir %{_rundir}/pppd
%ghost %dir %{_rundir}/pppd/lock
%dir %{_sysconfdir}/logrotate.d
%attr(700, root, root) %dir %{_localstatedir}/log/ppp
%config(noreplace) %{_sysconfdir}/ppp/options
%config(noreplace) %{_sysconfdir}/ppp/eaptls-*
%config(noreplace) %{_sysconfdir}/pam.d/ppp
%config(noreplace) %{_sysconfdir}/logrotate.d/ppp
%{_tmpfilesdir}/ppp.conf
%{_sysusersdir}/ppp.conf

%files devel
%{_includedir}/pppd
%doc PLUGINS
%{_libdir}/pkgconfig/pppd.pc

%changelog
%autochangelog
