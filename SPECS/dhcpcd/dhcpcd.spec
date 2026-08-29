# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           dhcpcd
Version:        10.3.2
Release:        %autorelease
Summary:        A minimalistic network configuration daemon
License:        BSD-2-Clause AND ISC AND MIT
URL:            http://roy.marples.name/projects/dhcpcd/
VCS:            git:https://github.com/NetworkConfiguration/dhcpcd
#!RemoteAsset:  sha256:b6aa46932074906a9badef1bfe142b8aff9d041c2689e1ef8b74c12e9fd942bd
Source0:        https://github.com/NetworkConfiguration/dhcpcd/releases/download/v%{version}/dhcpcd-%{version}.tar.xz
Source1:        dhcpcd.service
Source2:        dhcpcd@.service
Source3:        systemd-sysusers.conf

BuildSystem:    autotools

BuildOption(conf):  --dbdir=%{_localstatedir}/lib/%{name}
BuildOption(conf):  --runstatedir=%{_rundir}

BuildRequires:  make
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros

%description
The dhcpcd package provides a minimalistic network configuration daemon
that supports IPv4, rdisc, and DHCPv6 protocols.

%install -a
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}@.service
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf
install -d %{buildroot}%{_localstatedir}/lib/%{name}

%pre
%sysusers_create_package %{name} %{SOURCE3}

%post
%systemd_post dhcpcd.service

%preun
%systemd_preun dhcpcd.service

%postun
%systemd_postun_with_restart dhcpcd.service

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/dhcpcd.conf
%dir %{_datadir}/dhcpcd
%dir %{_datadir}/dhcpcd/hooks
%{_datadir}/dhcpcd/hooks/*
%dir %{_libdir}/dhcpcd
%{_libdir}/dhcpcd/*
%{_libexecdir}/dhcpcd-hooks
%{_libexecdir}/dhcpcd-run-hooks
%{_mandir}/man5/dhcpcd.conf.5.gz
%{_mandir}/man8/dhcpcd-run-hooks.8.gz
%{_mandir}/man8/dhcpcd.8.gz
%{_sbindir}/dhcpcd
%{_sysusersdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%attr(0644,root,dhcpcd) %dir %{_localstatedir}/lib/%{name}

%changelog
%autochangelog
