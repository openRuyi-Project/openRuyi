# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           metrics
%define go_import_path  k8s.io/metrics

Name:           go-k8s-metrics
Version:        0.19.3
Release:        %autorelease
Summary:        Kubernetes metrics API type definitions and clients
License:        Apache-2.0
URL:            https://github.com/kubernetes/metrics
#!RemoteAsset:  sha256:6e70fffac112d3f39fdafa985fc7bbbfaa7271b4944a9d2947a9ae1dcd28020d
Source0:        https://github.com/kubernetes/metrics/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/client-go)

Provides:       go(k8s.io/metrics) = %{version}

Requires:       go(github.com/gogo/protobuf)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/client-go)

%description
This library supplies API types and clients for Kubernetes resource,
custom and external metrics. Metrics servers and their consumers can
use these interfaces to exchange pod, node and application measurements.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
