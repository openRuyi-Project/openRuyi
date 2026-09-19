# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           konnectivity-client
%define go_import_path  sigs.k8s.io/apiserver-network-proxy/konnectivity-client

Name:           go-k8s-sigs-apiserver-network-proxy-konnectivity-client
Version:        0.34.0
Release:        %autorelease
Summary:        Kubernetes API server network proxy client
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/apiserver-network-proxy
#!RemoteAsset:  sha256:bf660c8f0f580f8ff1b52eac821bfb233bfd58d32416b133a6d75644288cb05f
Source0:        https://github.com/kubernetes-sigs/apiserver-network-proxy/archive/konnectivity-client/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(google.golang.org/protobuf/reflect)
BuildRequires:  go(google.golang.org/protobuf/runtime)
BuildRequires:  go(k8s.io/klog/v2)

Provides:       go(sigs.k8s.io/apiserver-network-proxy/konnectivity-client) = %{version}

Requires:       go(github.com/prometheus/client_golang)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/codes)
Requires:       go(google.golang.org/grpc/status)
Requires:       go(google.golang.org/protobuf/reflect)
Requires:       go(google.golang.org/protobuf/runtime)
Requires:       go(k8s.io/klog/v2)

%description
This package provides the Go client library used by Kubernetes components to
connect to an API server network proxy.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
