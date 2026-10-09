# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kms
%define go_import_path  k8s.io/kms

Name:           go-k8s-kms
Version:        0.37.1
Release:        %autorelease
Summary:        Kubernetes Key Management Service API
License:        Apache-2.0
URL:            https://github.com/kubernetes/kms
#!RemoteAsset:  sha256:c353e5fd72374a4664716f736ac6ad70c902992fa1a6f662443543edde1d3e05
Source0:        https://github.com/kubernetes/kms/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/credentials)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(google.golang.org/protobuf/reflect)
BuildRequires:  go(google.golang.org/protobuf/runtime)

Provides:       go(k8s.io/kms) = %{version}

Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/codes)
Requires:       go(google.golang.org/grpc/status)
Requires:       go(google.golang.org/protobuf/reflect)
Requires:       go(google.golang.org/protobuf/runtime)

%description
The Kubernetes Key Management Service module provides the API and service
types used by Kubernetes encryption-at-rest key management plugins.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
