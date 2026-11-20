# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           prometheus
%define go_import_path  github.com/prometheus/prometheus

Name:           prometheus
Version:        0.313.0
Release:        %autorelease
Summary:        Prometheus monitoring system
License:        Apache-2.0
URL:            https://github.com/prometheus/prometheus
#!RemoteAsset:  sha256:68dbe9e06f75c1ba48c8cbd4374f2dae2678e0c907083ea04a285dbfa09a6eea
Source0:        https://github.com/prometheus/prometheus/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Azure/azure-sdk-for-go)
BuildRequires:  go(github.com/Code-Hex/go-generics-cache)
BuildRequires:  go(github.com/KimMachineGun/automemlimit)
BuildRequires:  go(github.com/alecthomas/kingpin/v2)
BuildRequires:  go(github.com/alecthomas/units)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/smithy-go)
BuildRequires:  go(github.com/bboreham/go-loser)
BuildRequires:  go(github.com/cenkalti/backoff/v5)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/dennwc/varint)
BuildRequires:  go(github.com/digitalocean/godo)
BuildRequires:  go(github.com/edsrzf/mmap-go)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/envoy)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/facette/natsort)
BuildRequires:  go(github.com/felixge/fgprof)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-openapi/strfmt)
BuildRequires:  go(github.com/go-zookeeper/zk)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gophercloud/gophercloud/v2)
BuildRequires:  go(github.com/grafana/regexp)
BuildRequires:  go(github.com/hashicorp/consul/api)
BuildRequires:  go(github.com/hashicorp/nomad/api)
BuildRequires:  go(github.com/hetznercloud/hcloud-go/v2)
BuildRequires:  go(github.com/influxdata/influxdb-client-go/v2)
BuildRequires:  go(github.com/ionos-cloud/sdk-go/v6)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/kolo/xmlrpc)
BuildRequires:  go(github.com/linode/linodego)
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(github.com/moby/moby/api)
BuildRequires:  go(github.com/moby/moby/client)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/mwitkow/go-conntrack)
BuildRequires:  go(github.com/nsf/jsondiff)
BuildRequires:  go(github.com/oklog/run)
BuildRequires:  go(github.com/oklog/ulid/v2)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor)
BuildRequires:  go(github.com/outscale/osc-sdk-go/v2)
BuildRequires:  go(github.com/ovh/go-ovh)
BuildRequires:  go(github.com/pb33f/libopenapi)
BuildRequires:  go(github.com/pb33f/libopenapi-validator)
BuildRequires:  go(github.com/prometheus/alertmanager)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/exporter-toolkit)
BuildRequires:  go(github.com/prometheus/sigv4)
BuildRequires:  go(github.com/russross/blackfriday/v2)
BuildRequires:  go(github.com/scaleway/scaleway-sdk-go)
BuildRequires:  go(github.com/shurcooL/httpfs)
BuildRequires:  go(github.com/stackitcloud/stackit-sdk-go/core)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/vultr/govultr/v3)
BuildRequires:  go(go.opentelemetry.io/collector/component)
BuildRequires:  go(go.opentelemetry.io/collector/consumer)
BuildRequires:  go(go.opentelemetry.io/collector/pdata)
BuildRequires:  go(go.opentelemetry.io/collector/processor)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/automaxprocs)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/client-go)
BuildRequires:  go(k8s.io/klog)
BuildRequires:  go(k8s.io/klog/v2)

%description
Prometheus is a systems and service monitoring system. It collects metrics
from configured targets at regular intervals, evaluates rule expressions,
displays the results, and can trigger alerts when specified conditions are
observed.

%build
%go_common
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
%__go build %{go_build_flags_default} -o %{_builddir}/prometheus ./cmd/prometheus
%__go build %{go_build_flags_default} -o %{_builddir}/promtool ./cmd/promtool

%install
install -D -m 0755 %{_builddir}/prometheus %{buildroot}%{_bindir}/prometheus
install -D -m 0755 %{_builddir}/promtool %{buildroot}%{_bindir}/promtool

%check
%go_common
%__go test %{go_test_flags_default} ./cmd/prometheus ./cmd/promtool

%files
%doc README.md
%license LICENSE
%{_bindir}/prometheus
%{_bindir}/promtool

%changelog
%autochangelog
