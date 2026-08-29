# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-grpc-prometheus
%define go_import_path  github.com/grpc-ecosystem/go-grpc-prometheus

Name:           go-github-grpc-ecosystem-go-grpc-prometheus
Version:        1.2.0
Release:        %autorelease
Summary:        Prometheus monitoring for gRPC servers
License:        Apache-2.0
URL:            https://github.com/grpc-ecosystem/go-grpc-prometheus
#!RemoteAsset:  sha256:eba66530952a126ab869205bdb909af607bfd9eb09f00207b62eb29140258aa9
Source0:        https://github.com/grpc-ecosystem/go-grpc-prometheus/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)

Provides:       go(github.com/grpc-ecosystem/go-grpc-prometheus) = %{version}

Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)

%description
go-grpc-prometheus provides Prometheus metrics interceptors for gRPC servers.

%prep -a
# This legacy package's root test uses a Prometheus API removed from the
# packaged version. The library itself does not import test or example code.
find . -maxdepth 1 -mindepth 1 -type d -exec rm -rf {} +
rm -f *_test.go

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
