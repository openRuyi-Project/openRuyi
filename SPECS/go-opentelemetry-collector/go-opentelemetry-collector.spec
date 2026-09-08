# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-collector
%define go_import_path  go.opentelemetry.io/collector
# Builder, metadata generator, and schema generator tests invoke module-aware
# Go commands, which cannot run in the offline GOPATH package build.
# configtls tests additionally require the optional C-based TPM simulator.
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/cmd/builder*
    %{go_import_path}/cmd/mdatagen*
    %{go_import_path}/config/configtls*
    %{go_import_path}/internal/schemagen*
}

Name:           go-opentelemetry-collector
Version:        0.154.0
Release:        %autorelease
Summary:        Complete OpenTelemetry Collector source tree
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector
#!RemoteAsset:  sha256:f9fb0b1fb90c0326362244b7e2986c2efc3d84c15a38a8ab187477ef52b281bc
Source0:        https://github.com/open-telemetry/opentelemetry-collector/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Correct stale package import comments left behind by upstream source moves.
Patch1:         2000-correct-stale-test-import-comments.patch
# Correct the remaining stale comments in the telemetry test package.
Patch2:         2001-correct-telemetry-test-import-comments.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/cenkalti/backoff)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/ettle/strcase)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/foxboron/go-tpm-keyfiles)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-tpm)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/hashicorp/golang-lru/v2)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/knadh/koanf/parsers/yaml)
BuildRequires:  go(github.com/knadh/koanf/providers/confmap)
BuildRequires:  go(github.com/knadh/koanf/providers/env/v2)
BuildRequires:  go(github.com/knadh/koanf/providers/file)
BuildRequires:  go(github.com/knadh/koanf/providers/fs)
BuildRequires:  go(github.com/knadh/koanf/v2)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/otlptranslator)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/rs/cors)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(github.com/shirou/gopsutil)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/tklauser/numcpus)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/prometheus)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutlog)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutmetric)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
BuildRequires:  go(go.opentelemetry.io/otel/log)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/log)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.opentelemetry.io/proto)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(go.opentelemetry.io/collector/client) = %{version}
Provides:       go(go.opentelemetry.io/collector/cmd/builder) = %{version}
Provides:       go(go.opentelemetry.io/collector/cmd/mdatagen) = %{version}
Provides:       go(go.opentelemetry.io/collector/cmd/otelcorecol) = %{version}
Provides:       go(go.opentelemetry.io/collector/component) = %{version}
Provides:       go(go.opentelemetry.io/collector/component/componentstatus) = %{version}
Provides:       go(go.opentelemetry.io/collector/component/componenttest) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/configauth) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/configcompression) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/configgrpc) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/confighttp) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/confighttp/xconfighttp) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/configmiddleware) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/confignet) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/configopaque) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/configoptional) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/configretry) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/configtelemetry) = %{version}
Provides:       go(go.opentelemetry.io/collector/config/configtls) = %{version}
Provides:       go(go.opentelemetry.io/collector/confmap) = %{version}
Provides:       go(go.opentelemetry.io/collector/confmap/internal/e2e) = %{version}
Provides:       go(go.opentelemetry.io/collector/confmap/provider/envprovider) = %{version}
Provides:       go(go.opentelemetry.io/collector/confmap/provider/fileprovider) = %{version}
Provides:       go(go.opentelemetry.io/collector/confmap/provider/httpprovider) = %{version}
Provides:       go(go.opentelemetry.io/collector/confmap/provider/httpsprovider) = %{version}
Provides:       go(go.opentelemetry.io/collector/confmap/provider/yamlprovider) = %{version}
Provides:       go(go.opentelemetry.io/collector/confmap/xconfmap) = %{version}
Provides:       go(go.opentelemetry.io/collector/connector) = %{version}
Provides:       go(go.opentelemetry.io/collector/connector/connectortest) = %{version}
Provides:       go(go.opentelemetry.io/collector/connector/forwardconnector) = %{version}
Provides:       go(go.opentelemetry.io/collector/connector/xconnector) = %{version}
Provides:       go(go.opentelemetry.io/collector/consumer) = %{version}
Provides:       go(go.opentelemetry.io/collector/consumer/consumererror) = %{version}
Provides:       go(go.opentelemetry.io/collector/consumer/consumererror/xconsumererror) = %{version}
Provides:       go(go.opentelemetry.io/collector/consumer/consumertest) = %{version}
Provides:       go(go.opentelemetry.io/collector/consumer/xconsumer) = %{version}
Provides:       go(go.opentelemetry.io/collector/exporter) = %{version}
Provides:       go(go.opentelemetry.io/collector/exporter/debugexporter) = %{version}
Provides:       go(go.opentelemetry.io/collector/exporter/exporterhelper) = %{version}
Provides:       go(go.opentelemetry.io/collector/exporter/exporterhelper/xexporterhelper) = %{version}
Provides:       go(go.opentelemetry.io/collector/exporter/exportertest) = %{version}
Provides:       go(go.opentelemetry.io/collector/exporter/nopexporter) = %{version}
Provides:       go(go.opentelemetry.io/collector/exporter/otlpexporter) = %{version}
Provides:       go(go.opentelemetry.io/collector/exporter/otlphttpexporter) = %{version}
Provides:       go(go.opentelemetry.io/collector/exporter/xexporter) = %{version}
Provides:       go(go.opentelemetry.io/collector/extension) = %{version}
Provides:       go(go.opentelemetry.io/collector/extension/extensionauth) = %{version}
Provides:       go(go.opentelemetry.io/collector/extension/extensionauth/extensionauthtest) = %{version}
Provides:       go(go.opentelemetry.io/collector/extension/extensioncapabilities) = %{version}
Provides:       go(go.opentelemetry.io/collector/extension/extensionmiddleware) = %{version}
Provides:       go(go.opentelemetry.io/collector/extension/extensionmiddleware/extensionmiddlewaretest) = %{version}
Provides:       go(go.opentelemetry.io/collector/extension/extensiontest) = %{version}
Provides:       go(go.opentelemetry.io/collector/extension/memorylimiterextension) = %{version}
Provides:       go(go.opentelemetry.io/collector/extension/xextension) = %{version}
Provides:       go(go.opentelemetry.io/collector/extension/zpagesextension) = %{version}
Provides:       go(go.opentelemetry.io/collector/featuregate) = %{version}
Provides:       go(go.opentelemetry.io/collector/filter) = %{version}
Provides:       go(go.opentelemetry.io/collector/internal/cmd/pdatagen) = %{version}
Provides:       go(go.opentelemetry.io/collector/internal/componentalias) = %{version}
Provides:       go(go.opentelemetry.io/collector/internal/e2e) = %{version}
Provides:       go(go.opentelemetry.io/collector/internal/fanoutconsumer) = %{version}
Provides:       go(go.opentelemetry.io/collector/internal/memorylimiter) = %{version}
Provides:       go(go.opentelemetry.io/collector/internal/schemagen) = %{version}
Provides:       go(go.opentelemetry.io/collector/internal/sharedcomponent) = %{version}
Provides:       go(go.opentelemetry.io/collector/internal/telemetry) = %{version}
Provides:       go(go.opentelemetry.io/collector/internal/testutil) = %{version}
Provides:       go(go.opentelemetry.io/collector/internal/tools) = %{version}
Provides:       go(go.opentelemetry.io/collector/otelcol) = %{version}
Provides:       go(go.opentelemetry.io/collector/otelcol/otelcoltest) = %{version}
Provides:       go(go.opentelemetry.io/collector/pdata) = %{version}
Provides:       go(go.opentelemetry.io/collector/pdata/pprofile) = %{version}
Provides:       go(go.opentelemetry.io/collector/pdata/testdata) = %{version}
Provides:       go(go.opentelemetry.io/collector/pdata/xpdata) = %{version}
Provides:       go(go.opentelemetry.io/collector/pipeline) = %{version}
Provides:       go(go.opentelemetry.io/collector/pipeline/xpipeline) = %{version}
Provides:       go(go.opentelemetry.io/collector/processor) = %{version}
Provides:       go(go.opentelemetry.io/collector/processor/batchprocessor) = %{version}
Provides:       go(go.opentelemetry.io/collector/processor/memorylimiterprocessor) = %{version}
Provides:       go(go.opentelemetry.io/collector/processor/processorhelper) = %{version}
Provides:       go(go.opentelemetry.io/collector/processor/processorhelper/xprocessorhelper) = %{version}
Provides:       go(go.opentelemetry.io/collector/processor/processortest) = %{version}
Provides:       go(go.opentelemetry.io/collector/processor/xprocessor) = %{version}
Provides:       go(go.opentelemetry.io/collector/receiver) = %{version}
Provides:       go(go.opentelemetry.io/collector/receiver/nopreceiver) = %{version}
Provides:       go(go.opentelemetry.io/collector/receiver/otlpreceiver) = %{version}
Provides:       go(go.opentelemetry.io/collector/receiver/receiverhelper) = %{version}
Provides:       go(go.opentelemetry.io/collector/receiver/receivertest) = %{version}
Provides:       go(go.opentelemetry.io/collector/receiver/xreceiver) = %{version}
Provides:       go(go.opentelemetry.io/collector/scraper) = %{version}
Provides:       go(go.opentelemetry.io/collector/scraper/scraperhelper) = %{version}
Provides:       go(go.opentelemetry.io/collector/scraper/scraperhelper/xscraperhelper) = %{version}
Provides:       go(go.opentelemetry.io/collector/scraper/scrapertest) = %{version}
Provides:       go(go.opentelemetry.io/collector/scraper/xscraper) = %{version}
Provides:       go(go.opentelemetry.io/collector/service) = %{version}
Provides:       go(go.opentelemetry.io/collector/service/hostcapabilities) = %{version}
Provides:       go(go.opentelemetry.io/collector/service/telemetry/telemetrytest) = %{version}

