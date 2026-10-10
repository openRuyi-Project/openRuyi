# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           influxdb-observability
%define go_import_path  github.com/influxdata/influxdb-observability

Name:           go-github-influxdata-influxdb-observability
Version:        0.5.12
Release:        %autorelease
Summary:        OpenTelemetry conversion libraries for InfluxDB
License:        MIT
URL:            https://github.com/influxdata/influxdb-observability
#!RemoteAsset:  sha256:90c5682b6d7609c04e2751d61579017439c56c112ca19787b4389d5c6aca1ad4
Source0:        https://github.com/influxdata/influxdb-observability/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Break the runtime dependency cycle with Collector contrib.
# https://github.com/influxdata/influxdb-observability/pull/353
Patch2000:      2000-influx2otel-avoid-runtime-dependency-on-pdatautil.patch

BuildRequires:  go
BuildRequires:  go(github.com/alecthomas/participle)
BuildRequires:  go(github.com/alecthomas/units)
BuildRequires:  go(github.com/antlr/antlr4/runtime/Go/antlr/v4)
BuildRequires:  go(github.com/apache/arrow-adbc/go/adbc)
BuildRequires:  go(github.com/apache/arrow/go/v16)
BuildRequires:  go(github.com/awnumar/memcall)
BuildRequires:  go(github.com/awnumar/memguard)
BuildRequires:  go(github.com/benbjohnson/clock)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/bluele/gcache)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/compose-spec/compose-go)
BuildRequires:  go(github.com/coreos/go-semver)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-ole/go-ole)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/goccy/go-json)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/google/cel-go)
BuildRequires:  go(github.com/google/flatbuffers)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gosnmp/gosnmp)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-plugin)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/hashicorp/yamux)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/influxdata/influxdb/v2)
BuildRequires:  go(github.com/influxdata/line-protocol/v2)
BuildRequires:  go(github.com/influxdata/telegraf)
BuildRequires:  go(github.com/influxdata/toml)
BuildRequires:  go(github.com/jaegertracing/jaeger)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/klauspost/pgzip)
BuildRequires:  go(github.com/knadh/koanf)
BuildRequires:  go(github.com/knadh/koanf/v2)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/lufia/plan9stats)
BuildRequires:  go(github.com/magiconair/properties)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/go-testing-interface)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/naoina/go-stringutil)
BuildRequires:  go(github.com/oklog/run)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/influxdbexporter)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/healthcheckextension)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/common)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatatest)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatautil)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/influxdbreceiver)
BuildRequires:  go(github.com/opentracing/opentracing-go)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/power-devops/perfstat)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/prometheus/prometheus)
BuildRequires:  go(github.com/rs/cors)
BuildRequires:  go(github.com/sagikazarmark/locafero)
BuildRequires:  go(github.com/sagikazarmark/slog-shim)
BuildRequires:  go(github.com/shirou/gopsutil/v3)
BuildRequires:  go(github.com/shoenig/go-m1cpu)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/sleepinggenius2/gosmi)
BuildRequires:  go(github.com/sourcegraph/conc)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spf13/cast)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/spf13/viper)
BuildRequires:  go(github.com/stoewer/go-strcase)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/subosito/gotenv)
BuildRequires:  go(github.com/tarm/serial)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/tklauser/numcpus)
BuildRequires:  go(github.com/youmark/pkcs8)
BuildRequires:  go(github.com/yusufpapurcu/wmi)
BuildRequires:  go(github.com/zeebo/xxh3)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(go.opentelemetry.io/collector)
BuildRequires:  go(go.opentelemetry.io/collector/component)
BuildRequires:  go(go.opentelemetry.io/collector/config/configauth)
BuildRequires:  go(go.opentelemetry.io/collector/config/configcompression)
BuildRequires:  go(go.opentelemetry.io/collector/config/confighttp)
BuildRequires:  go(go.opentelemetry.io/collector/config/configopaque)
BuildRequires:  go(go.opentelemetry.io/collector/config/configretry)
BuildRequires:  go(go.opentelemetry.io/collector/config/configtelemetry)
BuildRequires:  go(go.opentelemetry.io/collector/config/configtls)
BuildRequires:  go(go.opentelemetry.io/collector/config/internal)
BuildRequires:  go(go.opentelemetry.io/collector/confmap)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/converter/expandconverter)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/envprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/fileprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/httpprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/httpsprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/yamlprovider)
BuildRequires:  go(go.opentelemetry.io/collector/connector)
BuildRequires:  go(go.opentelemetry.io/collector/consumer)
BuildRequires:  go(go.opentelemetry.io/collector/exporter)
BuildRequires:  go(go.opentelemetry.io/collector/extension)
BuildRequires:  go(go.opentelemetry.io/collector/extension/auth)
BuildRequires:  go(go.opentelemetry.io/collector/featuregate)
BuildRequires:  go(go.opentelemetry.io/collector/otelcol)
BuildRequires:  go(go.opentelemetry.io/collector/pdata)
BuildRequires:  go(go.opentelemetry.io/collector/processor)
BuildRequires:  go(go.opentelemetry.io/collector/receiver)
BuildRequires:  go(go.opentelemetry.io/collector/semconv)
BuildRequires:  go(go.opentelemetry.io/collector/service)
BuildRequires:  go(go.opentelemetry.io/contrib/config)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/contrib/propagators/b3)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/bridge/opencensus)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/prometheus)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutmetric)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.opentelemetry.io/proto/otlp)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/ini.v1)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/influxdata/influxdb-observability/common) = %{version}
Provides:       go(github.com/influxdata/influxdb-observability/influx2otel) = %{version}
Provides:       go(github.com/influxdata/influxdb-observability/jaeger-influxdb) = %{version}
Provides:       go(github.com/influxdata/influxdb-observability/jaeger-influxdb/internal) = %{version}
Provides:       go(github.com/influxdata/influxdb-observability/otel2influx) = %{version}

