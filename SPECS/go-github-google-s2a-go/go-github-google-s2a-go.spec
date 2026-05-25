# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           s2a-go
%define go_import_path  github.com/google/s2a-go

Name:           go-github-google-s2a-go
Version:        0.1.9
Release:        %autorelease
Summary:        Go library for github.com/google/s2a-go
License:        Apache-2.0
URL:            https://github.com/google/s2a-go
#!RemoteAsset:  sha256:c996a4f8f50ca2229787fcb8066d963a4e17908a6552b3d2c138e1f9ee522d4d
Source0:        https://github.com/google/s2a-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch0:         2000-fix-non-constant-fprintf-test.patch

BuildOption(prep):  -n s2a-go-0.1.9
# tools/internal_ci/test_gae is an upstream App Engine CI helper. It imports
# Google API and Cloud Translate clients, creating a bootstrap cycle with
# google-api/google-cloud-go packages, while the library packages do not use
# those imports.
%define go_test_exclude_glob %{go_import_path}/tools*

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(go.opencensus.io)
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
BuildRequires:  go(google.golang.org/appengine)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/s2a-go) = %{version}
Provides:       go(github.com/google/s2a-go/fallback) = %{version}
Provides:       go(github.com/google/s2a-go/internal/authinfo) = %{version}
Provides:       go(github.com/google/s2a-go/internal/fakehandshaker/service) = %{version}
Provides:       go(github.com/google/s2a-go/internal/handshaker) = %{version}
Provides:       go(github.com/google/s2a-go/internal/handshaker/service) = %{version}
Provides:       go(github.com/google/s2a-go/internal/proto/common_go_proto) = %{version}
Provides:       go(github.com/google/s2a-go/internal/proto/s2a_context_go_proto) = %{version}
Provides:       go(github.com/google/s2a-go/internal/proto/s2a_go_proto) = %{version}
Provides:       go(github.com/google/s2a-go/internal/proto/v2/common_go_proto) = %{version}
Provides:       go(github.com/google/s2a-go/internal/proto/v2/s2a_context_go_proto) = %{version}
Provides:       go(github.com/google/s2a-go/internal/proto/v2/s2a_go_proto) = %{version}
Provides:       go(github.com/google/s2a-go/internal/record) = %{version}
Provides:       go(github.com/google/s2a-go/internal/record/internal/aeadcrypter) = %{version}
Provides:       go(github.com/google/s2a-go/internal/record/internal/aeadcrypter/testutil) = %{version}
Provides:       go(github.com/google/s2a-go/internal/record/internal/halfconn) = %{version}
Provides:       go(github.com/google/s2a-go/internal/tokenmanager) = %{version}
Provides:       go(github.com/google/s2a-go/internal/v2) = %{version}
Provides:       go(github.com/google/s2a-go/internal/v2/certverifier) = %{version}
Provides:       go(github.com/google/s2a-go/internal/v2/fakes2av2) = %{version}
Provides:       go(github.com/google/s2a-go/internal/v2/remotesigner) = %{version}
Provides:       go(github.com/google/s2a-go/internal/v2/tlsconfigstore) = %{version}
Provides:       go(github.com/google/s2a-go/retry) = %{version}
Provides:       go(github.com/google/s2a-go/stream) = %{version}

Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(go.opencensus.io)
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
Requires:       go(google.golang.org/appengine)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library github.com/google/s2a-go.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