Obsoletes:      go-opentelemetry-collector-component < 2
Obsoletes:      go-opentelemetry-collector-confmap < 2
Obsoletes:      go-opentelemetry-collector-confmap-xconfmap < 2
Obsoletes:      go-opentelemetry-collector-consumer < 2
Obsoletes:      go-opentelemetry-collector-consumer-consumertest < 2
Obsoletes:      go-opentelemetry-collector-featuregate < 2
Obsoletes:      go-opentelemetry-collector-internal-componentalias < 2
Obsoletes:      go-opentelemetry-collector-internal-testutil < 2
Obsoletes:      go-opentelemetry-collector-pdata < 2
Obsoletes:      go-opentelemetry-collector-pipeline < 2
Obsoletes:      go-opentelemetry-collector-processor < 2

Requires:       go(github.com/Microsoft/go-winio)
Requires:       go(github.com/beorn7/perks)
Requires:       go(github.com/cenkalti/backoff)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/ettle/strcase)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/foxboron/go-tpm-keyfiles)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/gobwas/glob)
Requires:       go(github.com/golang/snappy)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-tpm)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(github.com/hashicorp/go-version)
Requires:       go(github.com/hashicorp/golang-lru/v2)
Requires:       go(github.com/inconshreveable/mousetrap)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/knadh/koanf/maps)
Requires:       go(github.com/knadh/koanf/parsers/yaml)
Requires:       go(github.com/knadh/koanf/providers/confmap)
Requires:       go(github.com/knadh/koanf/providers/env/v2)
Requires:       go(github.com/knadh/koanf/providers/file)
Requires:       go(github.com/knadh/koanf/providers/fs)
Requires:       go(github.com/knadh/koanf/v2)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/kr/text)
Requires:       go(github.com/mitchellh/copystructure)
Requires:       go(github.com/mitchellh/reflectwalk)
Requires:       go(github.com/modern-go/concurrent)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(github.com/munnerz/goautoneg)
Requires:       go(github.com/pierrec/lz4/v4)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/otlptranslator)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(github.com/rs/cors)
Requires:       go(github.com/santhosh-tekuri/jsonschema/v6)
Requires:       go(github.com/shirou/gopsutil)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/tklauser/go-sysconf)
Requires:       go(github.com/tklauser/numcpus)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib)
Requires:       go(go.opentelemetry.io/otel)
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
Requires:       go(go.opentelemetry.io/proto)
Requires:       go(go.uber.org/goleak)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(gonum.org/v1/gonum)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/check.v1)
Requires:       go(gopkg.in/yaml.v3)

