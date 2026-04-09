# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: kenlig <qiming.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           irqbalance
Version:        1.9.5
Release:        %autorelease
Summary:        IRQ balancing daemon
License:        GPL-2.0-only
URL:            https://github.com/Irqbalance/irqbalance
#!RemoteAsset
Source0:        %{url}/archive/v%{version}/irqbalance-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libcap-ng
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(numa)

Requires:       numactl

%description
irqbalance is a daemon that evenly distributes IRQ load across
multiple CPUs for enhanced performance.

%conf -p
# Otherwise configure will not happy - 251
./autogen.sh

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mv %{buildroot}/usr/etc/default/irqbalance.env %{buildroot}%{_sysconfdir}/sysconfig/irqbalance
rm -rf %{buildroot}/usr/etc
sed -i 's|/usr/etc/default/irqbalance.env|/etc/sysconfig/irqbalance|g' %{buildroot}%{_unitdir}/irqbalance.service

%post
%systemd_post irqbalance.service

%preun
%systemd_preun irqbalance.service

%postun
%systemd_postun_with_restart irqbalance.service

%files
%doc COPYING AUTHORS
%{_sbindir}/irqbalance
%{_unitdir}/irqbalance.service
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/sysconfig/irqbalance
# Should we include this? - 251
%exclude %{_sbindir}/irqbalance-ui

%changelog
%autochangelog
