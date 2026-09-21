# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-grpc-middleware
%define go_import_path  github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus
%define go_source_subdir providers/prometheus

Name:           go-github-grpc-ecosystem-go-grpc-middleware-providers-prometheus
Version:        1.0.1
Release:        %autorelease
Summary:        Prometheus metrics provider for gRPC middleware
License:        Apache-2.0
URL:            https://github.com/grpc-ecosystem/go-grpc-middleware
#!RemoteAsset:  sha256:0ad685543c14b146f4d7f5b7b7ee481688d8e44299769e1ab9d642d9120b317e
Source0:        %{url}/archive/refs/tags/providers/prometheus/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware/v2)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(google.golang.org/grpc)

Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus) = %{version}

Requires:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(google.golang.org/grpc)

%description
This package provides Prometheus server-side and client-side monitoring
interceptors for gRPC applications.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
