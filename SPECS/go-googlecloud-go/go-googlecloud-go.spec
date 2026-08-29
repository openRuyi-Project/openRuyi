# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go
%define go_import_path  cloud.google.com/go

Name:           go-googlecloud-go
Version:        14617
Release:        %autorelease
Summary:        Root package for Google Cloud Go clients
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-go
#!RemoteAsset:  sha256:0c768debe4b6f6cb1328b5ee5ff9c761036229ec76dc1b476fcb66680bbdbafa
Source0:        https://github.com/googleapis/google-cloud-go/archive/release-%{version}.tar.gz#/%{_name}-release-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/iam)
BuildRequires:  go(cloud.google.com/go/monitoring)
BuildRequires:  go(cloud.google.com/go/storage)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/martian/v3)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping)
BuildRequires:  go(github.com/spiffe/go-spiffe/v2)
BuildRequires:  go(github.com/zeebo/errs)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/detectors/gcp)
BuildRequires:  go(go.opentelemetry.io/contrib)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
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
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(cloud.google.com/go) = %{version}

%description
This package provides the root cloud.google.com/go import path and common
metadata for Google Cloud Go client modules.

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
rm -rf "%{_builddir}/go/src/%{go_import_path}"
mkdir -p "%{_builddir}/go/src/$(dirname "%{go_import_path}")"
cp -a . "%{_builddir}/go/src/%{go_import_path}"
cd "%{_builddir}/go/src/%{go_import_path}"
# The default golangmodules check expands ./... across thousands of generated
# cloud client and snippet packages; OBS killed that run with "Logfile got too
# big". This aggregate package is only needed for the root import path, while
# selected submodules are packaged and tested separately. - HNO3Miracle
go test -v %{go_import_path}

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# These directories are standalone Go modules packaged separately; keep the
# aggregate root package from owning the same files. - HNO3Miracle
%exclude %{go_sys_gopath}/%{go_import_path}/auth
%exclude %{go_sys_gopath}/%{go_import_path}/compute
%exclude %{go_sys_gopath}/%{go_import_path}/httpreplay
%exclude %{go_sys_gopath}/%{go_import_path}/iam
%exclude %{go_sys_gopath}/%{go_import_path}/internal
%exclude %{go_sys_gopath}/%{go_import_path}/logging
%exclude %{go_sys_gopath}/%{go_import_path}/longrunning
%exclude %{go_sys_gopath}/%{go_import_path}/monitoring
%exclude %{go_sys_gopath}/%{go_import_path}/storage
%exclude %{go_sys_gopath}/%{go_import_path}/trace
%exclude %{go_sys_gopath}/%{go_import_path}/translate

%changelog
%autochangelog
