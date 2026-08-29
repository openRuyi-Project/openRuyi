# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           influxdb-client-go
%define go_import_path  github.com/influxdata/influxdb-client-go/v2

Name:           go-github-influxdata-influxdb-client-go-v2
Version:        2.14.0
Release:        %autorelease
Summary:        InfluxDB 2 Go client library
License:        MIT
URL:            https://github.com/influxdata/influxdb-client-go
#!RemoteAsset:  sha256:fed7f5df0f67e3b4606f2103cb920c2027ee886be2a92a6fc07b4e5d334089e4
Source0:        https://github.com/influxdata/influxdb-client-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstream internal/write/service.go misuses a go vet error-wrapping directive
# that newer go vet rejects as a build error; disable vet (tests still run).
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/influxdata/line-protocol)
BuildRequires:  go(github.com/oapi-codegen/runtime)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/influxdata/influxdb-client-go/v2) = %{version}

Requires:       go(github.com/influxdata/line-protocol)
Requires:       go(github.com/oapi-codegen/runtime)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/net)

%description
This package provides the Go client library for InfluxDB 2.x and Flux.
It includes APIs for querying data, writing data, and using the InfluxDB
2 management API from Go programs.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