Requires:       go(github.com/apache/arrow-adbc/go/adbc)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/influxdata/line-protocol/v2)
Requires:       go(github.com/jaegertracing/jaeger)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatautil)
Requires:       go(github.com/opentracing/opentracing-go)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/viper)
Requires:       go(go.opentelemetry.io/collector)
Requires:       go(go.opentelemetry.io/collector/consumer)
Requires:       go(go.opentelemetry.io/collector/pdata)
Requires:       go(go.opentelemetry.io/collector/semconv)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/exp)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go modules from the InfluxDB observability
repository, including the Jaeger storage adapter and integration tests.

%install
# Install each module at its declared import path. Remove nested module
# copies from each parent before installing them at their own paths.
while read -r _source _import _children; do
    _target="%{buildroot}%{go_sys_gopath}/${_import}"
    install -d "${_target}"
    cp -aL "${_source}"/. "${_target}/"
    for _child in ${_children}; do
        rm -rf "${_target}/${_child}"
    done
done <<'GO_MODULES'
common github.com/influxdata/influxdb-observability/common
influx2otel github.com/influxdata/influxdb-observability/influx2otel
jaeger-influxdb github.com/influxdata/influxdb-observability/jaeger-influxdb
otel2influx github.com/influxdata/influxdb-observability/otel2influx
GO_MODULES

%check
%go_common
# Test the installed layout, including nested modules, without loading a
# second copy of the repository or using the system's older source package.
install -d "%{_builddir}/go/src"
cp -a "%{buildroot}%{go_sys_gopath}/." "%{_builddir}/go/src/"
_go_packages=$(go list -e -f '{{.ImportPath}}' github.com/influxdata/influxdb-observability/...)
_go_packages=$(printf '%s\n' "${_go_packages}" | sort -u)
_go_tests=
set -f
for _package in ${_go_packages}; do
    _skip=0
    for _exclude in %{?go_test_exclude}; do
        if [ "${_package}" = "${_exclude}" ]; then _skip=1; fi
    done
    for _exclude in %{?go_test_exclude_glob}; do
        case "${_package}" in ${_exclude}) _skip=1 ;; esac
    done
    [ "${_skip}" -eq 1 ] || _go_tests="${_go_tests} ${_package}"
done
set +f
test -n "${_go_tests}"
go test %{go_test_flags_default} ${_go_tests}

# This local-named module exercises the installed libraries and services.
pushd tests-integration
go test %{go_test_flags_default} ./...
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
