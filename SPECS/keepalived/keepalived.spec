# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond snmp 0
%bcond vrrp 1
%bcond sha1 1
%bcond json 1
%bcond nftables 1
%bcond profile 1
%bcond debug 1

Name:           keepalived
Version:        2.2.8
Release:        %autorelease
Summary:        High Availability monitor for LVS and VRRP
License:        GPL-2.0-or-later
URL:            http://www.keepalived.org/
VCS:            git:https://github.com/acassen/keepalived
#!RemoteAsset
Source0:        http://www.keepalived.org/software/keepalived-%{version}.tar.gz
Source1:        keepalived.service
BuildSystem:    autotools

%if %{with debug}
BuildOption(conf):  --enable-debug
%endif
%if %{with profile}
BuildOption(conf):  --enable-profile
%endif
%if %{without vrrp}
BuildOption(conf):  --disable-vrrp
%endif
%if %{with snmp}
BuildOption(conf):  --enable-snmp --enable-snmp-rfc
%endif
%if %{with nftables}
BuildOption(conf):  --enable-nftables --disable-iptables
%endif
%if %{with json}
BuildOption(conf):  --enable-json
%endif
%if %{with sha1}
BuildOption(conf):  --enable-sha1
%endif
BuildOption(conf):  --with-init=systemd
BuildOption(build):  STRIP=/bin/true

%if %{with snmp}
BuildRequires:  pkgconfig(netsnmp)
%endif
%if %{with nftables}
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnftnl)
%else
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(xtables)
%endif
BuildRequires:  gcc
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnfnetlink)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  make

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
Keepalived provides simple and robust facilities for load balancing
and high availability to Linux systems. It implements a set of checkers to
dynamically manage a load-balanced server pool according to their health,
and uses the VRRP protocol for high availability.

%install -a
rm -rf %{buildroot}%{_initrddir}/
rm -rf %{buildroot}%{_sysconfdir}/keepalived/samples/
mv %{buildroot}%{_sysconfdir}/keepalived/keepalived.conf.sample \
   %{buildroot}%{_sysconfdir}/keepalived/keepalived.conf
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/keepalived.service
mkdir -p %{buildroot}%{_libexecdir}/keepalived

%post
%systemd_post keepalived.service

%preun
%systemd_preun keepalived.service

%postun
%systemd_postun_with_restart keepalived.service

%files
%license COPYING
%doc AUTHOR ChangeLog CONTRIBUTORS TODO
%{_docdir}/%{name}/README
%doc doc/keepalived.conf.SYNOPSIS doc/samples/keepalived.conf.*
%attr(0755,root,root) %{_sbindir}/keepalived
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/sysconfig/keepalived
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/keepalived/keepalived.conf
%dir %{_sysconfdir}/keepalived/
%dir %{_libexecdir}/keepalived/
%if %{with snmp}
%{_datadir}/snmp/mibs/KEEPALIVED-MIB.txt
%{_datadir}/snmp/mibs/VRRP-MIB.txt
%{_datadir}/snmp/mibs/VRRPv3-MIB.txt
%endif
%{_bindir}/genhash
%{_unitdir}/keepalived.service
%{_mandir}/man1/genhash.1*
%{_mandir}/man5/keepalived.conf.5*
%{_mandir}/man8/keepalived.8*

%changelog
%autochangelog
