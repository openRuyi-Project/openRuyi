# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           streaming
%define go_import_path  k8s.io/streaming

Name:           go-k8s-streaming
Version:        0.36.1
Release:        %autorelease
Summary:        Kubernetes transport streaming primitives for Go
License:        Apache-2.0
URL:            https://github.com/kubernetes/streaming
#!RemoteAsset:  sha256:6c6d4bd668020c9574586f1585f90d9862b55e0c1e90f5a01db0fd29e760130c
Source0:        https://github.com/kubernetes/streaming/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/armon/go-socks5)
BuildRequires:  go(github.com/moby/spdystream)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/utils)

Provides:       go(k8s.io/streaming) = %{version}
Provides:       go(k8s.io/streaming/pkg/httpstream) = %{version}
Provides:       go(k8s.io/streaming/pkg/httpstream/spdy) = %{version}
Provides:       go(k8s.io/streaming/pkg/httpstream/wsstream) = %{version}
Provides:       go(k8s.io/streaming/pkg/runtime) = %{version}

Requires:       go(github.com/moby/spdystream)
Requires:       go(golang.org/x/net)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/utils)


%description
streaming contains Kubernetes transport streaming primitives for Go. It
provides HTTP stream, SPDY, websocket stream, and runtime helpers used for
remote command, attach, exec, and port-forward style APIs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
