# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ulogd
Version:        2.0.9
Release:        %autorelease
Summary:        Userspace logging daemon for Netfilter
License:        GPL-2.0-only
URL:            https://netfilter.org/projects/ulogd/
VCS:            git:https://git.netfilter.org/ulogd2
#!RemoteAsset:  sha256:523a651fe0a9f25b0cd87d5d35fc37d9382e7eecfcf61e48d5505ff3cf80eda5
Source0:        %{url}/files/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnetfilter_acct)
BuildRequires:  pkgconfig(libnetfilter_conntrack)
BuildRequires:  pkgconfig(libnetfilter_log)
BuildRequires:  pkgconfig(libnfnetlink)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

%description
ulogd is a userspace logging daemon for netfilter/iptables related
logging. This includes per-packet logging of security violations,
per-packet logging for accounting purpose as well as per-flow
logging.

%install -a
install -Dpm0644 ulogd.conf %{buildroot}%{_sysconfdir}/ulogd.conf

%files
%doc AUTHORS README
%license COPYING
%config(noreplace) %{_sysconfdir}/ulogd.conf
%{_sbindir}/ulogd
%{_libdir}/%{name}/
%{_mandir}/man*/*

%changelog
%autochangelog
