# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sdk-go
%define go_import_path  github.com/cloudevents/sdk-go

Name:           go-github-cloudevents-sdk-go
Version:        2.16.2
Release:        %autorelease
Summary:        CloudEvents SDK and protocol bindings for Go
License:        Apache-2.0
URL:            https://github.com/cloudevents/sdk-go
#!RemoteAsset:  sha256:db57a01e6346c1ef9b97775db0b62768109a6ff7cf0417be559e692a07999ad9
Source0:        https://github.com/cloudevents/sdk-go/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
# Use system librdkafka for the Confluent binding, including on RISC-V.
BuildOption(check):  -tags=dynamic

BuildRequires:  gcc
BuildRequires:  pkgconfig(rdkafka)
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go)
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/iam)
BuildRequires:  go(cloud.google.com/go/pubsub)
BuildRequires:  go(cloud.google.com/go/pubsub/v2)
BuildRequires:  go(github.com/Azure/go-amqp)
BuildRequires:  go(github.com/IBM/sarama)
BuildRequires:  go(github.com/antlr/antlr4/runtime/Go/antlr)
BuildRequires:  go(github.com/bytedance/sonic)
BuildRequires:  go(github.com/bytedance/sonic/loader)
BuildRequires:  go(github.com/cloudwego/base64x)
BuildRequires:  go(github.com/confluentinc/confluent-kafka-go/v2)
BuildRequires:  go(github.com/cucumber/gherkin/go/v26)
BuildRequires:  go(github.com/cucumber/godog)
BuildRequires:  go(github.com/cucumber/messages/go/v21)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/eapache/go-resiliency)
BuildRequires:  go(github.com/eapache/go-xerial-snappy)
BuildRequires:  go(github.com/eapache/queue)
BuildRequires:  go(github.com/eclipse/paho.golang)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/gabriel-vasile/mimetype)
BuildRequires:  go(github.com/gin-contrib/sse)
BuildRequires:  go(github.com/gin-gonic/gin)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-playground/locales)
BuildRequires:  go(github.com/go-playground/universal-translator)
BuildRequires:  go(github.com/go-playground/validator/v10)
BuildRequires:  go(github.com/goccy/go-json)
BuildRequires:  go(github.com/gofrs/uuid)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/gorilla/mux)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix)
BuildRequires:  go(github.com/hashicorp/go-memdb)
BuildRequires:  go(github.com/hashicorp/go-msgpack)
BuildRequires:  go(github.com/hashicorp/go-msgpack/v2)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-uuid)
BuildRequires:  go(github.com/hashicorp/golang-lru)
BuildRequires:  go(github.com/hashicorp/raft)
BuildRequires:  go(github.com/jcmturner/aescts/v2)
BuildRequires:  go(github.com/jcmturner/dnsutils/v2)
BuildRequires:  go(github.com/jcmturner/gofork)
BuildRequires:  go(github.com/jcmturner/gokrb5/v8)
BuildRequires:  go(github.com/jcmturner/rpc/v2)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/kelseyhightower/envconfig)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/leodido/go-urn)
BuildRequires:  go(github.com/lightstep/tracecontext.go)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/minio/highwayhash)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/nats-io/jwt/v2)
BuildRequires:  go(github.com/nats-io/nats-server/v2)
BuildRequires:  go(github.com/nats-io/nats-streaming-server)
BuildRequires:  go(github.com/nats-io/nats.go)
BuildRequires:  go(github.com/nats-io/nkeys)
BuildRequires:  go(github.com/nats-io/nuid)
BuildRequires:  go(github.com/nats-io/stan.go)
BuildRequires:  go(github.com/niemeyer/pretty)
BuildRequires:  go(github.com/onsi/ginkgo)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/rcrowley/go-metrics)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/twitchyliquid64/golang-asm)
BuildRequires:  go(github.com/ugorji/go/codec)
BuildRequires:  go(github.com/valyala/bytebufferpool)
BuildRequires:  go(go.einride.tech/aip)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(golang.org/x/arch)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(nhooyr.io/websocket)
BuildRequires:  go(sigs.k8s.io/yaml)

