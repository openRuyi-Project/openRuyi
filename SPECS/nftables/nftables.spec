# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nftables
Version:        1.1.5
Release:        %autorelease
Summary:        Netfilter Tables userspace utilities
License:        GPL-2.0-only
URL:            https://netfilter.org/projects/nftables/
#!RemoteAsset
Source0:        https://netfilter.org/projects/nftables/files/nftables-%{version}.tar.xz
Source1:        nftables.service
Source2:        nftables.conf
Source3:        main.nft
Source4:        router.nft
Source5:        nat.nft
BuildSystem:    autotools

BuildOption(conf): --with-xtables
BuildOption(conf): --with-json
BuildOption(conf): --disable-manpages

BuildRequires:  flex bison gmp-devel jansson-devel python3-devel readline-devel
BuildRequires:  libedit-devel python3-setuptools make gcc python3-pip
BuildRequires:  pkgconfig(libmnl) >= 1.0.4
BuildRequires:  pkgconfig(libnftnl) >= 1.3.0
BuildRequires:  pkgconfig(xtables) >= 1.6.1
BuildRequires:  systemd-rpm-macros autoconf automake libtool

Requires:         %{name}-services = %{version}
%systemd_requires

%description
Netfilter Tables userspace utilities.

%package        devel
Summary:        Development library for nftables / libnftables
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description    devel
Headers and other development files for the libnftables library.

%package -n     python3-nftables
Summary:        Python module providing an interface to libnftables
Requires:       %{name} = %{version}
%description -n python3-nftables
The nftables python module provides an interface to libnftables via ctypes.

%package          services
Summary:          Systemd service for nftables
Requires:         %{name} = %{version}

%description  services
Systemd service for managing an nftables-based firewall.

%conf -p
autoreconf -vif

%build -a
cd py
%pyproject_wheel

%install -a
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}/%{_libdir}/libnftables.a

install -d -m 755 %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/
install -d -m 755 %{buildroot}%{_sysconfdir}/nftables
install -m 644 %{SOURCE3} %{SOURCE4} %{SOURCE5} %{buildroot}%{_sysconfdir}/nftables/

cd py
%pyproject_install
%pyproject_save_files nftables

%post services -p /bin/sh
%systemd_post nftables.service
%preun services -p /bin/sh
%systemd_preun nftables.service
%postun services -p /bin/sh
%systemd_postun_with_restart nftables.service

%files
%license COPYING
%doc %{_docdir}/nftables/examples/
%doc %{_docdir}/nftables/main.nft
%{_sbindir}/nft
%{_libdir}/libnftables.so.*
%{_mandir}/man5/libnftables-json.5*
%{_mandir}/man8/nft*
%{_datadir}/nftables/

%files devel
%{_libdir}/libnftables.so
%{_libdir}/pkgconfig/libnftables.pc
%{_includedir}/nftables/libnftables.h
%{_mandir}/man3/libnftables.3*

%files -n python3-nftables -f %{pyproject_files}

%files services
%config(noreplace) %{_sysconfdir}/nftables/
%config(noreplace) %{_sysconfdir}/sysconfig/nftables.conf
%{_unitdir}/nftables.service

%changelog
%{?autochangelog}
