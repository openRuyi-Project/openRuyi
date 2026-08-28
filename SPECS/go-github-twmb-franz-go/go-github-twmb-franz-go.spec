# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           franz-go
%define go_import_path  github.com/twmb/franz-go

Name:           go-github-twmb-franz-go
Version:        1.21.2
Release:        %autorelease
Summary:        Kafka client library for Go
License:        BSD-3-Clause
URL:            https://github.com/twmb/franz-go
#!RemoteAsset:  sha256:9ba4d0706561168a132d70be847a0fa86dd85d45755ccfa6e4c7993e5703606c
Source0:        https://github.com/twmb/franz-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Align the kotel test with the semantic conventions used by its implementation.
# https://github.com/twmb/franz-go/commit/d912a2c5b2db006c3606c0b98fd1a7a6b3b94979
Patch0:         1000-align-kotel-test-semantic-conventions.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/jcmturner/gokrb5/v8)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/phuslu/log)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/rcrowley/go-metrics)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/VictoriaMetrics/metrics)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/twmb/franz-go) = %{version}

Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/jcmturner/gokrb5/v8)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/phuslu/log)
Requires:       go(github.com/pierrec/lz4/v4)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/rcrowley/go-metrics)
Requires:       go(github.com/rs/zerolog)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/VictoriaMetrics/metrics)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/crypto)

%description
Franz-go is a Kafka client library for Go. This package bundles its root
module, public package modules, Kerberos support, and logging, metrics, and
tracing plugins from one repository snapshot.

%check
%go_common
# srfake uses Go 1.22+ ServeMux method and path patterns.
export GODEBUG="${GODEBUG:+${GODEBUG},}httpmuxgo121=0"
install -d %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}

# Run the upstream in-repository Kafka simulator for the kgo integration tests.
_kfake_cmd=%{_builddir}/go/src/github.com/twmb/franz-kfake
install -d "${_kfake_cmd}"
# The upstream command is build-tagged out of the kfake library directory.
# Copy its entry point to a standalone GOPATH command for this test run.
tail -n +2 pkg/kfake/main.go >"${_kfake_cmd}/main.go"
_kfake_log=%{_builddir}/franz-kfake.log
go run github.com/twmb/franz-kfake --as-version 4.1 \
    -c group.consumer.heartbeat.interval.ms=1000 -l error \
    >"${_kfake_log}" 2>&1 &
_kfake_pid=$!
trap 'kill "$_kfake_pid" 2>/dev/null || true' EXIT
_kfake_ready=0
for _attempt in $(seq 1 60); do
    if bash -c 'exec 3<>/dev/tcp/127.0.0.1/9092' 2>/dev/null; then
        _kfake_ready=1
        break
    fi
    if ! kill -0 "$_kfake_pid" 2>/dev/null; then
        cat "${_kfake_log}"
        exit 1
    fi
    sleep 0.5
done
if [ "$_kfake_ready" -ne 1 ]; then
    cat "${_kfake_log}"
    exit 1
fi

KGO_TEST_RF=1 KGO_SEEDS=127.0.0.1:9092 go test -v -timeout 5m \
    %{go_import_path}/generate \
    %{go_import_path}/pkg/kadm/... \
    %{go_import_path}/pkg/kbin \
    %{go_import_path}/pkg/kerr \
    %{go_import_path}/pkg/kfake/... \
    %{go_import_path}/pkg/kgo/... \
    %{go_import_path}/pkg/kmsg/... \
    %{go_import_path}/pkg/kversion \
    %{go_import_path}/pkg/sasl \
    %{go_import_path}/pkg/sasl/aws \
    %{go_import_path}/pkg/sasl/kerberos \
    %{go_import_path}/pkg/sasl/oauth \
    %{go_import_path}/pkg/sasl/plain \
    %{go_import_path}/pkg/sasl/scram \
    %{go_import_path}/pkg/sr/... \
    %{go_import_path}/plugin/...

%files
%doc CHANGELOG.md DESIGN.md README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
