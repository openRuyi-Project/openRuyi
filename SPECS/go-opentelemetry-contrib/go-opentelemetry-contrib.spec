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

%define dir_otelgrpc    opentelemetry-go-contrib-instrumentation-google.golang.org-grpc-otelgrpc-v%{version}
%define dir_otelhttp    opentelemetry-go-contrib-instrumentation-net-http-otelhttp-v%{version}
%define dir_oteltrace   opentelemetry-go-contrib-instrumentation-net-http-httptrace-otelhttptrace-v%{version}
%define ver_otelconf    0.25.0
%define dir_otelconf    opentelemetry-go-contrib-otelconf-v%{ver_otelconf}
# Collector telemetry configuration also needs these bridges, propagators,
# and resource detectors. GCP remains owned by its existing detector RPM.
%define collector_contrib_modules %{shrink:
    bridges/otelslog
    bridges/otelzap
    detectors/aws/ecs
    detectors/aws/eks
    detectors/azure/azurevm
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
Summary:        OpenTelemetry instrumentation and telemetry configuration for Go
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-go-contrib
BuildArch:      noarch
BuildSystem:    golangmodules

# The modules are independently tagged at different repository commits, so use
# each module's exact official tag archive instead of assuming one tag contains
# the other modules at the same version.
#!RemoteAsset:  sha256:b37b3916da7ad1eeb6230b20612c01a08a1227977bd02213e1d6c2c5c3c98c98
Source0:        https://github.com/open-telemetry/opentelemetry-go-contrib/archive/refs/tags/%{otelgrpc_path}/v%{version}.tar.gz#/%{_name}-otelgrpc-%{version}.tar.gz
#!RemoteAsset:  sha256:323ba7865cfb62bd19a2119bca1b39f5f6d64e3629b010f58d5f6c8a02d3e349
Source1:        https://github.com/open-telemetry/opentelemetry-go-contrib/archive/refs/tags/%{otelhttp_path}/v%{version}.tar.gz#/%{_name}-otelhttp-%{version}.tar.gz
#!RemoteAsset:  sha256:f4fe446462d214049ce4a17e77180f473169017ed27be697b8d271827c101560
Source2:        https://github.com/open-telemetry/opentelemetry-go-contrib/archive/refs/tags/%{oteltrace_path}/v%{version}.tar.gz#/%{_name}-oteltrace-%{version}.tar.gz
# This release also contains matching otelzap, b3, and zpages source trees.
#!RemoteAsset:  sha256:ee1cd7a13db99251bcf8c534987d9b482e79f86891a6190381dab19f7afc0543
Source3:        https://github.com/open-telemetry/opentelemetry-go-contrib/archive/refs/tags/otelconf/v%{ver_otelconf}.tar.gz#/%{_name}-otelconf-%{ver_otelconf}.tar.gz

BuildRequires:  go
BuildRequires:  go(github.com/brunoscheufler/aws-ecs-metadata-go)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/otlptranslator)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/detectors/gcp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploggrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/prometheus)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutlog)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutmetric)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/log)
BuildRequires:  go(go.opentelemetry.io/otel/log/logtest)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/log)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/log/logtest)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.opentelemetry.io/proto)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(k8s.io/client-go)
BuildRequires:  go-rpm-macros

# Keep the umbrella virtual provide used by existing openRuyi consumers.
Provides:       go(go.opentelemetry.io/contrib) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace) = %{version}
Provides:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp) = %{version}
Provides:       go(go.opentelemetry.io/contrib/bridges/otelslog) = 0.20.0
Provides:       go(go.opentelemetry.io/contrib/bridges/otelzap) = 0.20.0
Provides:       go(go.opentelemetry.io/contrib/detectors/aws/ecs) = 1.45.0
Provides:       go(go.opentelemetry.io/contrib/detectors/aws/eks) = 1.45.0
Provides:       go(go.opentelemetry.io/contrib/detectors/azure/azurevm) = 0.17.0
Provides:       go(go.opentelemetry.io/contrib/otelconf) = %{ver_otelconf}
Provides:       go(go.opentelemetry.io/contrib/otelconf/v0.2.0) = %{ver_otelconf}
Provides:       go(go.opentelemetry.io/contrib/otelconf/v0.3.0) = %{ver_otelconf}
Provides:       go(go.opentelemetry.io/contrib/otelconf/x) = %{ver_otelconf}
Provides:       go(go.opentelemetry.io/contrib/propagators/autoprop) = 0.70.0
Provides:       go(go.opentelemetry.io/contrib/propagators/aws) = 1.45.0
Provides:       go(go.opentelemetry.io/contrib/propagators/aws/xray) = 1.45.0
Provides:       go(go.opentelemetry.io/contrib/propagators/b3) = 1.45.0
Provides:       go(go.opentelemetry.io/contrib/propagators/jaeger) = 1.45.0
Provides:       go(go.opentelemetry.io/contrib/propagators/ot) = 1.45.0
Provides:       go(go.opentelemetry.io/contrib/zpages) = 0.70.0

Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/brunoscheufler/aws-ecs-metadata-go)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/otlptranslator)
Requires:       go(go.opentelemetry.io/contrib/detectors/gcp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploggrpc)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp)
Requires:       go(go.opentelemetry.io/otel/exporters/prometheus)
Requires:       go(go.opentelemetry.io/otel/exporters/stdout/stdoutlog)
Requires:       go(go.opentelemetry.io/otel/exporters/stdout/stdoutmetric)
Requires:       go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
Requires:       go(go.opentelemetry.io/otel/log)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/log)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/exp)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(k8s.io/client-go)

