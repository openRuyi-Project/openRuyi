# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           auth
%define go_import_path  cloud.google.com/go/auth
%define go_source_subdir auth

Name:           go-googlecloud-go-auth
Version:        0.20.0
Release:        %autorelease
Summary:        Go library for cloud.google.com/go/auth
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-go
#!RemoteAsset:  sha256:31d2fd0e0f3e4010e5776e7c8be92688995a200a43f8dfc5004ff3c12892e527
Source0:        https://github.com/googleapis/google-cloud-go/archive/refs/tags/auth/v0.20.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n google-cloud-go-auth-v0.20.0
# This module imports only google.golang.org/api/googleapi, so depend on the
# support leaf package instead of the full go-google-api package to avoid a
# bootstrap cycle with google-api.
# The explicit %%install/%%check sections below enter %%{go_source_subdir}; using
# BuildOption(prep): -n .../auth would copy the whole repository under the auth
# import path because the GitHub archive still contains the top-level directory.
# auth/oauth2adapt is a nested Go module packaged as
# go-googlecloud-go-auth-oauth2adapt; test and own it in that package.
%define go_test_exclude_glob %{go_import_path}/oauth2adapt*

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/googleapis/gax-go/v2/internallog)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
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
BuildRequires:  go(google.golang.org/api/googleapi)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(cloud.google.com/go/auth) = %{version}
Provides:       go(cloud.google.com/go/auth/credentials) = %{version}
Provides:       go(cloud.google.com/go/auth/credentials/downscope) = %{version}
Provides:       go(cloud.google.com/go/auth/credentials/externalaccount) = %{version}
Provides:       go(cloud.google.com/go/auth/credentials/idtoken) = %{version}
Provides:       go(cloud.google.com/go/auth/credentials/impersonate) = %{version}
Provides:       go(cloud.google.com/go/auth/credentials/internal/externalaccount) = %{version}
Provides:       go(cloud.google.com/go/auth/credentials/internal/externalaccountuser) = %{version}
Provides:       go(cloud.google.com/go/auth/credentials/internal/gdch) = %{version}
Provides:       go(cloud.google.com/go/auth/credentials/internal/impersonate) = %{version}
Provides:       go(cloud.google.com/go/auth/credentials/internal/stsexchange) = %{version}
Provides:       go(cloud.google.com/go/auth/grpctransport) = %{version}
Provides:       go(cloud.google.com/go/auth/httptransport) = %{version}
Provides:       go(cloud.google.com/go/auth/internal) = %{version}
Provides:       go(cloud.google.com/go/auth/internal/compute) = %{version}
Provides:       go(cloud.google.com/go/auth/internal/credsfile) = %{version}
Provides:       go(cloud.google.com/go/auth/internal/jwt) = %{version}
Provides:       go(cloud.google.com/go/auth/internal/retry) = %{version}
Provides:       go(cloud.google.com/go/auth/internal/testutil) = %{version}
Provides:       go(cloud.google.com/go/auth/internal/testutil/testdns) = %{version}
Provides:       go(cloud.google.com/go/auth/internal/testutil/testgcs) = %{version}
Provides:       go(cloud.google.com/go/auth/internal/transport) = %{version}
Provides:       go(cloud.google.com/go/auth/internal/transport/cert) = %{version}
Provides:       go(cloud.google.com/go/auth/internal/transport/headers) = %{version}
Provides:       go(cloud.google.com/go/auth/internal/trustboundary) = %{version}

Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/s2a-go)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/googleapis/gax-go/v2/internallog)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/api/googleapi)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library cloud.google.com/go/auth.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
# TestDownscopedToken needs Google Application Default Credentials, and the
# DirectPath misconfiguration tests fail in OBS with "failed to create creds".
%buildsystem_golangmodules_check -skip 'TestDownscopedToken|TestLogDirectPathMisconfigDirectPathNotSet|TestLogDirectPathMisconfigNotOnGCE'
popd

%files
%doc README.md
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let this module own
# their source directories, otherwise RPM can hit file conflicts.
%exclude %{go_sys_gopath}/%{go_import_path}/oauth2adapt

%changelog
%autochangelog
