# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           component-base
%define go_import_path  k8s.io/component-base

Name:           go-k8s-component-base
Version:        0.36.0
Release:        %autorelease
Summary:        Common functionality for Kubernetes core components
License:        Apache-2.0
URL:            https://github.com/kubernetes/component-base
#!RemoteAsset:  sha256:6b5fb4602554e3d5564815895428c514dab0df25c7f445780c7092e620b03971
Source0:        https://github.com/kubernetes/component-base/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/blang/semver/v4)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/zapr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/moby/term)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel/attribute)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
BuildRequires:  go(go.opentelemetry.io/otel/propagation)
BuildRequires:  go(go.opentelemetry.io/otel/semconv/v1.17.0)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.uber.org/zap/zapcore)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/client-go)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/utils/clock)
BuildRequires:  go(k8s.io/utils/ptr)
BuildRequires:  go(k8s.io/utils/trace)
BuildRequires:  go(sigs.k8s.io/json)

Provides:       go(k8s.io/component-base) = %{version}

Requires:       go(github.com/blang/semver/v4)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/zapr)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/moby/term)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel/attribute)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
Requires:       go(go.opentelemetry.io/otel/propagation)
Requires:       go(go.opentelemetry.io/otel/semconv/v1.17.0)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.uber.org/zap)
Requires:       go(go.uber.org/zap/zapcore)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(golang.org/x/text)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/client-go)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/utils/ptr)
Requires:       go(k8s.io/utils/trace)

%description
Component-base implements common functionality shared by Kubernetes core
components, including configuration, flag handling, HTTPS serving,
authentication, authorization, and logging.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
