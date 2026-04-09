# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-sysconf
%define go_import_path  github.com/tklauser/go-sysconf
# Tests fail in container with cpu limit on riscv64 - Julian
%define go_test_ignore_failure 1

Name:           go-github-tklauser-go-sysconf
Version:        0.3.16
Release:        %autorelease
Summary:        sysconf for Go, without using cgo
License:        BSD-3-Clause
URL:            https://github.com/tklauser/go-sysconf
#!RemoteAsset
Source0:        https://github.com/tklauser/go-sysconf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/tklauser/numcpus)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/tklauser/go-sysconf) = %{version}

Requires:       go(github.com/tklauser/numcpus)
Requires:       go(golang.org/x/sys)

%description
sysconf for Go, without using cgo or external binaries (e.g. getconf).

Supported operating systems: Linux, macOS, DragonflyBSD, FreeBSD,
NetBSD, OpenBSD, Solaris/Illumos.

All POSIX.1 and POSIX.2 variables are supported, see References for a
complete list.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
