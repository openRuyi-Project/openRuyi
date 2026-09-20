# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           franz-go
%define go_import_path  github.com/twmb/franz-go
# Use an upstream round-trip test as a smoke test. It temporarily starts a
# simulated Kafka broker, produces and consumes records, checks their values
# and headers, and closes the broker and clients when the test finishes.
%define go_test_include  %{go_import_path}/pkg/kfake

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
Patch1000:      1000-align-kotel-test-semantic-conventions.patch

BuildOption(check):  -run '^TestConsumeRecordHeaders$' -count=1 -timeout 1m

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

%files
%doc CHANGELOG.md DESIGN.md README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
