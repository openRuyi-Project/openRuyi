# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           datadog-go
%define go_import_path  github.com/DataDog/datadog-go

Name:           go-github-datadog-datadog-go
Version:        3.2.0
Release:        %autorelease
Summary:        Go DogStatsD client library for Datadog
License:        MIT
URL:            https://github.com/DataDog/datadog-go
#!RemoteAsset:  sha256:0bcedc94ee42e08997a53753a091ff3465f87cd9c156a59d0516b0f6bfbd2eb1
Source0:        https://github.com/DataDog/datadog-go/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/DataDog/datadog-go) = %{version}

%description
This package provides the legacy, pre-v5 github.com/DataDog/datadog-go
import path required by packages that depend on
github.com/DataDog/datadog-go v3.x+incompatible.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
