# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global gitname     IPMITOOL
%global gitversion  1_8_19

Name:           ipmitool
Version:        1.8.19
Release:        %autorelease
Summary:        Utility for IPMI control
License:        BSD-3-Clause
URL:            https://github.com/ipmitool/ipmitool
#!RemoteAsset
Source0:        https://github.com/ipmitool/ipmitool/archive/refs/tags/IPMITOOL_%{gitversion}.tar.gz
Source1:        ipmievd.sysconf
Source2:        ipmievd.service
BuildSystem:    autotools

# disable download file from net.
Patch0:         0001-disable-download-file.patch

BuildOption(conf):  --disable-dependency-tracking
BuildOption(conf):  --enable-file-security
BuildOption(conf):  --disable-intf-free
BuildOption(conf):  --enable-intf-usb

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  curl
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros

%description
This package contains a utility for interfacing with devices that support
the Intelligent Platform Management Interface specification.

%package     -n bmc-snmp-proxy
Summary:        Reconfigure SNMP to include host SNMP agent within BMC
# Requires:       net-snmp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n bmc-snmp-proxy
Extend system configuration of net-snmp to include redirections to BMC based SNMP.

%prep -a
for f in AUTHORS ChangeLog; do
    iconv -f iso-8859-1 -t utf8 < ${f} > ${f}.utf8
    mv ${f}.utf8 ${f}
done

%conf -p
autoreconf -fiv

%install -a
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/ipmievd.service
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/ipmievd

install -D -m 0644 contrib/exchange-bmc-os-info.service.redhat %{buildroot}%{_unitdir}/exchange-bmc-os-info.service
install -D -m 0644 contrib/exchange-bmc-os-info.sysconf %{buildroot}/%{_sysconfdir}/sysconfig/exchange-bmc-os-info

install -Dm 644 contrib/bmc-snmp-proxy.sysconf %{buildroot}%{_sysconfdir}/sysconfig/bmc-snmp-proxy
install -Dm 644 contrib/bmc-snmp-proxy.service %{buildroot}%{_unitdir}/bmc-snmp-proxy.service
install -Dm 755 contrib/bmc-snmp-proxy         %{buildroot}%{_libexecdir}/bmc-snmp-proxy

rm -f %{buildroot}%{_datadir}/misc/enterprise-numbers

%post
%systemd_post exchange-bmc-os-info.service ipmievd.service

%preun
%systemd_preun exchange-bmc-os-info.service ipmievd.service

%postun
%systemd_postun_with_restart exchange-bmc-os-info.service ipmievd.service

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_docdir}/ipmitool/COPYING
%{_bindir}/ipmitool
%{_mandir}/man1/ipmitool.1*
%{_datadir}/ipmitool/
%config(noreplace) %{_sysconfdir}/sysconfig/ipmievd
%{_unitdir}/ipmievd.service
%{_sbindir}/ipmievd
%{_mandir}/man8/ipmievd.8*
%config(noreplace) %{_sysconfdir}/sysconfig/exchange-bmc-os-info
%{_unitdir}/exchange-bmc-os-info.service

%files -n bmc-snmp-proxy
%config(noreplace) %{_sysconfdir}/sysconfig/bmc-snmp-proxy
%{_unitdir}/bmc-snmp-proxy.service
%{_libexecdir}/bmc-snmp-proxy

%changelog
%autochangelog