%description
This package provides the complete Go source tree for the OpenTelemetry
Collector, including its nested modules and test support packages.

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}"
cp -a ./. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/"

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
# synctest requires the current timer channel implementation, while HTTP
# method/path pattern tests require the Go 1.22 ServeMux behavior.
export GODEBUG="${GODEBUG:+${GODEBUG},}asynctimerchan=0,httpmuxgo121=0"
install -d "%{_builddir}/go/src/%{go_import_path}"
cp -a ./. "%{_builddir}/go/src/%{go_import_path}/"
pushd "%{_builddir}/go/src/%{go_import_path}"
while IFS= read -r -d '' _go_mod; do
    _module_dir=${_go_mod%/go.mod}
    pushd "${_module_dir}"
    _go_all_pkgs=$(go list -e -f '{{.ImportPath}}' ./...)
    _go_pkgs=
    set -f
    for _go_pkg in ${_go_all_pkgs}; do
        case "${_go_pkg}" in
            %{go_import_path}|%{go_import_path}/*) ;;
            *) continue ;;
        esac
        _go_skip=0
        for _go_pattern in %{go_test_exclude_glob}; do
            case "${_go_pkg}" in
                ${_go_pattern}) _go_skip=1; break ;;
            esac
        done
        [ "${_go_skip}" -eq 0 ] && _go_pkgs="${_go_pkgs} ${_go_pkg}"
    done
    set +f
    if [ -n "${_go_pkgs}" ]; then
        # Several package tests bind fixed localhost ports.
        go test -p 1 -v ${_go_pkgs}
    fi
    popd
done < <(find . -name go.mod -print0 | sort -z)
popd

%files
%doc CHANGELOG-API.md CHANGELOG.md CONTRIBUTING.md README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