# The repository root preserves the canonical paths of all nested modules.
Provides:       go(github.com/cloudevents/sdk-go) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/binding/format/protobuf/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/binding/format/protobuf/v2/pb) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/observability/opencensus/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/observability/opencensus/v2/client) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/observability/opencensus/v2/http) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/observability/opentelemetry/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/observability/opentelemetry/v2/client) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/observability/opentelemetry/v2/http) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/amqp/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/kafka_confluent/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/kafka_sarama/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/mqtt_paho/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/nats/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/nats_jetstream/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/nats_jetstream/v3) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/pubsub/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/pubsub/v2/context) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/pubsub/v2/internal) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/stan/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/protocol/ws/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/amqp) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/amqp/receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/amqp/sender) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/gochan) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/receiver-direct) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/receiver-gin) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/receiver-gorilla) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/receiver-protected) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/receiver-protobuf) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/receiver-result) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/receiver-sleepy) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/receiver-traced) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/requester) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/requester-with-custom-client) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/responder) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/sender) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/sender-protobuf) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/http/sender-retry) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/kafka) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/kafka/message-handle-non-cloudevents) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/kafka/receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/kafka/sender) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/kafka/sender-receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/kafka_confluent) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/kafka_confluent/receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/kafka_confluent/receiver-assign) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/kafka_confluent/sender) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/mqtt) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/mqtt/receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/mqtt/sender) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/nats) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/nats/message-interoperability) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/nats/receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/nats/sender) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/nats_jetstream) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/nats_jetstream/message-interoperability) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/nats_jetstream/receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/nats_jetstream/sender) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/nats_jetstream/v3) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/nats_jetstream/v3/receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/nats_jetstream/v3/sender) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/pubsub) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/pubsub/multireceiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/pubsub/multisender) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/pubsub/receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/pubsub/sender) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/stan) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/stan/receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/stan/sender) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/stan/sender-receiver) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/ws) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/samples/ws/client) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/sql/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/sql/v2/errors) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/sql/v2/expression) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/sql/v2/function) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/sql/v2/gen) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/sql/v2/parser) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/sql/v2/runtime) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/sql/v2/runtime/test) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/sql/v2/test) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/sql/v2/utils) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/benchmark) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/benchmark/buffering_vs_to_event) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/benchmark/e2e) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/benchmark/e2e/http) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/benchmark/http_request_to_kafka_sarama_encode) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/benchmark/kafka_sarama_to_http_request_encode) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/conformance) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/amqp) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/amqp_binding) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/http) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/http_binding) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/kafka_confluent) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/kafka_sarama) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/kafka_sarama_binding) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/mqtt_paho) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/mqtt_paho_binding) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/nats) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/nats_jetstream) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/nats_jetstream/v3) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/integration/stan) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/observability) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/observability/opentelemetry) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/test/sql) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/tools) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/tools/http/raw) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/binding) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/binding/buffering) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/binding/format) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/binding/spec) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/binding/test) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/binding/transformer) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/binding/utils) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/client) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/client/test) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/context) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/event) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/event/datacodec) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/event/datacodec/json) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/event/datacodec/text) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/event/datacodec/xml) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/extensions) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/observability) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/protocol) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/protocol/gochan) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/protocol/http) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/protocol/test) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/test) = %{version}
Provides:       go(github.com/cloudevents/sdk-go/v2/types) = %{version}

Requires:       go(cloud.google.com/go/pubsub/v2)
Requires:       go(github.com/Azure/go-amqp)
Requires:       go(github.com/IBM/sarama)
Requires:       go(github.com/antlr/antlr4/runtime/Go/antlr)
Requires:       go(github.com/confluentinc/confluent-kafka-go/v2)
Requires:       go(github.com/eclipse/paho.golang)
Requires:       go(github.com/gin-gonic/gin)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/gorilla/mux)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/kelseyhightower/envconfig)
Requires:       go(github.com/nats-io/nats.go)
Requires:       go(github.com/nats-io/stan.go)
Requires:       go(github.com/rs/zerolog)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/valyala/bytebufferpool)
Requires:       go(go.opencensus.io)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/sync)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(nhooyr.io/websocket)

%description
This package provides the complete CloudEvents Go SDK repository, including
protocol bindings, observability integrations, SQL support, samples, and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
