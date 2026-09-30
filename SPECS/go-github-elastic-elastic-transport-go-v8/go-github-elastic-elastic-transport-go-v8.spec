# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           elastic-transport-go
%define go_import_path  github.com/elastic/elastic-transport-go/v8

Name:           go-github-elastic-elastic-transport-go-v8
Version:        8.11.0
Release:        %autorelease
Summary:        Transport library for Elastic Go clients
License:        Apache-2.0
URL:            https://github.com/elastic/elastic-transport-go
#!RemoteAsset:  sha256:6bdc405fb40962bad70b561f94c87ddaf7db5239728617614d31f58a901439eb
Source0:        https://github.com/elastic/elastic-transport-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(go.opentelemetry.io/otel)

%description
Elastic Transport provides the HTTP transport interface, connection pooling,
cluster discovery, instrumentation, and logging used by Elastic Go clients.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
