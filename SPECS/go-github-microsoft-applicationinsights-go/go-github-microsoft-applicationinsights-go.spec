# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ApplicationInsights-Go
%define go_import_path  github.com/microsoft/ApplicationInsights-Go

Name:           go-github-microsoft-applicationinsights-go
Version:        0.4.4
Release:        %autorelease
Summary:        Application Insights SDK for Go
License:        MIT
URL:            https://github.com/microsoft/ApplicationInsights-Go
#!RemoteAsset:  sha256:29573b7dc96fc14934bed2a87efc643f3f1c724d11041ada1c8b53075aba6e58
Source0:        https://github.com/microsoft/ApplicationInsights-Go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(code.cloudfoundry.org/clock)
BuildRequires:  go(github.com/gofrs/uuid)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/onsi/ginkgo)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/tedsuo/ifrit)
BuildRequires:  go(gopkg.in/check.v1)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(code.cloudfoundry.org/clock)
Requires:       go(github.com/gofrs/uuid)

%description
ApplicationInsights-Go provides a Go SDK for sending event, metric, trace, and
request telemetry to Microsoft Application Insights.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
