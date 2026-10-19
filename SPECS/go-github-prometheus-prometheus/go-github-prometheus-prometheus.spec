# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           prometheus
%define go_import_path  github.com/prometheus/prometheus

Name:           go-github-prometheus-prometheus
Version:        0.303.0
Release:        %autorelease
Summary:        Prometheus histogram model library
License:        Apache-2.0
URL:            https://github.com/prometheus/prometheus
#!RemoteAsset:  sha256:0d30e03d0068126d2430f9f17074ebf942def66d60598106d3a2ef99c6fcd80a
Source0:        https://github.com/prometheus/prometheus/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# MinIO uses only model/histogram through prom2json. The server and discovery
# libraries need additional unprovided modules (Docker, Alertmanager, collector
# contrib and govultr); keep this package limited to the standalone model.
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/prometheus/prometheus) = %{version}

%description
Prometheus histogram model library, used to process native histogram metrics.
This source package currently ships model/histogram and its model/value test support; Prometheus server,
storage and service discovery libraries are not included.

%prep -a
# Retain only the self-contained model required by MinIO and its unit tests.
find . -mindepth 1 -maxdepth 1 ! -name model ! -name LICENSE ! -name NOTICE ! -name README.md -exec rm -rf {} +
find model -mindepth 1 -maxdepth 1 ! -name histogram ! -name value -exec rm -rf {} +

%files
%doc README.md
%license LICENSE NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
