# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           numcpus
%define go_import_path  github.com/tklauser/numcpus
# Tests fail in container with cpu limit on riscv64 - Julian
%define go_test_ignore_failure 1

Name:           go-github-tklauser-go-numcpus
Version:        0.11.0
Release:        %autorelease
Summary:        Go package providing information about the number of CPUs in the system
License:        Apache-2.0
URL:            https://github.com/tklauser/numcpus
#!RemoteAsset
Source0:        https://github.com/tklauser/numcpus/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/tklauser/numcpus) = %{version}

%description
Package numcpus provides information about the number of CPUs in the
system.

It gets the number of CPUs (online, offline, present, possible,
configured or kernel maximum) on Linux, Darwin, FreeBSD, NetBSD,
OpenBSD, DragonflyBSD or Solaris/Illumos systems.

On Linux, the information is retrieved by reading the corresponding CPU
topology files in /sys/devices/system/cpu.

On BSD systems, the information is retrieved using the hw.ncpu and
hw.ncpuonline sysctls, if supported.

Not all functions are supported on Darwin, FreeBSD, NetBSD, OpenBSD,
DragonflyBSD and Solaris/Illumos. ErrNotSupported is returned in case a
function is not supported on a particular platform.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
