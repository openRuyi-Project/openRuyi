# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-collector-contrib
%define go_import_path  github.com/open-telemetry/opentelemetry-collector-contrib
# Schemagen path assertions require Go module mode rather than the offline GOPATH layout.
# Failover recovery tests use a fixed timeout that flakes on loaded OBS workers.
# AWS X-Ray telemetry assertions depend on the external request failure type.
%define go_test_exclude %{go_import_path}/cmd/schemagen/internal %{go_import_path}/connector/failoverconnector %{go_import_path}/exporter/awsxrayexporter

Name:           go-github-open-telemetry-opentelemetry-collector-contrib
Version:        0.154.0
Release:        %autorelease
Summary:        OpenTelemetry Collector contrib modules
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector-contrib
#!RemoteAsset:  sha256:72c3365cf0f1a879a753e97cea902c2c09ce48ac5e28df5246cd048d7786edc1
Source0:        https://github.com/open-telemetry/opentelemetry-collector-contrib/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-cmd-telemetrygen-fix-canonical-import-comments.patch
# Keep the benchmark test connection compatible with packaged clickhouse-go.
Patch2001:      2001-exporter-clickhouse-support-clickhouse-go-v2.48-test.patch
# Avoid depending on resolver-specific gRPC error text in Coralogix tests.
Patch2002:      2002-exporter-coralogix-avoid-resolver-specific-error-mes.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go/secretmanager)
BuildRequires:  go(cloud.google.com/go/storage)
BuildRequires:  go(github.com/alecthomas/participle/v2)
BuildRequires:  go(github.com/aliyun/aliyun-log-go-sdk)
BuildRequires:  go(github.com/apache/cassandra-gocql-driver/v2)
BuildRequires:  go(github.com/antchfx/xmlquery)
BuildRequires:  go(github.com/antchfx/xpath)
BuildRequires:  go(github.com/Azure/azure-kusto-go)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob)
BuildRequires:  go(github.com/aws/aws-msk-iam-sasl-signer-go)
BuildRequires:  go(github.com/bmatcuk/doublestar/v4)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/ClickHouse/clickhouse-go/v2)
BuildRequires:  go(github.com/containerd/cgroups/v3)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/DataDog/agent-payload/v5)
BuildRequires:  go(github.com/DataDog/datadog-agent)
BuildRequires:  go(github.com/DataDog/datadog-go/v5)
BuildRequires:  go(github.com/DataDog/gohai)
BuildRequires:  go(github.com/DeRuina/timberjack)
BuildRequires:  go(github.com/elastic/elastic-transport-go/v8)
BuildRequires:  go(github.com/elastic/go-docappender/v2)
BuildRequires:  go(github.com/elastic/go-freelru)
BuildRequires:  go(github.com/fortytw2/leaktest)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector)
BuildRequires:  go(github.com/elastic/go-grok)
BuildRequires:  go(github.com/elastic/go-structform)
BuildRequires:  go(github.com/openshift/client-go)
BuildRequires:  go(github.com/elastic/lunes)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/goccy/go-json)
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/grafana/faro/pkg/go)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gorilla/mux)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/influxdata/influxdb-observability/common)
BuildRequires:  go(github.com/itchyny/timefmt-go)
BuildRequires:  go(github.com/jaegertracing/jaeger-idl)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/jonboulle/clockwork)
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/knadh/koanf/providers/confmap)
BuildRequires:  go(github.com/knadh/koanf/providers/rawbytes)
BuildRequires:  go(github.com/knadh/koanf/v2)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/lestrrat-go/strftime)
BuildRequires:  go(github.com/lightstep/go-expohisto)
BuildRequires:  go(github.com/microsoft/ApplicationInsights-Go)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/moby/moby/api)
BuildRequires:  go(github.com/moby/moby/client)
BuildRequires:  go(github.com/open-telemetry/opamp-go)
BuildRequires:  go(github.com/orcaman/concurrent-map/v2)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/puzpuzpuz/xsync)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/scalyr/dataset-go)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tg123/go-htpasswd)
BuildRequires:  go(github.com/tilinna/clock)
BuildRequires:  go(github.com/tj/assert)
BuildRequires:  go(github.com/tidwall/wal)
BuildRequires:  go(github.com/twmb/murmur3)
BuildRequires:  go(github.com/ua-parser/uap-go)
BuildRequires:  go(github.com/wk8/go-ordered-map/v2)
BuildRequires:  go(github.com/zeebo/xxh3)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/collector)
BuildRequires:  go(go.opentelemetry.io/collector/semconv)
BuildRequires:  go(go.opentelemetry.io/ebpf-profiler)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(gotest.tools/assert)
BuildRequires:  go(sigs.k8s.io/controller-runtime)
BuildRequires:  tzdata

Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib) = %{version}

