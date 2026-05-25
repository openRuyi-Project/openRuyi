# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sdk
%define go_import_path  go.opentelemetry.io/otel/sdk
%define go_source_subdir sdk

Name:           go-opentelemetry-otel-sdk
Version:        1.43.0
Release:        %autorelease
Summary:        Go module dependency for Prometheus
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go
#!RemoteAsset:  sha256:836705c57a5c44566e2aeb624060c7eba9547310240061bf9bc06cd7e36be3e7
Source0:        https://github.com/open-telemetry/opentelemetry-go/archive/refs/tags/sdk/v1.43.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n opentelemetry-go-sdk-v1.43.0
# This package owns a Go module below the repository root; the explicit
# %%install/%%check sections below copy only %%{go_source_subdir}, because
# the default golangmodules phases would copy the full archive under
# %%{go_import_path} and create invalid import paths.
# Nested Go modules have their own module path/dependencies; skip them in %check
# so the parent package does not try to test unrelated internal tools.
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/log*
    %{go_import_path}/metric*
}

BuildRequires:  go
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/logr/funcr)
BuildRequires:  go(github.com/go-logr/logr/testr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(github.com/stretchr/testify/suite)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/attribute)
BuildRequires:  go(go.opentelemetry.io/otel/codes)
BuildRequires:  go(go.opentelemetry.io/otel/internal/global)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/metric/embedded)
BuildRequires:  go(go.opentelemetry.io/otel/metric/noop)
BuildRequires:  go(go.opentelemetry.io/otel/propagation)
BuildRequires:  go(go.opentelemetry.io/otel/semconv/v1.40.0)
BuildRequires:  go(go.opentelemetry.io/otel/semconv/v1.40.0/otelconv)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.opentelemetry.io/otel/trace/embedded)
BuildRequires:  go(go.opentelemetry.io/otel/trace/noop)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/unix)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/otel/sdk) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/instrumentation) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/internal) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/internal/x) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/metric) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/metric/exemplar) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/metric/internal) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/metric/internal/aggregate) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/metric/internal/observ) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/metric/internal/reservoir) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/metric/internal/x) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/metric/metricdata) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/metric/metricdata/metricdatatest) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/resource) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/trace) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/trace/internal/env) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/trace/internal/observ) = %{version}
Provides:       go(go.opentelemetry.io/otel/sdk/trace/tracetest) = %{version}

Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/google/uuid)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/attribute)
Requires:       go(go.opentelemetry.io/otel/codes)
Requires:       go(go.opentelemetry.io/otel/internal/global)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/metric/embedded)
Requires:       go(go.opentelemetry.io/otel/metric/noop)
Requires:       go(go.opentelemetry.io/otel/propagation)
Requires:       go(go.opentelemetry.io/otel/semconv/v1.40.0)
Requires:       go(go.opentelemetry.io/otel/semconv/v1.40.0/otelconv)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.opentelemetry.io/otel/trace/embedded)
Requires:       go(go.opentelemetry.io/otel/trace/noop)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/sys/unix)

%description
Go module dependency for Prometheus. Generated by go2spec.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
export GO111MODULE=off
# SDK source imports go.opentelemetry.io/otel/internal/global. Copy the
# installed parent module into the temporary GOPATH first so Go's internal
# package visibility check sees sdk and otel/internal in the same tree.
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p %{_builddir}/go/src/go.opentelemetry.io
cp -a %{_datadir}/gocode/src/go.opentelemetry.io/otel %{_builddir}/go/src/go.opentelemetry.io/
rm -rf %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}
_go_pkgs="%{?go_test_include}"
if [ -z "${_go_pkgs}" ]; then
    _go_pkgs=$(go list -e -f '{{.ImportPath}}' ./...)
fi
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
test -n "${_go_filtered}"
go test -v ${_go_filtered}
popd

%files
%doc sdk/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
