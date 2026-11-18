# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openntpd
Version:        7.9p1
Release:        %autorelease
Summary:        OpenNTPD portable version - a lightweight NTP server
License:        ISC
URL:            https://www.openntpd.org/
VCS:            git:https://github.com/openntpd-portable/openntpd-portable.git
#!RemoteAsset:  sha256:091eeb3f4e358e28c3ab2ea58f93d7a0b5758a20d7c8a0418e162e9b2c27addc
Source0:        https://cdn.openbsd.org/pub/OpenBSD/OpenNTPD/%{name}-%{version}.tar.gz
BuildSystem:    autotools

%description
OpenNTPD is a Unix system daemon implementing the Network Time
Protocol to synchronize the local clock of a computer system with
remote NTP servers. It is also able to act as an NTP server to
NTP-compatible clients.

%files
%doc ChangeLog README.md
%license COPYING
%config(noreplace) %{_sysconfdir}/ntpd.conf
%{_sbindir}/ntpctl
%{_sbindir}/ntpd
%{_mandir}/man5/ntpd.conf.5*
%{_mandir}/man8/ntp*.8*

%changelog
%autochangelog
