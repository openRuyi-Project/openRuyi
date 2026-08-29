# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _copts -DHAVE_DBUS -DHAVE_LIBIDN2 -DHAVE_DNSSEC -DHAVE_CONNTRACK -DHAVE_NFTSET

Name:           dnsmasq
Version:        2.92
Release:        %autorelease
Summary:        A lightweight DHCP/caching DNS server
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://thekelleys.org.uk/dnsmasq/
VCS:            git:http://thekelleys.org.uk/git/dnsmasq.git
#!RemoteAsset:  sha256:4bf50c2c1018f9fbc26037df51b90ecea0cb73d46162846763b92df0d6c3a458
Source0:        https://thekelleys.org.uk/dnsmasq/dnsmasq-%{version}.tar.xz
Source2:        dnsmasq.service
Source3:        dnsmasq.sysusers
BuildSystem:    autotools

BuildOption(build):  PREFIX=%{_prefix}
BuildOption(build):  CFLAGS="%{optflags}"
BuildOption(build):  LDFLAGS="%{?build_ldflags}"
BuildOption(build):  COPTS="%{_copts}"
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  CFLAGS="%{optflags}"
BuildOption(install):  LDFLAGS="%{?build_ldflags}"
BuildOption(install):  COPTS="%{_copts}"
BuildOption(install):  BINDIR="%{_bindir}"

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libnetfilter_conntrack)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(libnftables)
BuildRequires:  pkgconfig(systemd)

Provides:       dnsmasq-utils

Requires:       nettle

%{?systemd_requires}

%description
Dnsmasq provides network infrastructure for small networks: DNS, DHCP, router
advertisement and network boot. It is designed to be lightweight and have a small
footprint, suitable for resource constrained routers and firewalls.
It has also been widely used for tethering on smartphones and portable hotspots,
and to support virtual networking in virtualisation frameworks.

%prep -a
# use /var/lib/dnsmasq instead of /var/lib/misc
for file in dnsmasq.conf.example man/dnsmasq.8 man/es/dnsmasq.8 src/config.h; do
    sed -i 's|/var/lib/misc/dnsmasq.leases|/var/lib/dnsmasq/dnsmasq.leases|g' "$file"
done

#set default user /group in src/config.h
sed -i 's|#define CHUSER "nobody"|#define CHUSER "dnsmasq"|' src/config.h
sed -i 's|#define CHGRP "dip"|#define CHGRP "dnsmasq"|' src/config.h
sed -i "s|\(#\s*define RUNFILE\) \"/var/run/dnsmasq.pid\"|\1 \"%{_rundir}/dnsmasq.pid\"|" src/config.h

%conf

%build -a
%make_build -C contrib/lease-tools CFLAGS="%{optflags}" LDFLAGS="%{?build_ldflags}" COPTS="%{_copts}"

%install -a
mkdir -p %{buildroot}%{_var}/lib/dnsmasq \
        %{buildroot}%{_sysconfdir}/dnsmasq.d \
        %{buildroot}%{_datadir}/dbus-1/system.d
install -p -m 0644 dnsmasq.conf.example %{buildroot}%{_sysconfdir}/dnsmasq.conf
install -p -m 0644 dbus/dnsmasq.conf %{buildroot}%{_datadir}/dbus-1/system.d/
install -p -D -m 0644 trust-anchors.conf %{buildroot}%{_datadir}/%{name}/trust-anchors.conf

# utils sub package
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_mandir}/man1
install -p -m 755 contrib/lease-tools/dhcp_release %{buildroot}%{_bindir}/dhcp_release
install -p -m 644 contrib/lease-tools/dhcp_release.1 %{buildroot}%{_mandir}/man1/dhcp_release.1
install -p -m 755 contrib/lease-tools/dhcp_release6 %{buildroot}%{_bindir}/dhcp_release6
install -p -m 644 contrib/lease-tools/dhcp_release6.1 %{buildroot}%{_mandir}/man1/dhcp_release6.1
install -p -m 755 contrib/lease-tools/dhcp_lease_time %{buildroot}%{_bindir}/dhcp_lease_time
install -p -m 644 contrib/lease-tools/dhcp_lease_time.1 %{buildroot}%{_mandir}/man1/dhcp_lease_time.1

# Systemd
mkdir -p %{buildroot}%{_unitdir}
install -p -m644 %{SOURCE2} %{buildroot}%{_unitdir}

#install systemd sysuser file
install -p -Dpm 644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf

# no tests.
%check

%pre
%sysusers_create_package %{name} %{SOURCE3}

%post
%systemd_post dnsmasq.service

%preun
%systemd_preun dnsmasq.service

%postun
%systemd_postun_with_restart dnsmasq.service

%files
%license COPYING COPYING-v3
%doc CHANGELOG FAQ doc.html setup.html dbus/DBus-interface
%config(noreplace) %{_sysconfdir}/dnsmasq.conf
%dir %{_sysconfdir}/dnsmasq.d
%dir %attr(0755,root,dnsmasq) %{_var}/lib/dnsmasq
%{_datadir}/dbus-1/system.d/dnsmasq.conf
%{_bindir}/dhcp_*
%{_bindir}/dnsmasq
%{_unitdir}/%{name}.service
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/trust-anchors.conf
%{_sysusersdir}/dnsmasq.conf
%{_mandir}/man1/dhcp_*
%{_mandir}/man8/dnsmasq*

%changelog
%autochangelog
