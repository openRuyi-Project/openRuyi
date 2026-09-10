# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           datadog-go
%define go_import_path  github.com/DataDog/datadog-go

Name:           go-github-datadog-datadog-go
Version:        4.8.3
Release:        %autorelease
Summary:        Go DogStatsD client library for Datadog
License:        MIT
URL:            https://github.com/DataDog/datadog-go
#!RemoteAsset:  sha256:0053a6b391abda1f494b858a23575fcbdd218666dd8050249074ad3f0a1dd3b5
Source0:        https://github.com/DataDog/datadog-go/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/DataDog/datadog-go) = %{version}

Requires:       go(github.com/Microsoft/go-winio)

%description
This package provides the legacy, pre-v5 github.com/DataDog/datadog-go
import path required by packages that depend on v3 or v4 releases.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
