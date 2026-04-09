# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           client_model
%define go_import_path  github.com/prometheus/client_model

Name:           go-github-prometheus-client-model
Version:        0.6.2
Release:        %autorelease
Summary:        Data model artifacts for Prometheus.
License:        Apache-2.0
URL:            https://github.com/prometheus/client_model
#!RemoteAsset
Source0:        https://github.com/prometheus/client_model/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/prometheus/client_model) = %{version}

Requires:       go(google.golang.org/protobuf)

%description
Golang data model artifacts for Prometheus.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
