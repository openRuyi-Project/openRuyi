# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sarama
%define go_import_path  github.com/IBM/sarama
# The HTTP example has an environment-dependent response, while the other
# packages remain fully tested. - HNO3Miracle
%define go_test_exclude %{go_import_path}/examples/http_server

Name:           go-github-ibm-sarama
Version:        1.60.1
Release:        %autorelease
Summary:        Apache Kafka client library for Go
License:        MIT
URL:            https://github.com/IBM/sarama
#!RemoteAsset:  sha256:4408163337f16275c2f6393d48c1ec9bbe4195699293789ec94c9e4c79acc2c9
Source0:        https://github.com/IBM/sarama/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects a non-constant TestReporter format string; retain the
# tests without that vet check. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/eapache/go-resiliency)
BuildRequires:  go(github.com/jcmturner/gofork)
BuildRequires:  go(github.com/jcmturner/gokrb5/v8)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/rcrowley/go-metrics)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/attribute)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutmetric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/trace)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(github.com/xdg-go/scram)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/eapache/go-resiliency)
Requires:       go(github.com/jcmturner/gofork)
Requires:       go(github.com/jcmturner/gokrb5/v8)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/pierrec/lz4/v4)
Requires:       go(github.com/rcrowley/go-metrics)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/attribute)
Requires:       go(go.opentelemetry.io/otel/exporters/stdout/stdoutmetric)
Requires:       go(go.opentelemetry.io/otel/sdk/trace)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(github.com/xdg-go/scram)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)

%description
Sarama is a pure Go client library for Apache Kafka.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
