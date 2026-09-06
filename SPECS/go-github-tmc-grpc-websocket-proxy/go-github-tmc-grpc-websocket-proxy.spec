# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           grpc-websocket-proxy
%define go_import_path  github.com/tmc/grpc-websocket-proxy
%define commit_id       673ab2c3ae75cc01952b84b88590e30e75dcf395

Name:           go-github-tmc-grpc-websocket-proxy
Version:        0+git20260821.673ab2c
Release:        %autorelease
Summary:        WebSocket proxy for gRPC streams
License:        MIT
URL:            https://github.com/tmc/grpc-websocket-proxy
#!RemoteAsset:  sha256:d61b8d40e899184d5b7a988a959b1f6fb5de64c3c4d5fb3435c9c0246aceb84f
Source0:        https://github.com/tmc/grpc-websocket-proxy/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/tmc/grpc-websocket-proxy) = %{version}

Requires:       go(github.com/gorilla/websocket)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(golang.org/x/net)

%description
This package adapts gRPC streams to WebSocket connections for clients that
cannot connect to a native gRPC endpoint.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
