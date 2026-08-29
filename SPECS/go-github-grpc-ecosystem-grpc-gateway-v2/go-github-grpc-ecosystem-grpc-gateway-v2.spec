# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           grpc-gateway
%define go_import_path  github.com/grpc-ecosystem/grpc-gateway/v2

Name:           go-github-grpc-ecosystem-grpc-gateway-v2
Version:        2.29.0
Release:        %autorelease
Summary:        gRPC to JSON proxy generator for Go
License:        BSD-3-Clause
URL:            https://github.com/grpc-ecosystem/grpc-gateway
#!RemoteAsset:  sha256:c067650666440981109965953c4636cb08a556d0986ad4861167fec4553d8d74
Source0:        https://github.com/grpc-ecosystem/grpc-gateway/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/antihax/optional)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/rogpeppe/fastuuid)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)

Provides:       go(github.com/grpc-ecosystem/grpc-gateway/v2) = %{version}

Requires:       go(github.com/antihax/optional)
Requires:       go(github.com/rogpeppe/fastuuid)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides gRPC to JSON reverse proxy generation support for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
