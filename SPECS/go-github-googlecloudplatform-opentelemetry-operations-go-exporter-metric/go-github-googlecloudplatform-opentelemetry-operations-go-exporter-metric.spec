# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           metric
%define go_import_path  github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric
%define go_source_subdir exporter/metric
# Root package tests import internal/cloudmock, which pulls cloud logging and
# creates a test-only bootstrap cycle because storage needs this metric exporter. - HNO3Miracle
%define go_test_exclude %{go_import_path}

Name:           go-github-googlecloudplatform-opentelemetry-operations-go-exporter-metric
Version:        0.57.0
Release:        %autorelease
Summary:        Google Cloud Monitoring metric exporter for OpenTelemetry
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/opentelemetry-operations-go
#!RemoteAsset:  sha256:cd7769b387d312bae444e31b86f372ca7e7146a0fbf229e6a26223776e4775ec
Source0:        https://github.com/GoogleCloudPlatform/opentelemetry-operations-go/archive/refs/tags/exporter/metric/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The explicit %%install/%%check sections below enter %%{go_source_subdir};
# using BuildOption(prep): -n .../exporter/metric would place the module
# contents at the wrong import root because the GitHub archive is still rooted
# at the full opentelemetry-operations-go tree. - HNO3Miracle

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/monitoring)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
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
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric) = %{version}

Requires:       go(cloud.google.com/go/auth)
Requires:       go(cloud.google.com/go/monitoring)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/oauth2)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Google Cloud Monitoring metric exporter for OpenTelemetry.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
rm -rf "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go"
mkdir -p "%{_builddir}/go/src/$(dirname "%{go_import_path}")"
cp -a . "%{_builddir}/go/src/%{go_import_path}"
mkdir -p "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal"
cp -a ../../internal/resourcemapping "%{_builddir}/go/src/github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping"
cd "%{_builddir}/go/src/%{go_import_path}"
_go_pkgs=$(go list -e -f '{{.ImportPath}}' ./...)
_go_exclude="%{?go_test_exclude}"
_go_exclude_glob="%{?go_test_exclude_glob}"
_go_filtered=""
set -f
for _pkg in ${_go_pkgs}; do
    _skip=0
    for _ex in ${_go_exclude}; do
        [ "${_pkg}" = "${_ex}" ] && _skip=1
    done
    for _ex in ${_go_exclude_glob}; do
        case "${_pkg}" in ${_ex}) _skip=1 ;; esac
    done
    [ ${_skip} -eq 0 ] && _go_filtered="${_go_filtered} ${_pkg}"
done
set +f
if [ -n "${_go_filtered}" ]; then
    go test -v ${_go_filtered}
fi
popd

%files
%doc %{go_source_subdir}/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
