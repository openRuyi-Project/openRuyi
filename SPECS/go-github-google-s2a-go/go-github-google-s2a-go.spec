# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           s2a-go
%define go_import_path  github.com/google/s2a-go
# tools/internal_ci/test_gae is an upstream App Engine CI helper. It imports
# Google API and Cloud Translate clients, creating a bootstrap cycle with
# google-api/google-cloud-go packages, while the library packages do not use
# those imports. - HNO3Miracle
%define go_test_exclude_glob %{go_import_path}/tools*

Name:           go-github-google-s2a-go
Version:        0.1.9
Release:        %autorelease
Summary:        Google S2A authentication library for Go
License:        Apache-2.0
URL:            https://github.com/google/s2a-go
#!RemoteAsset:  sha256:c996a4f8f50ca2229787fcb8066d963a4e17908a6552b3d2c138e1f9ee522d4d
Source0:        https://github.com/google/s2a-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 vet rejects non-constant fmt.Fprintf format strings in tests.
# - HNO3Miracle
Patch2000:      2000-fix-non-constant-fprintf-test.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(go.opentelemetry.io/contrib)
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
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/google/s2a-go) = %{version}

Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(go.opencensus.io)
Requires:       go(go.opentelemetry.io/contrib)
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
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides Go support for Google Secure Session Agent authentication.

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
