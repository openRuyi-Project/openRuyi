# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ttrpc
%define go_import_path  github.com/containerd/ttrpc

Name:           go-github-containerd-ttrpc
Version:        1.2.7
Release:        %autorelease
Summary:        Low-memory gRPC implementation
License:        Apache-2.0
URL:            https://github.com/containerd/ttrpc
#!RemoteAsset:  sha256:647c74fa44cc19ccb2f89d01283f4488c7cac7578b14b3d537fbd19b92146abf
Source0:        https://github.com/containerd/ttrpc/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(github.com/prometheus/procfs)

Provides:       go(github.com/containerd/ttrpc) = %{version}

Requires:       go(github.com/containerd/log)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang/protobuf)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
ttrpc provides a compact gRPC-compatible RPC implementation for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
