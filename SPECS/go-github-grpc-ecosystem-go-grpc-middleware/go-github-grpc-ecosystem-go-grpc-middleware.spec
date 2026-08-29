# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-grpc-middleware
%define go_import_path  github.com/grpc-ecosystem/go-grpc-middleware

Name:           go-github-grpc-ecosystem-go-grpc-middleware
Version:        1.3.0
Release:        %autorelease
Summary:        gRPC middleware for Go
License:        Apache-2.0
URL:            https://github.com/grpc-ecosystem/go-grpc-middleware
#!RemoteAsset:  sha256:c9b908202c05a7f821b03ee49cd678e7e71469519054629770e0565d78275cbc
Source0:        https://github.com/grpc-ecosystem/go-grpc-middleware/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)

Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware) = %{version}

Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)

%description
go-grpc-middleware provides reusable server and client middleware for gRPC
applications.

%prep -a
# containerd uses only the root interceptor-chain API. Remove optional
# middleware implementations and their unrelated dependency closure.
find . -maxdepth 1 -mindepth 1 -type d -exec rm -rf {} +

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
