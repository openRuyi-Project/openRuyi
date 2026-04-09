# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           grpc-gateway
%define go_import_path  github.com/grpc-ecosystem/grpc-gateway

Name:           go-github-grpc-ecosystem-grpc-gateway
Version:        2.27.7
Release:        %autorelease
Summary:        gRPC to JSON proxy generator following the gRPC HTTP spec
License:        BSD-3-Clause
URL:            https://github.com/grpc-ecosystem/grpc-gateway
#!RemoteAsset
Source0:        https://github.com/grpc-ecosystem/grpc-gateway/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/antihax/optional)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/rogpeppe/fastuuid)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/grpc-ecosystem/grpc-gateway) = %{version}

%description
The gRPC-Gateway is a plugin of the Google protocol buffers compiler
protoc. It reads protobuf
service definitions and generates a reverse-proxy server which
translates a RESTful HTTP API into gRPC. This server is generated according to the
google.api.http annotations in your service definitions.
This helps you provide your APIs in both gRPC and RESTful style at the
same time.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
