# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gax-go
%define go_import_path  github.com/googleapis/gax-go/v2
%define go_source_subdir v2
%define commit_id 8d0f47cf4be58fe6acbc59d9c29f8bf85b0f1bc2
# These packages import google.golang.org/api, while google-api itself imports
# gax-go. Exclude only the cycle-forming packages from %check so gax-go can
# bootstrap first; keep the runtime Requires below because the source is shipped. - HNO3Miracle
%define go_test_exclude %{shrink:
    %{go_import_path}
    %{go_import_path}/apierror
    %{go_import_path}/callctx
    %{go_import_path}/iterator
}
# callctx example tests and root tests import google.golang.org/genproto/googleapis/api
# only from test files. The runtime package keeps the root genproto dependency below. - HNO3Miracle
%global __requires_exclude ^go\\(google\\.golang\\.org/genproto/googleapis/api.*\\)$

Name:           go-github-googleapis-gax-go-v2
Version:        0+git20260607.8d0f47c
Release:        %autorelease
Summary:        Google API extensions for generated Go clients
License:        BSD-3-Clause
URL:            https://github.com/googleapis/gax-go
#!RemoteAsset:  sha256:5c55d68c3279fcd7d297c08ede7348418b6de0d77d91fd37bcab036e29620f31
Source0:        https://github.com/googleapis/gax-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstream keeps the v2 Go module in the v2/ subdirectory. Run install/check
# from that directory so GOPATH import paths do not become
# github.com/googleapis/gax-go/v2/v2. - HNO3Miracle

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/googleapis/gax-go/v2) = %{version}

Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
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
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides Google API extensions used by generated Go clients.

# google-api generated clients only import gax-go/v2/internallog. Split that
# subtree so google-api can build without installing the gax root package, which
# legitimately requires google-api for apierror/iterator helpers.
%package        internallog
Summary:        Internal logging helpers for generated Google API clients
Provides:       go(github.com/googleapis/gax-go/v2/internallog) = %{version}

%description    internallog
This subpackage provides internal logging helpers for generated Google API
clients.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/internallog

%files internallog
%license LICENSE
%{go_sys_gopath}/%{go_import_path}/internallog

%changelog
%autochangelog
