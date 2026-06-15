# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-go-contrib
%define go_import_path  go.opentelemetry.io/contrib
%define otelgrpc_path   instrumentation/google.golang.org/grpc/otelgrpc
%define otelhttp_path   instrumentation/net/http/otelhttp
%define oteltrace_path  instrumentation/net/http/httptrace/otelhttptrace

Name:           go-opentelemetry-contrib
Version:        0.68.0
Release:        %autorelease
Summary:        OpenTelemetry instrumentation modules for Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go-contrib
#!RemoteAsset:  sha256:4ad91b08b6700d5803e5758a0bed12223abe7c5c8442d83ffb5abd39b11e33a1
Source0:        https://github.com/open-telemetry/opentelemetry-go-contrib/archive/refs/tags/instrumentation/net/http/otelhttp/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The upstream repository is a multi-module tree. Package the modules currently
# needed by prometheus and Google libraries together because they share the same
# upstream release commit and otelhttptrace has a local replace to otelhttp. - HNO3Miracle

BuildRequires:  go
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutmetric)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(go.opentelemetry.io/contrib) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp) = %{version}

Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides selected OpenTelemetry Go contrib instrumentation modules:
gRPC, HTTP, and HTTP trace instrumentation.

%install
for _subdir in %{otelgrpc_path} %{otelhttp_path} %{oteltrace_path}; do
    install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}/$(dirname "${_subdir}")"
    cp -a "${_subdir}" "%{buildroot}%{go_sys_gopath}/%{go_import_path}/${_subdir}"
done

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
# TestWithSpanNameFormatter expects Go 1.22+ ServeMux pattern matching;
# OBS currently behaves like httpmuxgo121=1 unless this is forced. - HNO3Miracle
export GODEBUG="${GODEBUG:+${GODEBUG},}httpmuxgo121=0"
for _subdir in %{otelgrpc_path} %{otelhttp_path} %{oteltrace_path}; do
    _import_path=%{go_import_path}/${_subdir}
    mkdir -p "%{_builddir}/go/src/$(dirname "${_import_path}")"
    rm -rf "%{_builddir}/go/src/${_import_path}"
    cp -a "${_subdir}" "%{_builddir}/go/src/${_import_path}"
done
for _subdir in %{otelgrpc_path} %{otelhttp_path} %{oteltrace_path}; do
    _import_path=%{go_import_path}/${_subdir}
    pushd "%{_builddir}/go/src/${_import_path}"
    go test -v $(go list -e -f '{{.ImportPath}}' ./...)
    popd
done

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}/%{otelgrpc_path}
%{go_sys_gopath}/%{go_import_path}/%{otelhttp_path}
%{go_sys_gopath}/%{go_import_path}/%{oteltrace_path}

%changelog
%autochangelog