%description
This package provides OpenTelemetry Go instrumentation, telemetry configuration,
logging bridges, propagators, resource detectors, and diagnostic pages.

%prep
%setup -q -c -T -a 0
%setup -q -D -T -a 1
%setup -q -D -T -a 2
%setup -q -D -T -a 3

%install
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/$(dirname %{otelgrpc_path})
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/$(dirname %{otelhttp_path})
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/$(dirname %{oteltrace_path})
cp -a %{dir_otelgrpc}/%{otelgrpc_path} \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/%{otelgrpc_path}
cp -a %{dir_otelhttp}/%{otelhttp_path} \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/%{otelhttp_path}
cp -a %{dir_oteltrace}/%{oteltrace_path} \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/%{oteltrace_path}
# Install complete module directories, including nested packages and fixtures.
for _module in %{collector_contrib_modules}; do
    install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}/$(dirname "${_module}")"
    cp -a "%{dir_otelconf}/${_module}" \
        "%{buildroot}%{go_sys_gopath}/%{go_import_path}/${_module}"
done

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
# TestWithSpanNameFormatter expects Go 1.22+ ServeMux pattern matching;
# force the current behavior in workers that default to httpmuxgo121=1.
export GODEBUG="${GODEBUG:+${GODEBUG},}httpmuxgo121=0"
for _entry in \
    "%{dir_otelgrpc}:%{otelgrpc_path}" \
    "%{dir_otelhttp}:%{otelhttp_path}" \
    "%{dir_oteltrace}:%{oteltrace_path}"; do
    _dir=${_entry%%:*}
    _subdir=${_entry#*:}
    _import_path=%{go_import_path}/${_subdir}
    mkdir -p "%{_builddir}/go/src/$(dirname "${_import_path}")"
    rm -rf "%{_builddir}/go/src/${_import_path}"
    cp -a "${_dir}/${_subdir}" "%{_builddir}/go/src/${_import_path}"
done
# Stage all modules in one tree so internal imports keep their Go visibility.
for _subdir in %{collector_contrib_modules}; do
    _import_path=%{go_import_path}/${_subdir}
    mkdir -p "%{_builddir}/go/src/$(dirname "${_import_path}")"
    rm -rf "%{_builddir}/go/src/${_import_path}"
    cp -a "%{dir_otelconf}/${_subdir}" "%{_builddir}/go/src/${_import_path}"
done
for _subdir in %{otelgrpc_path} %{otelhttp_path} %{oteltrace_path} %{collector_contrib_modules}; do
    _import_path=%{go_import_path}/${_subdir}
    pushd "%{_builddir}/go/src/${_import_path}"
    go test -v $(go list -e -f '{{.ImportPath}}' ./...)
    popd
done

%files
%license %{dir_otelgrpc}/LICENSE
%{go_sys_gopath}/%{go_import_path}/%{otelgrpc_path}
%{go_sys_gopath}/%{go_import_path}/%{otelhttp_path}
%{go_sys_gopath}/%{go_import_path}/%{oteltrace_path}
%{go_sys_gopath}/%{go_import_path}/bridges/otelslog
%{go_sys_gopath}/%{go_import_path}/bridges/otelzap
%{go_sys_gopath}/%{go_import_path}/detectors/aws/ecs
%{go_sys_gopath}/%{go_import_path}/detectors/aws/eks
%{go_sys_gopath}/%{go_import_path}/detectors/azure/azurevm
%{go_sys_gopath}/%{go_import_path}/otelconf
%{go_sys_gopath}/%{go_import_path}/propagators/autoprop
%{go_sys_gopath}/%{go_import_path}/propagators/aws
%{go_sys_gopath}/%{go_import_path}/propagators/b3
%{go_sys_gopath}/%{go_import_path}/propagators/jaeger
%{go_sys_gopath}/%{go_import_path}/propagators/ot
%{go_sys_gopath}/%{go_import_path}/zpages

%changelog
%autochangelog
