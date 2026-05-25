# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           automemlimit
%define go_import_path  github.com/KimMachineGun/automemlimit

Name:           go-github-kimmachinegun-automemlimit
Version:        0.7.5~pre1
Release:        %autorelease
Summary:        Automatically set GOMEMLIMIT to match Linux cgroups(7) memory limit.
License:        MIT
URL:            https://github.com/KimMachineGun/automemlimit
#!RemoteAsset:  sha256:04f1613b446078c48519dd5be4791ce95b68026d2222844fb0b25ba84a2d549a
Source0:        https://github.com/KimMachineGun/automemlimit/archive/refs/tags/v0.7.5-pre.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n automemlimit-0.7.5-pre.1
# OBS builders do not expose a normal process cgroup layout; this test
# observes "process is not in cgroup" instead of upstream's expected
# "cgroups is not supported on this system".
BuildOption(check):  -skip TestSetGoMemLimit
# Nested Go modules have their own module path/dependencies; skip them in %check
# so the parent package does not try to test unrelated internal tools.
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/examples/dynamic*
    %{go_import_path}/examples/logger*
    %{go_import_path}/examples/system*
}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pbnjay/memory)

Provides:       go(github.com/KimMachineGun/automemlimit) = %{version}
Provides:       go(github.com/KimMachineGun/automemlimit/memlimit) = %{version}

Requires:       go(github.com/pbnjay/memory)


%description
automemlimit

[Image: Go Reference]
(https://pkg.go.dev/badge/github.com/KimMachineGun/automemlimit.svg)
(https://pkg.go.dev/github.com/KimMachineGun/automemlimit) [Image: Go
Report Card]
(https://goreportcard.com/badge/github.com/KimMachineGun/automemlimit)
(https://goreportcard.com/report/github.com/KimMachineGun/automemlimit)
[Image: Test]
(https://github.com/KimMachineGun/automemlimit/actions/workflows/test.
yml/badge.svg?branch=main)

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let this module own
# their source directories, otherwise RPM can hit file conflicts.
%exclude %{go_sys_gopath}/%{go_import_path}/examples/dynamic
%exclude %{go_sys_gopath}/%{go_import_path}/examples/logger
%exclude %{go_sys_gopath}/%{go_import_path}/examples/system

%changelog
%autochangelog
