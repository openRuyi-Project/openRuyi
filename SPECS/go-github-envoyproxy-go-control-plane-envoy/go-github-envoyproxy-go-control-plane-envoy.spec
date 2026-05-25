# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           envoy
%define go_import_path  github.com/envoyproxy/go-control-plane/envoy
%define go_source_subdir envoy

Name:           go-github-envoyproxy-go-control-plane-envoy
Version:        1.37.0
Release:        %autorelease
Summary:        Envoy API Go module from go-control-plane
License:        Apache-2.0
URL:            https://github.com/envoyproxy/go-control-plane
#!RemoteAsset:  sha256:311e84ca6659b8eb0a88bf7193579196a543305736ce8a0e12dc450a8faa1139
Source0:        https://github.com/envoyproxy/go-control-plane/archive/refs/tags/envoy/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/envoyproxy/go-control-plane)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/planetscale/vtprotobuf)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(go.opentelemetry.io/proto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/envoyproxy/go-control-plane/envoy) = %{version}

Requires:       go(cel.dev/expr)
Requires:       go(github.com/cncf/xds/go)
Requires:       go(github.com/envoyproxy/go-control-plane)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(github.com/planetscale/vtprotobuf)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(go.opentelemetry.io/proto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Envoy API Go module from go-control-plane.

%install
# The envoy tag contains a nested Go module below the archive root. Keep prep at
# the root so shared LICENSE/README files are available, then enter the nested
# module for install and check.
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
