# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           strace
Version:        6.18
Release:        %autorelease
Summary:        Tracks and displays system calls associated with a running process
License:        LGPL-2.1-or-later
URL:            http://strace.io/
#!RemoteAsset:  sha256:0ad5dcba973a69e779650ef1cb335b12ee60716fc7326609895bd33e6d2a7325
Source0:        https://strace.io/files/%{version}/strace-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  xz
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  libelf-devel
BuildRequires:  binutils-devel
BuildRequires:  pkgconfig(libselinux)

%description
The strace program intercepts and records the system calls called and
received by a running process.  Strace can print a record of each
system call, its arguments and its return value.  Strace is useful for
diagnosing problems and debugging, as well as for instructional
purposes.

Install strace if you need a tool to track the system calls made and
received by a process.

%files
%defattr(-,root,root)
%doc CREDITS README doc/README-linux-ptrace NEWS
%{_bindir}/strace
%{_bindir}/strace-log-merge
%{_mandir}/man1/strace.1*
%{_mandir}/man1/strace-log-merge.1*

%changelog
%{?autochangelog}
