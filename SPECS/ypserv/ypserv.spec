# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ypserv
Version:        4.2
Release:        %autorelease
Summary:        The NIS (Network Information Service) server
License:        GPL-2.0-only
URL:            https://www.thkukuk.de/nis/nis/ypserv/
VCS:            git:https://github.com/thkukuk/ypserv
#!RemoteAsset
Source0:        https://github.com/thkukuk/ypserv/archive/refs/tags/v%{version}.tar.gz
Source1:        ypserv.service
Source2:        yppasswdd.service
Source3:        ypxfrd.service
Source4:        yppasswdd
BuildSystem:    autotools

# disable gen docs.
Patch:          0001-disable-doc.patch

BuildOption(conf):  --enable-checkroot
BuildOption(conf):  --enable-fqdn
BuildOption(conf):  --libexecdir=%{_libdir}/yp
BuildOption(conf):  --with-dbmliborder=gdbm
BuildOption(conf):  --localstatedir=%{_localstatedir}
BuildOption(conf):  --with-selinux
BuildOption(conf):  CFLAGS="%{optflags} -fPIC -Wno-format-overflow"

BuildRequires:  make
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(systemd)
BuildRequires:  rpcsvc-proto-devel
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libnsl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  systemd-rpm-macros

Requires:       gawk
Requires:       bash
%{?systemd_requires}

%description
The Network Information Service (NIS) is a system that provides
network information (login names, passwords, home directories, group
information) to all of the machines on a network.

%conf -p
./autogen.sh
cp etc/README etc/README.etc

%install -a
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_libexecdir}
mkdir -p %{buildroot}/etc/sysconfig

install -m 644 etc/ypserv.conf %{buildroot}%{_sysconfdir}

install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/ypserv.service
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/yppasswdd.service
install -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/ypxfrd.service

install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/

%post
%systemd_post ypserv.service ypxfrd.service yppasswdd.service

%preun
%systemd_preun ypserv.service ypxfrd.service yppasswdd.service

%postun
%systemd_postun_with_restart ypserv.service ypxfrd.service yppasswdd.service

%files
%doc AUTHORS README INSTALL ChangeLog TODO NEWS COPYING
%doc etc/ypserv.conf etc/securenets etc/README.etc
%doc etc/netgroup etc/locale etc/netmasks etc/timezone
%config(noreplace) %{_sysconfdir}/ypserv.conf
%config(noreplace) %{_sysconfdir}/sysconfig/yppasswdd
%config(noreplace) /var/yp/*
%{_unitdir}/*
%{_libdir}/yp/*
%{_sbindir}/*
%{_includedir}/rpcsvc

%changelog
%autochangelog
