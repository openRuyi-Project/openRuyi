# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           prom2json
%define go_import_path  github.com/prometheus/prom2json

Name:           go-github-prometheus-prom2json
Version:        1.4.2
Release:        %autorelease
Summary:        Prometheus metrics to JSON conversion library
License:        Apache-2.0
URL:            https://github.com/prometheus/prom2json
#!RemoteAsset:  sha256:30b3374c8c874f78d838262db07711003f43db85cbd20faae21f7dfd15770648
Source0:        https://github.com/prometheus/prom2json/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Backport the upstream fix for a panic with prometheus/common >= 0.66.
Patch1000:      1000-initialize-prometheus-text-parser.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/matttproud/golang_protobuf_extensions)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/prometheus)

Provides:       go(github.com/prometheus/prom2json) = %{version}

Requires:       go(github.com/matttproud/golang_protobuf_extensions)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/prometheus)

%description
Go library for scraping Prometheus metrics and converting them to JSON,
including native histogram metrics.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
