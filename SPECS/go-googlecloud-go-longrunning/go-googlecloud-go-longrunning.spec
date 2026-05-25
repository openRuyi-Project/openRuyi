# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           longrunning
%define go_import_path  cloud.google.com/go/longrunning
%define go_source_subdir longrunning

Name:           go-googlecloud-go-longrunning
Version:        1.0.0
Release:        %autorelease
Summary:        Go library for cloud.google.com/go/longrunning
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-go
#!RemoteAsset:  sha256:97922f03412c49b0f13f83b8f6866f4ce7663663024bf57819add8f8ecc22f53
Source0:        https://github.com/googleapis/google-cloud-go/archive/refs/tags/longrunning/v1.0.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n google-cloud-go-longrunning-v1.0.0
# The explicit %%install/%%check sections below enter %%{go_source_subdir};
# using BuildOption(prep): -n .../longrunning would place the module contents at
# the wrong import root because the GitHub archive is still rooted at the full
# google-cloud-go tree. tidyfix.go imports cloud.google.com/go only under the
# modhack build tag, so the root module is not a real build or check dependency.

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(cloud.google.com/go/longrunning) = %{version}
Provides:       go(cloud.google.com/go/longrunning/autogen) = %{version}
Provides:       go(cloud.google.com/go/longrunning/autogen/longrunningpb) = %{version}
Provides:       go(cloud.google.com/go/longrunning/internal) = %{version}

Requires:       go(cloud.google.com/go/auth)
Requires:       go(cloud.google.com/go/auth/oauth2adapt)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/google/s2a-go)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library cloud.google.com/go/longrunning.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%doc %{go_source_subdir}/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
