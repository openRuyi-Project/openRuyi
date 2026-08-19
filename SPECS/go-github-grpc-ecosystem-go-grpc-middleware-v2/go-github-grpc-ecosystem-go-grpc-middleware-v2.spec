# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-grpc-middleware
%define go_import_path  github.com/grpc-ecosystem/go-grpc-middleware/v2
# Examples and optional protovalidate adapters require separately packaged ecosystems.
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/examples*
    %{go_import_path}/interceptors/logging/examples*
    %{go_import_path}/interceptors/protovalidate*
    %{go_import_path}/testing/testvalidate*
}

Name:           go-github-grpc-ecosystem-go-grpc-middleware-v2
Version:        2.3.3
Release:        %autorelease
Summary:        Collection of gRPC middleware interceptors for Go
License:        Apache-2.0
URL:            https://github.com/grpc-ecosystem/go-grpc-middleware
#!RemoteAsset:  sha256:653cae72dbba078a04eb6eda0e8b330b3832a5794af28829c32a965aa26a29d0
Source0:        https://github.com/grpc-ecosystem/go-grpc-middleware/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/oauth2/google)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2) = %{version}

Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/oauth2/google)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(google.golang.org/protobuf)

%description
Go gRPC middleware interceptors for authentication, logging, retrying, and
other common RPC concerns.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
