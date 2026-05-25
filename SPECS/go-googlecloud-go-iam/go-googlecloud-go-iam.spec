# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           iam
%define go_import_path  cloud.google.com/go/iam
%define go_source_subdir iam

Name:           go-googlecloud-go-iam
Version:        1.11.0
Release:        %autorelease
Summary:        IAM client libraries for Google Cloud Go
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-go
#!RemoteAsset:  sha256:6bcf9ab2e3c5f87777b887273dfbf17fc4414cafda4fa6930831d863372a306c
Source0:        https://github.com/googleapis/google-cloud-go/archive/refs/tags/iam/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The explicit %%install/%%check sections below enter %%{go_source_subdir};
# using BuildOption(prep): -n .../iam would place the module contents at the
# wrong import root because the GitHub archive is still rooted at the full
# google-cloud-go tree. - HNO3Miracle

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/internal)
BuildRequires:  go(cloud.google.com/go/longrunning)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
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

Provides:       go(cloud.google.com/go/iam) = %{version}

Requires:       go(cloud.google.com/go/auth)
Requires:       go(cloud.google.com/go/auth/oauth2adapt)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(cloud.google.com/go/internal)
Requires:       go(cloud.google.com/go/longrunning)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/google/s2a-go)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(go.opentelemetry.io/auto/sdk)
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
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides IAM client libraries for Google Cloud Go.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
rm -rf "%{_builddir}/go/src/cloud.google.com/go"
mkdir -p "%{_builddir}/go/src/$(dirname "%{go_import_path}")"
cp -a . "%{_builddir}/go/src/%{go_import_path}"
# iam tests import cloud.google.com/go/internal/testutil. Keep the module and
# its sibling internal packages in the same temporary GOPATH tree so Go internal
# package visibility rules are preserved. - HNO3Miracle
cp -a ../internal "%{_builddir}/go/src/cloud.google.com/go/internal"
cd "%{_builddir}/go/src/%{go_import_path}"
go test -v $(go list -e -f '{{.ImportPath}}' ./...)
popd

%files
%doc %{go_source_subdir}/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
