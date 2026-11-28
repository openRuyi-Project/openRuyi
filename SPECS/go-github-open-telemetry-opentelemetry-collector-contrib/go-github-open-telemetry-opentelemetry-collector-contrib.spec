# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-collector-contrib
%define go_import_path  github.com/open-telemetry/%{_name}
%define go_modules      internal/exp/metrics pkg/pdatautil processor/deltatocumulativeprocessor

Name:           go-github-open-telemetry-opentelemetry-collector-contrib
Version:        0.154.0
Release:        %autorelease
Summary:        OpenTelemetry Collector Contrib metrics processor and helpers
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector-contrib
#!RemoteAsset:  sha256:72c3365cf0f1a879a753e97cea902c2c09ce48ac5e28df5246cd048d7786edc1
Source0:        https://github.com/open-telemetry/opentelemetry-collector-contrib/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go >= 1.25
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/knadh/koanf/providers/confmap)
BuildRequires:  go(github.com/knadh/koanf/v2)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/puzpuzpuz/xsync/v4)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/collector/component)
BuildRequires:  go(go.opentelemetry.io/collector/component/componentstatus)
BuildRequires:  go(go.opentelemetry.io/collector/component/componenttest)
BuildRequires:  go(go.opentelemetry.io/collector/confmap)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/xconfmap)
BuildRequires:  go(go.opentelemetry.io/collector/consumer)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumertest)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/xconsumer)
BuildRequires:  go(go.opentelemetry.io/collector/featuregate)
BuildRequires:  go(go.opentelemetry.io/collector/internal/componentalias)
BuildRequires:  go(go.opentelemetry.io/collector/pdata)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/pprofile)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/testdata)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/xpdata)
BuildRequires:  go(go.opentelemetry.io/collector/pipeline)
BuildRequires:  go(go.opentelemetry.io/collector/processor)
BuildRequires:  go(go.opentelemetry.io/collector/processor/processortest)
BuildRequires:  go(go.opentelemetry.io/collector/processor/xprocessor)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(%{go_import_path}/internal/exp/metrics) = %{version}
Provides:       go(%{go_import_path}/pkg/pdatautil) = %{version}
Provides:       go(%{go_import_path}/processor/deltatocumulativeprocessor) = %{version}

Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/puzpuzpuz/xsync/v4)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.opentelemetry.io/collector/component)
Requires:       go(go.opentelemetry.io/collector/component/componenttest)
Requires:       go(go.opentelemetry.io/collector/confmap/xconfmap)
Requires:       go(go.opentelemetry.io/collector/consumer)
Requires:       go(go.opentelemetry.io/collector/pdata)
Requires:       go(go.opentelemetry.io/collector/processor)
Requires:       go(go.opentelemetry.io/collector/processor/processortest)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/tools)
Requires:       go(go.yaml.in/yaml/v3)

%description
Go source for the delta-to-cumulative metrics processor and its supporting
modules from OpenTelemetry Collector Contrib.

%install
# Install the three modules in Prometheus's import closure under their
# upstream paths so that Go's internal package imports keep working.
for module in %{go_modules}; do
    target=%{buildroot}%{go_sys_gopath}/%{go_import_path}/$module
    install -d "$target"
    cp -a "$module/." "$target/"
done

%check
# The three upstream tags share this source revision. The metrics tests
# import golden and pdatatest from it, so add them only to the test GOPATH.
%go_common
for module in %{go_modules} pkg/golden pkg/pdatatest; do
    target=%{_builddir}/go/src/%{go_import_path}/$module
    install -d "$target"
    cp -a "$module/." "$target/"
done
for module in %{go_modules}; do
    %{__go} test %{go_test_flags_default} "%{go_import_path}/$module/..."
done

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
