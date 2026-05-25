# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wazero
%define go_import_path  github.com/tetratelabs/wazero
# OBS filesystem returns EEXIST instead of ENOTEMPTY for rename-over-nonempty-dir
# cases in internal/sysfs tests; the rest of the package test suite still runs.
# internal/integration_test/engine TestMemoryLeak panics with "cannot allocate
# memory" in the CI build VM - HNO3Miracle
%define go_test_exclude %{shrink:
    github.com/tetratelabs/wazero/internal/integration_test/engine
    github.com/tetratelabs/wazero/internal/sysfs
}

Name:           go-github-tetratelabs-wazero
Version:        1.11.0
Release:        %autorelease
Summary:        Zero dependency WebAssembly runtime for Go developers
License:        Apache-2.0
URL:            https://github.com/tetratelabs/wazero
#!RemoteAsset:  sha256:a785f0eabe510e454a01e0d187675a913f96814d0c7e38c4717e03f6d5420ed4
Source0:        https://github.com/tetratelabs/wazero/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/tetratelabs/wazero) = %{version}

Requires:       go(golang.org/x/sys)

%description
Wazero is a zero-dependency WebAssembly runtime for Go developers.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%license NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
