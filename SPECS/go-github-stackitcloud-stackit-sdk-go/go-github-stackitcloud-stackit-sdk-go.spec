# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stackit-sdk-go
%define go_import_path  github.com/stackitcloud/stackit-sdk-go
# These stale examples import services removed from this repository snapshot;
# all core and service modules and the remaining examples are tested.
%define go_test_exclude %{shrink:
    %{go_import_path}/examples/configuration
    %{go_import_path}/examples/middleware
}

Name:           go-github-stackitcloud-stackit-sdk-go
Version:        0.26.0
Release:        %autorelease
Summary:        Go SDK for STACKIT services
License:        Apache-2.0
URL:            https://github.com/stackitcloud/stackit-sdk-go
#!RemoteAsset:  sha256:6b03852a5275ab76521d9a367a895a6eaa16847115e845ef6ea2dc1ae3127fec
Source0:        https://github.com/stackitcloud/stackit-sdk-go/archive/refs/tags/core/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/stackitcloud/stackit-sdk-go/core) = %{version}

Requires:       go(github.com/golang-jwt/jwt/v5)
Requires:       go(github.com/google/uuid)
Requires:       go(gopkg.in/yaml.v3)

%description
This package bundles the STACKIT SDK core and all service modules from one
repository snapshot.

%prep
%autosetup -n %{_name}-core-v%{version}

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
