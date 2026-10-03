# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           server
%define go_import_path  go.etcd.io/etcd/server/v3

Name:           go-go.etcd-etcd-server-v3
Version:        3.6.8
Release:        %autorelease
Summary:        etcd v3 server Go module
License:        Apache-2.0
URL:            https://github.com/etcd-io/etcd
#!RemoteAsset:  sha256:8e6869dd5914220f2f530f1e962beafec138ee308e67fa6bc06e5769da6de1d9
Source0:        https://github.com/etcd-io/etcd/archive/server/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/coreos/go-semver)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/btree)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/jonboulle/clockwork)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/soheilhy/cmux)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tmc/grpc-websocket-proxy)
BuildRequires:  go(github.com/xiang90/probing)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(go.etcd.io/bbolt/errors)
BuildRequires:  go(go.etcd.io/etcd/api/v3)
BuildRequires:  go(go.etcd.io/etcd/client/v3)
BuildRequires:  go(go.etcd.io/etcd/pkg/v3)
BuildRequires:  go(go.etcd.io/raft/v3)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation)
BuildRequires:  go(go.opentelemetry.io/otel/exporters)
BuildRequires:  go(go.opentelemetry.io/otel/propagation)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/semconv/v1.17.0)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/genproto/googleapis)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf/encoding)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(google.golang.org/protobuf/reflect)
BuildRequires:  go(google.golang.org/protobuf/types)
BuildRequires:  go(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(go.etcd.io/etcd/server/v3) = %{version}

Requires:       go(github.com/coreos/go-semver)
Requires:       go(github.com/coreos/go-systemd/v22)
Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang-jwt/jwt/v5)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/btree)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/grpc-ecosystem/go-grpc-middleware)
Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(github.com/jonboulle/clockwork)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/soheilhy/cmux)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/tmc/grpc-websocket-proxy)
Requires:       go(github.com/xiang90/probing)
Requires:       go(go.etcd.io/bbolt)
Requires:       go(go.etcd.io/bbolt/errors)
Requires:       go(go.etcd.io/etcd/api/v3)
Requires:       go(go.etcd.io/etcd/client/v3)
Requires:       go(go.etcd.io/etcd/pkg/v3)
Requires:       go(go.etcd.io/raft/v3)
Requires:       go(go.opentelemetry.io/contrib/instrumentation)
Requires:       go(go.opentelemetry.io/otel/exporters)
Requires:       go(go.opentelemetry.io/otel/propagation)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/semconv/v1.17.0)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/genproto/googleapis)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf/encoding)
Requires:       go(google.golang.org/protobuf/proto)
Requires:       go(google.golang.org/protobuf/reflect)
Requires:       go(google.golang.org/protobuf/types)
Requires:       go(gopkg.in/natefinch/lumberjack.v2)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/yaml)

%description
This package provides the server-side Go module for etcd v3, including the
embedded server and server support packages used by Kubernetes.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
