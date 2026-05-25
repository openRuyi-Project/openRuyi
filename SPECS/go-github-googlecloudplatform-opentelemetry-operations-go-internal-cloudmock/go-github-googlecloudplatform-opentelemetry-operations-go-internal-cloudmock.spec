# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cloudmock
%define go_import_path  github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/cloudmock

Name:           go-github-googlecloudplatform-opentelemetry-operations-go-internal-cloudmock
Version:        0.56.0
Release:        %autorelease
Summary:        Cloud mock helpers for OpenTelemetry Google Cloud tests
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/opentelemetry-operations-go
#!RemoteAsset:  sha256:7eab1e3f5395e12e19d2eaa7ae8a121918698ddd4ce74e640408343d785dffbe
Source0:        https://github.com/GoogleCloudPlatform/opentelemetry-operations-go/archive/refs/tags/internal/cloudmock/v0.56.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n opentelemetry-operations-go-internal-cloudmock-v0.56.0/internal/cloudmock
# The import path is a Go module below the repository root; keep %check scoped
# to this module so GOPATH-mode tests do not scan sibling modules from the archive.
%define go_test_include %{go_import_path}

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/logging)
BuildRequires:  go(cloud.google.com/go/longrunning)
BuildRequires:  go(cloud.google.com/go/monitoring)
BuildRequires:  go(cloud.google.com/go/trace)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/cloudmock) = %{version}

Requires:       go(cloud.google.com/go/logging)
Requires:       go(cloud.google.com/go/longrunning)
Requires:       go(cloud.google.com/go/monitoring)
Requires:       go(cloud.google.com/go/trace)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides Cloud mock helpers for OpenTelemetry Google Cloud tests.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