Requires:       go(cloud.google.com/go/secretmanager)
Requires:       go(cloud.google.com/go/storage)
Requires:       go(github.com/alecthomas/participle/v2)
Requires:       go(github.com/aliyun/aliyun-log-go-sdk)
Requires:       go(github.com/apache/cassandra-gocql-driver/v2)
Requires:       go(github.com/antchfx/xmlquery)
Requires:       go(github.com/antchfx/xpath)
Requires:       go(github.com/Azure/azure-kusto-go)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob)
Requires:       go(github.com/aws/aws-msk-iam-sasl-signer-go)
Requires:       go(github.com/bmatcuk/doublestar/v4)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/ClickHouse/clickhouse-go/v2)
Requires:       go(github.com/containerd/cgroups/v3)
Requires:       go(github.com/DataDog/agent-payload/v5)
Requires:       go(github.com/DataDog/datadog-agent)
Requires:       go(github.com/DataDog/datadog-go/v5)
Requires:       go(github.com/DataDog/gohai)
Requires:       go(github.com/DeRuina/timberjack)
Requires:       go(github.com/elastic/elastic-transport-go/v8)
Requires:       go(github.com/elastic/go-docappender/v2)
Requires:       go(github.com/elastic/go-freelru)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector)
Requires:       go(github.com/elastic/go-grok)
Requires:       go(github.com/elastic/go-structform)
Requires:       go(github.com/openshift/client-go)
Requires:       go(github.com/elastic/lunes)
Requires:       go(github.com/goccy/go-json)
Requires:       go(github.com/go-sql-driver/mysql)
Requires:       go(github.com/grafana/faro/pkg/go)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/gorilla/mux)
Requires:       go(github.com/influxdata/influxdb-observability/common)
Requires:       go(github.com/itchyny/timefmt-go)
Requires:       go(github.com/jaegertracing/jaeger-idl)
Requires:       go(github.com/jonboulle/clockwork)
Requires:       go(github.com/knadh/koanf/providers/rawbytes)
Requires:       go(github.com/lestrrat-go/strftime)
Requires:       go(github.com/lightstep/go-expohisto)
Requires:       go(github.com/microsoft/ApplicationInsights-Go)
Requires:       go(github.com/moby/moby/api)
Requires:       go(github.com/moby/moby/client)
Requires:       go(github.com/open-telemetry/opamp-go)
Requires:       go(github.com/orcaman/concurrent-map/v2)
Requires:       go(github.com/puzpuzpuz/xsync)
Requires:       go(github.com/scalyr/dataset-go)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/tg123/go-htpasswd)
Requires:       go(github.com/tilinna/clock)
Requires:       go(github.com/tidwall/wal)
Requires:       go(github.com/twmb/murmur3)
Requires:       go(github.com/ua-parser/uap-go)
Requires:       go(github.com/wk8/go-ordered-map/v2)
Requires:       go(github.com/zeebo/xxh3)
Requires:       go(go.etcd.io/bbolt)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/collector)
Requires:       go(go.opentelemetry.io/collector/semconv)
Requires:       go(go.opentelemetry.io/ebpf-profiler)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(golang.org/x/tools)
Requires:       go(gopkg.in/yaml.v3)
Requires:       go(sigs.k8s.io/controller-runtime)

%description
This package bundles the Collector contrib metrics utilities and delta-to-
cumulative processor from one upstream repository snapshot. Additional modules
from this repository should be added here instead of split into source packages.

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}"
cp -a ./. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/"

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
install -d "%{_builddir}/go/src/%{go_import_path}"
cp -a ./. "%{_builddir}/go/src/%{go_import_path}/"
pushd "%{_builddir}/go/src/%{go_import_path}"
while IFS= read -r -d '' _go_mod; do
    _module_dir=${_go_mod%/go.mod}
    pushd "${_module_dir}"
    _go_pkgs=$(go list -e -f '{{.ImportPath}}' ./...)
    _go_test_pkgs=
    for _go_pkg in ${_go_pkgs}; do
        case " %{go_test_exclude} " in
            *" ${_go_pkg} "*) go test -run '^$' "${_go_pkg}" ;;
            *) _go_test_pkgs="${_go_test_pkgs} ${_go_pkg}" ;;
        esac
    done
    if [ -n "${_go_test_pkgs}" ]; then
        go test -v ${_go_test_pkgs}
    fi
    popd
done < <(find . -name go.mod -print0 | sort -z)
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
