# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gopsutil
%define go_import_path  github.com/shirou/gopsutil/v3
# CPU per-core counts and swap devices are not stable in the OBS container. - HNO3Miracle
%define go_test_exclude %{shrink:
    github.com/shirou/gopsutil/v3/cpu
    github.com/shirou/gopsutil/v3/mem
}

Name:           go-github-shirou-gopsutil-v3
Version:        3.22.12
Release:        %autorelease
Summary:        System and process utilities for Go
License:        BSD-3-Clause
URL:            https://github.com/shirou/gopsutil
#!RemoteAsset:  sha256:39bedcb6d755a19df45657cc44dd6a1bf5f4c2727017dc19db4091db2b5c06d6
Source0:        https://github.com/shirou/gopsutil/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/lufia/plan9stats)
BuildRequires:  go(github.com/power-devops/perfstat)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/yusufpapurcu/wmi)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  procps-ng

Provides:       go(github.com/shirou/gopsutil/v3) = %{version}

Requires:       go(github.com/lufia/plan9stats)
Requires:       go(github.com/power-devops/perfstat)
Requires:       go(github.com/tklauser/go-sysconf)
Requires:       go(github.com/yusufpapurcu/wmi)
Requires:       go(golang.org/x/sys)

%description
Gopsutil provides Go interfaces for retrieving system and process information
on multiple operating systems.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
