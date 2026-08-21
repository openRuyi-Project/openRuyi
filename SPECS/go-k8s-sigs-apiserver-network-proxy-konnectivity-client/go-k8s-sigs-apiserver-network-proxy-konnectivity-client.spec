# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           konnectivity-client
%define go_import_path  sigs.k8s.io/apiserver-network-proxy
# Integration tests require a kind cluster, prebuilt images, and unrestricted
# network behavior that is unavailable in the OBS build environment.
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/e2e*
    %{go_import_path}/tests*
}

Name:           go-k8s-sigs-apiserver-network-proxy-konnectivity-client
Version:        0.34.0
Release:        %autorelease
Summary:        Kubernetes API server network proxy
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/apiserver-network-proxy
#!RemoteAsset:  sha256:bf660c8f0f580f8ff1b52eac821bfb233bfd58d32416b133a6d75644288cb05f
Source0:        https://github.com/kubernetes-sigs/apiserver-network-proxy/archive/konnectivity-client/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/kubernetes-sigs/apiserver-network-proxy/commit/99a65280b5ddc82b02a5226f54dcf0f6568f04ef
Patch1000:      1000-fix-test-client-integer-format.patch

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

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/konnectivity-client) = %{version}

Requires:       go(github.com/prometheus/client_golang)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/codes)
Requires:       go(google.golang.org/grpc/status)
Requires:       go(google.golang.org/protobuf/reflect)
Requires:       go(google.golang.org/protobuf/runtime)
Requires:       go(k8s.io/klog/v2)

%description
This package provides the API server network proxy and the Go client library
used by Kubernetes components to connect to it.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
