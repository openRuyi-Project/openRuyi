# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iotop
Version:        1.30
Release:        %autorelease
Summary:        Simple top-like I/O monitor (implemented in C)
License:        GPL-2.0-or-later
URL:            https://github.com/Tomas-M/iotop
#!RemoteAsset
Source:         https://github.com/Tomas-M/iotop/releases/download/v%{version}/iotop-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(build):  NO_FLTO=1
BuildOption(install):  V=1 STRIP=: BINDIR=$RPM_BUILD_ROOT%{_bindir}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)

%description
iotop does for I/O usage what top(1) does for CPU usage. It watches I/O
usage information output by the Linux kernel and displays a table of
current I/O usage by processes on the system. It is handy for answering
the question "Why is the disk churning so much?".

iotop requires a Linux kernel built with the CONFIG_TASKSTATS,
CONFIG_TASK_DELAY_ACCT, CONFIG_TASK_IO_ACCOUNTING and
CONFIG_VM_EVENT_COUNTERS config options on.

iotop is an alternative re-implementation of iotop in C, optimized for
performance. Normally a monitoring tool intended to be used on a system
under heavy stress should use the least additional resources as
possible.

# no configure script
%conf

# No tests.
%check

%files
%license COPYING
%license LICENSE
%{_bindir}/iotop
%{_mandir}/man8/iotop.8*

%changelog
%autochangelog
