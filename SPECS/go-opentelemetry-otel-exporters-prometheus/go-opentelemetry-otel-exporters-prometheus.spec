# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           prometheus
%define go_import_path  go.opentelemetry.io/otel/exporters/prometheus
%define go_source_subdir exporters/prometheus

Name:           go-opentelemetry-otel-exporters-prometheus
Version:        0.65.0
Release:        %autorelease
Summary:        Prometheus exporter for OpenTelemetry Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go
#!RemoteAsset:  sha256:661e5fb88fe193071d43aae3fc4291bf1c5f92432ceb51431500effb6211756f
Source0:        https://github.com/open-telemetry/opentelemetry-go/archive/refs/tags/exporters/prometheus/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# This package owns a Go module below the repository root; the explicit
# %%install/%%check sections below copy only %%{go_source_subdir}, because
# the default golangmodules phases would copy the full archive under
# %%{go_import_path} and create invalid import paths.

BuildRequires:  go
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/kylelemons/godebug)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/otlptranslator)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/otel/exporters/prometheus) = %{version}

Requires:       go(github.com/beorn7/perks)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/kylelemons/godebug)
Requires:       go(github.com/munnerz/goautoneg)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/otlptranslator)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/yaml.v3)

%description
This package provides Prometheus exporter for OpenTelemetry Go.

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
%doc exporters/prometheus/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
