# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cri-streaming
%define go_import_path  k8s.io/cri-streaming

Name:           go-k8s-cri-streaming
Version:        0.36.3
Release:        %autorelease
Summary:        Kubernetes CRI streaming server implementation
License:        Apache-2.0
URL:            https://github.com/kubernetes/cri-streaming
#!RemoteAsset:  sha256:3b516875a5e9b7020ea969a7b6f06abae889e1a0d92036283ff76158ea34d10d
Source0:        https://github.com/kubernetes/cri-streaming/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(k8s.io/cri-api/pkg)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/streaming/pkg)
BuildRequires:  go(k8s.io/utils/clock)
BuildRequires:  go(k8s.io/utils/exec)

Provides:       go(k8s.io/cri-streaming) = %{version}

Requires:       go(github.com/emicklei/go-restful/v3)
Requires:       go(google.golang.org/grpc/codes)
Requires:       go(google.golang.org/grpc/status)
Requires:       go(k8s.io/cri-api/pkg)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/streaming/pkg)
Requires:       go(k8s.io/utils/clock)
Requires:       go(k8s.io/utils/exec)

%description
This package provides the Kubernetes CRI streaming server implementation for
exec, attach, and port forwarding without depending on the full kubelet module.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
