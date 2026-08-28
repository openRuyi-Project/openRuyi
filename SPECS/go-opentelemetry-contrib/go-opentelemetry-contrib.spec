# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-go-contrib
%define go_import_path  go.opentelemetry.io/contrib
%define contrib_paths   %{shrink:
    bridges/otelzap
    instrumentation/google.golang.org/grpc/otelgrpc
    instrumentation/net/http/httptrace/otelhttptrace
    instrumentation/net/http/otelhttp
    otelconf
    propagators/autoprop
    propagators/aws
    propagators/b3
    propagators/jaeger
    propagators/ot
    zpages
}

Name:           go-opentelemetry-contrib
Version:        0.69.0
Release:        %autorelease
Summary:        OpenTelemetry instrumentation modules for Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go-contrib
#!RemoteAsset:  sha256:323ba7865cfb62bd19a2119bca1b39f5f6d64e3629b010f58d5f6c8a02d3e349
Source0:        https://github.com/open-telemetry/opentelemetry-go-contrib/archive/refs/tags/instrumentation/net/http/otelhttp/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The upstream repository is a multi-module tree. Bundle the modules required by
# current consumers because they share one upstream release commit and contain
# local replacements between sibling modules.

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/cenkalti/backoff)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
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
BuildRequires:  go(go.opentelemetry.io/otel/exporters/prometheus)
BuildRequires:  go(go.opentelemetry.io/proto)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(go.opentelemetry.io/contrib) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp) = %{version}
Provides:       go(go.opentelemetry.io/contrib/bridges/otelzap) = %{version}
Provides:       go(go.opentelemetry.io/contrib/otelconf) = %{version}
Provides:       go(go.opentelemetry.io/contrib/propagators/autoprop) = %{version}
Provides:       go(go.opentelemetry.io/contrib/propagators/aws) = %{version}
Provides:       go(go.opentelemetry.io/contrib/propagators/b3) = %{version}
Provides:       go(go.opentelemetry.io/contrib/propagators/jaeger) = %{version}
Provides:       go(go.opentelemetry.io/contrib/propagators/ot) = %{version}
Provides:       go(go.opentelemetry.io/contrib/zpages) = %{version}

Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/otlptranslator)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/exporters/prometheus)
Requires:       go(go.opentelemetry.io/proto)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/exp)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides OpenTelemetry Go contrib instrumentation, configuration,
propagation, logging bridge, and diagnostic modules.

%install
for _subdir in %{contrib_paths}; do
    install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}/$(dirname "${_subdir}")"
    cp -a "${_subdir}" "%{buildroot}%{go_sys_gopath}/%{go_import_path}/${_subdir}"
done

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
# TestWithSpanNameFormatter expects Go 1.22+ ServeMux pattern matching;
# OBS currently behaves like httpmuxgo121=1 unless this is forced. - HNO3Miracle
export GODEBUG="${GODEBUG:+${GODEBUG},}httpmuxgo121=0"
for _subdir in %{contrib_paths}; do
    _import_path=%{go_import_path}/${_subdir}
    mkdir -p "%{_builddir}/go/src/$(dirname "${_import_path}")"
    rm -rf "%{_builddir}/go/src/${_import_path}"
    cp -a "${_subdir}" "%{_builddir}/go/src/${_import_path}"
done
for _subdir in %{contrib_paths}; do
    _import_path=%{go_import_path}/${_subdir}
    pushd "%{_builddir}/go/src/${_import_path}"
    go test -v $(go list -e -f '{{.ImportPath}}' ./...)
    popd
done

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
