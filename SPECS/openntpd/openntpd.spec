# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openntpd
Version:        6.8p1
Release:        %autorelease
Summary:        OpenNTPD portable version - a lightweight NTP server
License:        ISC
URL:            https://www.openntpd.org/
VCS:            git:https://github.com/openntpd-portable/openntpd-portable.git
#!RemoteAsset:  sha256:8582db838a399153d4a17f2a76518b638cc3020f58028575bf54127518f55a46
Source0:        https://ftp.openbsd.org/pub/OpenBSD/OpenNTPD/%{name}-%{version}.tar.gz
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
