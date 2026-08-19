# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           streaming
%define go_import_path  k8s.io/streaming

Name:           go-k8s-streaming
Version:        0.36.2
Release:        %autorelease
Summary:        Contains the staged module root for Kubernetes transport streaming primitives
License:        Apache-2.0
URL:            https://github.com/kubernetes/streaming
#!RemoteAsset:  sha256:cdcb85a1668aae13e2a373ff5cdc9cbae16e46fca84ccf320e027ff585bfdf76
Source0:        https://github.com/kubernetes/streaming/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/armon/go-socks5)
BuildRequires:  go(github.com/moby/spdystream)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/utils/net)

Provides:       go(k8s.io/streaming) = %{version}

Requires:       go(github.com/moby/spdystream)
Requires:       go(golang.org/x/net)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/utils/net)

%description
Kubernetes transport streaming primitives for Go.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
