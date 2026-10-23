# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-spancheck
%define go_import_path  github.com/jjti/go-spancheck

Name:           go-github-jjti-go-spancheck
Version:        0.6.5
Release:        %autorelease
Summary:        Defines a linter that checks for mistakes with OTEL trace spans
License:        MIT
URL:            https://github.com/jjti/go-spancheck
#!RemoteAsset:  sha256:9b7c649862563bcdb5db282d063a97e9d0245ea86fddaba64b2035146d75484e
Source0:        https://github.com/jjti/go-spancheck/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/jjti/go-spancheck) = %{version}

Requires:       go(golang.org/x/tools)

%description
Defines a linter that checks for mistakes with OTEL trace spans.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n go-spancheck-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/jjti/go-spancheck

%changelog
%autochangelog
