# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kit
%define go_import_path  github.com/go-kit/kit
# These suites depend on external services, timing-sensitive metric sampling,
# or behavior removed by current etcd, gRPC, and HTTP dependencies.
%define go_test_exclude %{shrink:
    %{go_import_path}/metrics/cloudwatch
    %{go_import_path}/metrics/dogstatsd
    %{go_import_path}/metrics/prometheus
    %{go_import_path}/sd/etcdv3
    %{go_import_path}/tracing/opencensus
    %{go_import_path}/tracing/opentracing
    %{go_import_path}/tracing/zipkin
}

Name:           go-github-go-kit-kit
Version:        0.13.0
Release:        %autorelease
Summary:        Toolkit for building Go microservices
License:        MIT
URL:            https://github.com/go-kit/kit
#!RemoteAsset:  sha256:3d6850dd688d524a839300f374e7770c9f83459c90ee6073d194e1463c61ebde
Source0:        https://github.com/go-kit/kit/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects non-constant and mismatched test format strings.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/VividCortex/gohistogram)
BuildRequires:  go(github.com/afex/hystrix-go)
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/casbin/casbin/v2)
BuildRequires:  go(github.com/go-kit/log)
BuildRequires:  go(github.com/go-zookeeper/zk)
BuildRequires:  go(github.com/golang-jwt/jwt/v4)
BuildRequires:  go(github.com/hashicorp/consul/api)
BuildRequires:  go(github.com/hashicorp/golang-lru/v2)
BuildRequires:  go(github.com/hudl/fargo)
BuildRequires:  go(github.com/influxdata/influxdb1-client/v2)
BuildRequires:  go(github.com/nats-io/nats-server/v2)
BuildRequires:  go(github.com/nats-io/nats.go)
BuildRequires:  go(github.com/opentracing/opentracing-go)
BuildRequires:  go(github.com/openzipkin/zipkin-go)
BuildRequires:  go(github.com/performancecopilot/speed/v4)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/rabbitmq/amqp091-go)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/sony/gobreaker)
BuildRequires:  go(github.com/streadway/handy)
BuildRequires:  go(go.etcd.io/etcd/client/pkg/v3)
BuildRequires:  go(go.etcd.io/etcd/client/v2)
BuildRequires:  go(go.etcd.io/etcd/client/v3)
BuildRequires:  go(go.opencensus.io/plugin/ochttp)
BuildRequires:  go(go.opencensus.io/trace)
BuildRequires:  go(go.opencensus.io/trace/propagation)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.uber.org/zap/zapcore)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/metadata)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(google.golang.org/protobuf/reflect)
BuildRequires:  go(google.golang.org/protobuf/runtime)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/VividCortex/gohistogram)
Requires:       go(github.com/afex/hystrix-go)
Requires:       go(github.com/aws/aws-sdk-go)
Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/casbin/casbin/v2)
Requires:       go(github.com/go-kit/log)
Requires:       go(github.com/go-zookeeper/zk)
Requires:       go(github.com/golang-jwt/jwt/v4)
Requires:       go(github.com/hashicorp/consul/api)
Requires:       go(github.com/hashicorp/golang-lru/v2)
Requires:       go(github.com/hudl/fargo)
Requires:       go(github.com/influxdata/influxdb1-client/v2)
Requires:       go(github.com/nats-io/nats.go)
Requires:       go(github.com/opentracing/opentracing-go)
Requires:       go(github.com/openzipkin/zipkin-go)
Requires:       go(github.com/performancecopilot/speed/v4)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/rabbitmq/amqp091-go)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/sony/gobreaker)
Requires:       go(github.com/streadway/handy)
Requires:       go(go.etcd.io/etcd/client/pkg/v3)
Requires:       go(go.etcd.io/etcd/client/v2)
Requires:       go(go.etcd.io/etcd/client/v3)
Requires:       go(go.opencensus.io/plugin/ochttp)
Requires:       go(go.opencensus.io/trace)
Requires:       go(go.opencensus.io/trace/propagation)
Requires:       go(go.uber.org/zap)
Requires:       go(go.uber.org/zap/zapcore)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/codes)
Requires:       go(google.golang.org/grpc/metadata)
Requires:       go(google.golang.org/grpc/status)
Requires:       go(google.golang.org/protobuf/proto)

%description
Go kit is a collection of packages and design guidance for building robust,
maintainable microservices in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
