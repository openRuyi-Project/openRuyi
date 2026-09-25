# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gopsutil
%define go_import_path  github.com/shirou/gopsutil
# Keep the unversioned import path on the last release that exports it. The
# release archive also contains the independently packaged /v3 module.
# CPU, memory, process, and sensor tests depend on OBS worker host state.
%define go_test_exclude %{shrink:
    %{go_import_path}/cpu
    %{go_import_path}/mem
    %{go_import_path}/process
    %{go_import_path}/sensors
}
%define go_test_exclude_glob %{go_import_path}/v3*

Name:           go-github-shirou-gopsutil
Version:        3.21.11
Release:        %autorelease
Summary:        System and process utilities for Go
License:        BSD-3-Clause
URL:            https://github.com/shirou/gopsutil
#!RemoteAsset:  sha256:cb6fcdf8faece3e584604d6293a4b7e09fd5259a806174eded2fb90a3042c227
Source0:        https://github.com/shirou/gopsutil/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/process) = %{version}

Requires:       go(github.com/tklauser/go-sysconf)
Requires:       go(golang.org/x/sys)

%description
Gopsutil provides Go interfaces for retrieving system and process information
on multiple operating systems. This package preserves the unversioned import
path used before upstream migrated to semantic import versioning.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/v3

%changelog
%autochangelog
