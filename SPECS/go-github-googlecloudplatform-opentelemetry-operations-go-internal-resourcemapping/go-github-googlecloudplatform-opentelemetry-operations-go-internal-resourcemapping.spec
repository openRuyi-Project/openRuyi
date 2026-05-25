# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           resourcemapping
%define go_import_path  github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping
%define go_source_subdir internal/resourcemapping

Name:           go-github-googlecloudplatform-opentelemetry-operations-go-internal-resourcemapping
Version:        0.56.0
Release:        %autorelease
Summary:        Resource mapping helpers for OpenTelemetry Google Cloud exporters
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/opentelemetry-operations-go
#!RemoteAsset:  sha256:1fb2308d9aad853f7fba330f21b68ee45ab31a7f69add6a043c3ba9700ecb6fb
Source0:        https://github.com/GoogleCloudPlatform/opentelemetry-operations-go/archive/refs/tags/internal/resourcemapping/v0.56.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n opentelemetry-operations-go-internal-resourcemapping-v0.56.0
# The explicit %%install/%%check sections below enter %%{go_source_subdir};
# using BuildOption(prep): -n .../internal/resourcemapping would place the
# module contents at the wrong import root because the GitHub archive is still
# rooted at the full opentelemetry-operations-go tree.

BuildRequires:  go
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping) = %{version}

Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/protobuf)

%description
This package provides Resource mapping helpers for OpenTelemetry Google Cloud exporters.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
