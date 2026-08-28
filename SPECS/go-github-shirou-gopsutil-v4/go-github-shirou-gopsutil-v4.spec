# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gopsutil
%define go_import_path  github.com/shirou/gopsutil/v4
# These tests require host CPU, mount, swap, and sensor state unavailable in OBS workers.
%define go_test_exclude %{shrink:
    %{go_import_path}/cpu
    %{go_import_path}/disk
    %{go_import_path}/mem
    %{go_import_path}/sensors
}

Name:           go-github-shirou-gopsutil-v4
Version:        4.26.7
Release:        %autorelease
Summary:        Cross-platform system information library for Go
License:        BSD-3-Clause
URL:            https://github.com/shirou/gopsutil
#!RemoteAsset:  sha256:cd5d9632eaaccd86cf298eaddf59ced34cd9df5dfb01b9086857213f6538204a
Source0:        https://github.com/shirou/gopsutil/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/ebitengine/purego)
BuildRequires:  go(github.com/go-ole/go-ole)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/lufia/plan9stats)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/power-devops/perfstat)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/tklauser/numcpus)
BuildRequires:  go(github.com/yusufpapurcu/wmi)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/ebitengine/purego)
Requires:       go(github.com/lufia/plan9stats)
Requires:       go(github.com/power-devops/perfstat)
Requires:       go(github.com/tklauser/go-sysconf)
Requires:       go(github.com/yusufpapurcu/wmi)
Requires:       go(golang.org/x/sys)

%description
Gopsutil retrieves CPU, memory, process, disk, network, host, and sensor
information through a portable Go API.

%check
%buildsystem_golangmodules_check
go test -run '^$' \
    %{go_import_path}/cpu \
    %{go_import_path}/disk \
    %{go_import_path}/mem \
    %{go_import_path}/sensors

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
