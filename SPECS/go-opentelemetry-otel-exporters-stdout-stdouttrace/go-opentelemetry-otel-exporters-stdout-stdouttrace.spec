# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stdouttrace
%define go_import_path  go.opentelemetry.io/otel/exporters/stdout/stdouttrace
%define go_source_subdir exporters/stdout/stdouttrace

Name:           go-opentelemetry-otel-exporters-stdout-stdouttrace
Version:        1.43.0
Release:        %autorelease
Summary:        Stdout trace exporter for OpenTelemetry Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go
#!RemoteAsset:  sha256:1822f099b2f1866e3d0e58d44e0e22e9fb4c7e229ddb1080a04c39dbabbd19a8
Source0:        https://github.com/open-telemetry/opentelemetry-go/archive/refs/tags/exporters/stdout/stdouttrace/v1.43.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n opentelemetry-go-exporters-stdout-stdouttrace-v1.43.0
# This package owns a Go module below the repository root; the explicit
# %%install/%%check sections below copy only %%{go_source_subdir}, because
# the default golangmodules phases would copy the full archive under
# %%{go_import_path} and create invalid import paths.

BuildRequires:  go
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/attribute)
BuildRequires:  go(go.opentelemetry.io/otel/codes)
BuildRequires:  go(go.opentelemetry.io/otel/internal/global)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/propagation)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/instrumentation)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric/metricdata)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric/metricdata/metricdatatest)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/resource)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/trace)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/trace/tracetest)
BuildRequires:  go(go.opentelemetry.io/otel/semconv/v1.40.0)
BuildRequires:  go(go.opentelemetry.io/otel/semconv/v1.40.0/otelconv)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace) = %{version}
Provides:       go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace/internal) = %{version}
Provides:       go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace/internal/counter) = %{version}
Provides:       go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace/internal/observ) = %{version}
Provides:       go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace/internal/x) = %{version}

Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/attribute)
Requires:       go(go.opentelemetry.io/otel/internal/global)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/propagation)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/sdk/trace)
Requires:       go(go.opentelemetry.io/otel/sdk/trace/tracetest)
Requires:       go(go.opentelemetry.io/otel/semconv/v1.40.0)
Requires:       go(go.opentelemetry.io/otel/semconv/v1.40.0/otelconv)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/sys)
Requires:       go(gopkg.in/yaml.v3)

%description
This package provides Stdout trace exporter for OpenTelemetry Go.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
export GO111MODULE=off
# Submodule tests may import packages, including internal packages, from the
# parent module. Copy an installed parent tree into the temporary GOPATH first
# so Go's internal package visibility checks use a single physical tree.
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
_go_parent=%{go_import_path}
while :; do
    _go_next_parent=${_go_parent%/*}
    [ "${_go_next_parent}" = "${_go_parent}" ] && break
    _go_parent=${_go_next_parent}
    if [ -d "%{_datadir}/gocode/src/${_go_parent}" ] &&
       { [ -f "%{_datadir}/gocode/src/${_go_parent}/go.mod" ] ||
         [ -n "$(find "%{_datadir}/gocode/src/${_go_parent}" -maxdepth 1 -name '*.go' -print -quit 2>/dev/null)" ]; }; then
        mkdir -p "%{_builddir}/go/src/$(dirname "${_go_parent}")"
        rm -rf "%{_builddir}/go/src/${_go_parent}"
        cp -a "%{_datadir}/gocode/src/${_go_parent}" "%{_builddir}/go/src/${_go_parent}"
        break
    fi
done
mkdir -p "%{_builddir}/go/src/$(dirname "%{go_import_path}")"
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
%doc exporters/stdout/stdouttrace/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
