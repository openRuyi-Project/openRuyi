# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zipkin-go
%define go_import_path  github.com/openzipkin/zipkin-go
# These tests require external DNS/HTTP access or the older Sarama test API.
%define go_test_exclude %{go_import_path} %{go_import_path}/middleware/http %{go_import_path}/reporter/kafka

Name:           go-github-openzipkin-zipkin-go
Version:        0.4.3
Release:        %autorelease
Summary:        Zipkin instrumentation library for Go
License:        Apache-2.0
URL:            https://github.com/openzipkin/zipkin-go
#!RemoteAsset:  sha256:27136dc752ba9a07a7cfae3939cb3349353c230c71fbd1875cbb2f8a208f28d4
Source0:        https://github.com/openzipkin/zipkin-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/IBM/sarama)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/rabbitmq/amqp091-go)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/metadata)
BuildRequires:  go(google.golang.org/grpc/peer)
BuildRequires:  go(google.golang.org/grpc/stats)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(google.golang.org/protobuf/reflect)
BuildRequires:  go(google.golang.org/protobuf/runtime)
BuildRequires:  go(google.golang.org/protobuf/types)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/IBM/sarama)
Requires:       go(github.com/rabbitmq/amqp091-go)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/codes)
Requires:       go(google.golang.org/grpc/metadata)
Requires:       go(google.golang.org/grpc/peer)
Requires:       go(google.golang.org/grpc/stats)
Requires:       go(google.golang.org/grpc/status)
Requires:       go(google.golang.org/protobuf/proto)
Requires:       go(google.golang.org/protobuf/reflect)
Requires:       go(google.golang.org/protobuf/runtime)
Requires:       go(google.golang.org/protobuf/types)

%description
Zipkin-go provides tracing instrumentation and reporters for Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
