# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gax-go
%define go_import_path  github.com/googleapis/gax-go/v2
%define go_source_subdir v2
%define commit_id 8d0f47cf4be58fe6acbc59d9c29f8bf85b0f1bc2

Name:           go-github-googleapis-gax-go-v2
Version:        0+git20260518.8d0f47c
Release:        %autorelease
Summary:        Go library for github.com/googleapis/gax-go/v2
License:        BSD-3-Clause
URL:            https://github.com/googleapis/gax-go
#!RemoteAsset:  sha256:5c55d68c3279fcd7d297c08ede7348418b6de0d77d91fd37bcab036e29620f31
Source0:        https://github.com/googleapis/gax-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n gax-go-%{commit_id}
# Upstream keeps the v2 Go module in the v2/ subdirectory. Run install/check
# from that directory so GOPATH import paths do not become
# github.com/googleapis/gax-go/v2/v2.

# These packages import google.golang.org/api, while google-api itself imports
# gax-go. Exclude only the cycle-forming packages from %check so gax-go can
# bootstrap first; keep the runtime Requires below because the source is shipped.
%define go_test_exclude %{shrink:
    %{go_import_path}
    %{go_import_path}/apierror
    %{go_import_path}/iterator
}

BuildRequires:  go
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/googleapis/gax-go/v2) = %{version}
Provides:       go(github.com/googleapis/gax-go/v2/apierror) = %{version}
Provides:       go(github.com/googleapis/gax-go/v2/apierror/internal/proto) = %{version}
Provides:       go(github.com/googleapis/gax-go/v2/callctx) = %{version}
Provides:       go(github.com/googleapis/gax-go/v2/internal) = %{version}
Provides:       go(github.com/googleapis/gax-go/v2/iterator) = %{version}

Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/google/go-cmp)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/api/googleapi)
Requires:       go(google.golang.org/api/iterator)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library github.com/googleapis/gax-go/v2.

# google-api generated clients only import gax-go/v2/internallog. Split that
# subtree so google-api can build without installing the gax root package, which
# legitimately requires google-api for apierror/iterator helpers.
%package        internallog
Summary:        Internal logging helpers for generated Google API clients

Provides:       go(github.com/googleapis/gax-go/v2/internallog) = %{version}
Provides:       go(github.com/googleapis/gax-go/v2/internallog/grpclog) = %{version}
Provides:       go(github.com/googleapis/gax-go/v2/internallog/internal) = %{version}
Provides:       go(github.com/googleapis/gax-go/v2/internallog/internal/bookpb) = %{version}
Provides:       go(github.com/googleapis/gax-go/v2/internallog/internal/logtest) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description    internallog
This subpackage provides github.com/googleapis/gax-go/v2/internallog.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/internallog

%files internallog
%{go_sys_gopath}/%{go_import_path}/internallog

%changelog
%autochangelog
