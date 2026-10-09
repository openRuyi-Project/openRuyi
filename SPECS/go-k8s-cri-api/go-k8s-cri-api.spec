# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cri-api
%define go_import_path  k8s.io/cri-api

Name:           go-k8s-cri-api
Version:        0.37.1
Release:        %autorelease
Summary:        Kubernetes Container Runtime Interface API definitions
License:        Apache-2.0
URL:            https://github.com/kubernetes/cri-api
#!RemoteAsset:  sha256:96c6ac2620dd941676930077f0920cda8f009fec0e21ea630502e7a902a06e3f
Source0:        https://github.com/kubernetes/cri-api/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(google.golang.org/protobuf/reflect)
BuildRequires:  go(google.golang.org/protobuf/runtime)

Provides:       go(k8s.io/cri-api) = %{version}
Provides:       go(k8s.io/cri-api/pkg) = %{version}

Requires:       go(github.com/stretchr/testify)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/codes)
Requires:       go(google.golang.org/grpc/status)
Requires:       go(google.golang.org/protobuf/proto)
Requires:       go(google.golang.org/protobuf/reflect)
Requires:       go(google.golang.org/protobuf/runtime)

%description
This package provides the Kubernetes Container Runtime Interface API
definitions used by kubelet and container runtime implementations.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
