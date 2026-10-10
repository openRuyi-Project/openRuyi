# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           faro
%define go_import_path  github.com/grafana/faro/pkg/go
%define commit_id       bb5f9417df83f79eb88449cff5ab1b7ca65531f4

Name:           go-github-grafana-faro-pkg-go
Version:        0+git20260819.bb5f941
Release:        %autorelease
Summary:        Go models for Grafana Faro telemetry
License:        Apache-2.0
URL:            https://github.com/grafana/faro
#!RemoteAsset:  sha256:b6e76f4aa0fef747e393bc8430fc9f2912f354e7161244ac1a959ee3206d2a82
Source0:        https://github.com/grafana/faro/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go(github.com/apapsch/go-jsonmerge/v2)
BuildRequires:  go(github.com/bahlo/generic-list-go)
BuildRequires:  go(github.com/buger/jsonparser)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-logfmt/logfmt)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/knadh/koanf/providers/confmap)
BuildRequires:  go(github.com/knadh/koanf/v2)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/oapi-codegen/runtime)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/faro)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rs/cors)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/wk8/go-ordered-map/v2)
BuildRequires:  go(github.com/zeebo/xxh3)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/collector)
BuildRequires:  go(go.opentelemetry.io/collector/client)
BuildRequires:  go(go.opentelemetry.io/collector/component)
BuildRequires:  go(go.opentelemetry.io/collector/component/componentstatus)
BuildRequires:  go(go.opentelemetry.io/collector/component/componenttest)
BuildRequires:  go(go.opentelemetry.io/collector/config/configauth)
BuildRequires:  go(go.opentelemetry.io/collector/config/configcompression)
BuildRequires:  go(go.opentelemetry.io/collector/config/confighttp)
BuildRequires:  go(go.opentelemetry.io/collector/config/configopaque)
BuildRequires:  go(go.opentelemetry.io/collector/config/configretry)
BuildRequires:  go(go.opentelemetry.io/collector/config/configtelemetry)
BuildRequires:  go(go.opentelemetry.io/collector/config/configtls)
BuildRequires:  go(go.opentelemetry.io/collector/confmap)
BuildRequires:  go(go.opentelemetry.io/collector/consumer)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumererror)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumertest)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/xconsumer)
BuildRequires:  go(go.opentelemetry.io/collector/exporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/exportertest)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/xexporter)
BuildRequires:  go(go.opentelemetry.io/collector/extension)
BuildRequires:  go(go.opentelemetry.io/collector/extension/auth)
BuildRequires:  go(go.opentelemetry.io/collector/extension/xextension)
BuildRequires:  go(go.opentelemetry.io/collector/featuregate)
BuildRequires:  go(go.opentelemetry.io/collector/pdata)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/pprofile)
BuildRequires:  go(go.opentelemetry.io/collector/pipeline)
BuildRequires:  go(go.opentelemetry.io/collector/receiver)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/receivertest)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/xreceiver)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/grafana/faro/pkg/exporter/faroexporter) = %{version}
Provides:       go(github.com/grafana/faro/pkg/exporter/faroexporter/internal/httphelper) = %{version}
Provides:       go(github.com/grafana/faro/pkg/exporter/faroexporter/internal/metadata) = %{version}
Provides:       go(github.com/grafana/faro/pkg/go) = %{version}
Provides:       go(github.com/grafana/faro/pkg/receiver/faroreceiver) = %{version}
Provides:       go(github.com/grafana/faro/pkg/receiver/faroreceiver/internal/httphelper) = %{version}
Provides:       go(github.com/grafana/faro/pkg/receiver/faroreceiver/internal/metadata) = %{version}
Provides:       go(github.com/grafana/faro/pkg/receiver/faroreceiver/internal/sharedcomponent) = %{version}

Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/oapi-codegen/runtime)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/faro)
Requires:       go(go.opentelemetry.io/collector)
Requires:       go(go.opentelemetry.io/collector/component)
Requires:       go(go.opentelemetry.io/collector/component/componentstatus)
Requires:       go(go.opentelemetry.io/collector/config/configcompression)
Requires:       go(go.opentelemetry.io/collector/config/confighttp)
Requires:       go(go.opentelemetry.io/collector/config/configretry)
Requires:       go(go.opentelemetry.io/collector/confmap)
Requires:       go(go.opentelemetry.io/collector/consumer)
Requires:       go(go.opentelemetry.io/collector/consumer/consumererror)
Requires:       go(go.opentelemetry.io/collector/exporter)
Requires:       go(go.opentelemetry.io/collector/pdata)
Requires:       go(go.opentelemetry.io/collector/pdata/pprofile)
Requires:       go(go.opentelemetry.io/collector/receiver)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)

%description
This package provides generated Go models and OpenTelemetry conversion code
for Grafana Faro frontend telemetry, together with the Faro exporter and
receiver modules from the same repository snapshot.

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
pkg/go github.com/grafana/faro/pkg/go
pkg/exporter/faroexporter github.com/grafana/faro/pkg/exporter/faroexporter
pkg/receiver/faroreceiver github.com/grafana/faro/pkg/receiver/faroreceiver
GO_MODULES

%check
%go_common
# Test the installed layout, including nested modules, without loading a
# second copy of the repository or using the system's older source package.
install -d "%{_builddir}/go/src"
cp -a "%{buildroot}%{go_sys_gopath}/." "%{_builddir}/go/src/"
_go_packages=$(go list -e -f '{{.ImportPath}}' github.com/grafana/faro/...)
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

%files
%license LICENSE
%{go_sys_gopath}/github.com/grafana/faro

%changelog
%autochangelog
