# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           mdadm
Version:        4.4
Release:        %autorelease
Summary:        The mdadm program controls Linux md devices (software RAID arrays)
License:        GPL-2.0-or-later
URL:            http://www.kernel.org/pub/linux/utils/raid/mdadm/
VCS:            git:https://git.kernel.org/pub/scm/utils/mdadm/mdadm.git/
#!RemoteAsset
Source0:        https://git.kernel.org/pub/scm/utils/mdadm/mdadm.git/snapshot/mdadm-%{version}.tar.gz
Source1:        raid-check
Source2:        mdadm-raid-check.sysconfig
Source3:        mdmonitor.service
Source4:        mdadm.tmpfiles
Source5:        raid-check.service
Source6:        raid-check.timer
BuildSystem:    autotools

# include xmalloc to build successfully.
Patch0:         0001-fix-missing-xmalloc-include.patch

BuildOption(build):  CXFLAGS="%{optflags} -std=gnu17 -Wno-error=unterminated-string-initialization"
BuildOption(build):  SYSCONFDIR="%{_sysconfdir}"
BuildOption(build):  mdadm mdmon raid6check raid6check.man

BuildOption(install):  MANDIR=%{_mandir}
BuildOption(install):  BINDIR=%{_sbindir}
BuildOption(install):  SYSTEMD_DIR=%{_unitdir}
BuildOption(install):  UDEVDIR=%{_prefix}/lib/udev/
BuildOption(install):  install install-systemd

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  binutils-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  mandoc

Requires(post):   coreutils
Requires(postun): coreutils

%description
The mdadm program is used to create, manage, and monitor Linux MD (software
RAID) devices.

# No configure.
%conf

%install -a
install -Dp -m 755 %{SOURCE1} %{buildroot}%{_sbindir}/raid-check
install -Dp -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/raid-check
mkdir -p -m 755 %{buildroot}%{_datadir}/%{name}

install -Dm644 %{SOURCE3} %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE6} %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE5} %{buildroot}%{_unitdir}

install -Dm 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p -m 0710 %{buildroot}/run/%{name}

install -Dm755 raid6check %{buildroot}/%{_sbindir}/raid6check
install -Dm644 raid6check.man %{buildroot}/%{_mandir}/man8/raid6check.man

%post
%systemd_post mdmonitor.service raid-check.timer

%preun
%systemd_preun mdmonitor.service raid-check.timer

%postun
%systemd_postun_with_restart mdmonitor.service

%files
%license COPYING
%doc misc/*
%{_udevrulesdir}/*-md-*
%{_sbindir}/mdadm
%{_sbindir}/mdmon
%{_sbindir}/raid-check
%{_sbindir}/raid6check
%{_unitdir}/md*
%{_unitdir}/raid-check.*
%{_mandir}/man*/md*
%{_mandir}/man8/raid6check*
%{_prefix}/lib/systemd/system-shutdown/mdadm.shutdown
%config(noreplace) %{_sysconfdir}/sysconfig/raid-check
%dir %{_rundir}/mdadm/
%config(noreplace) %{_tmpfilesdir}/mdadm.conf
%{_datadir}/mdadm/

%changelog
%autochangelog
