# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opentelemetry-collector-contrib
%define go_import_path  github.com/open-telemetry/opentelemetry-collector-contrib
# Schemagen path assertions require Go module mode rather than the offline GOPATH layout.
# Failover recovery tests use a fixed timeout that flakes on loaded OBS workers.
# AWS X-Ray telemetry assertions depend on the external request failure type.
%define go_test_exclude  %{go_import_path}/cmd/schemagen/internal %{go_import_path}/connector/failoverconnector %{go_import_path}/exporter/awsxrayexporter

Name:           go-github-open-telemetry-opentelemetry-collector-contrib
Version:        0.154.0
Release:        %autorelease
Summary:        OpenTelemetry Collector contrib modules
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector-contrib
#!RemoteAsset:  sha256:72c3365cf0f1a879a753e97cea902c2c09ce48ac5e28df5246cd048d7786edc1
Source0:        https://github.com/open-telemetry/opentelemetry-collector-contrib/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-cmd-telemetrygen-fix-canonical-import-comments.patch
# Keep the benchmark test connection compatible with packaged clickhouse-go.
Patch2001:      2001-exporter-clickhouse-support-clickhouse-go-v2.48-test.patch
# Avoid depending on resolver-specific gRPC error text in Coralogix tests.
Patch2002:      2002-exporter-coralogix-avoid-resolver-specific-error-mes.patch

BuildRequires:  go
BuildRequires:  go(4d63.com/gocheckcompilerdirectives)
BuildRequires:  go(4d63.com/gochecknoglobals)
BuildRequires:  go(bitbucket.org/atlassian/go-asap/v2)
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(cloud.google.com/go)
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/iam)
BuildRequires:  go(cloud.google.com/go/logging)
BuildRequires:  go(cloud.google.com/go/longrunning)
BuildRequires:  go(cloud.google.com/go/monitoring)
BuildRequires:  go(cloud.google.com/go/pubsub/v2)
BuildRequires:  go(cloud.google.com/go/secretmanager)
BuildRequires:  go(cloud.google.com/go/spanner)
BuildRequires:  go(cloud.google.com/go/storage)
BuildRequires:  go(cloud.google.com/go/trace)
BuildRequires:  go(code.cloudfoundry.org/clock)
BuildRequires:  go(code.cloudfoundry.org/garden)
BuildRequires:  go(code.cloudfoundry.org/go-diodes)
BuildRequires:  go(code.cloudfoundry.org/go-loggregator)
BuildRequires:  go(code.cloudfoundry.org/lager/v3)
BuildRequires:  go(code.cloudfoundry.org/rfc5424)
BuildRequires:  go(codeberg.org/chavacava/garif)
BuildRequires:  go(dario.cat/mergo)
BuildRequires:  go(dev.gaijin.team/go/exhaustruct/v4)
BuildRequires:  go(dev.gaijin.team/go/golib)
BuildRequires:  go(filippo.io/edwards25519)
BuildRequires:  go(github.com/4meepo/tagalign)
BuildRequires:  go(github.com/99designs/go-keychain)
BuildRequires:  go(github.com/99designs/keyring)
BuildRequires:  go(github.com/Abirdcfly/dupword)
BuildRequires:  go(github.com/AdminBenni/iota-mixing)
BuildRequires:  go(github.com/AlwxSin/noinlineerr)
BuildRequires:  go(github.com/Antonboom/errname)
BuildRequires:  go(github.com/Antonboom/nilnil)
BuildRequires:  go(github.com/Antonboom/testifylint)
BuildRequires:  go(github.com/Arize-ai/openinference/go/openinference-semantic-conventions)
BuildRequires:  go(github.com/AthenZ/athenz)
BuildRequires:  go(github.com/Azure/azure-kusto-go)
BuildRequires:  go(github.com/Azure/azure-kusto-go/azkustodata)
BuildRequires:  go(github.com/Azure/azure-kusto-go/azkustoingest)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/data/aztables)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/internal)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/messaging/azeventhubs/v2)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/monitor/query/azmetrics)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/compute/armcompute/v5)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/monitor/armmonitor)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/network/armnetwork/v4)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resources/armresources/v3)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resources/armsubscriptions)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/storage/azqueue)
BuildRequires:  go(github.com/Azure/go-amqp)
BuildRequires:  go(github.com/Azure/go-ansiterm)
BuildRequires:  go(github.com/Azure/go-ntlmssp)
BuildRequires:  go(github.com/AzureAD/microsoft-authentication-library-for-go)
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/ClickHouse/ch-go)
BuildRequires:  go(github.com/ClickHouse/clickhouse-go/v2)
BuildRequires:  go(github.com/Code-Hex/go-generics-cache)
BuildRequires:  go(github.com/DATA-DOG/go-sqlmock)
BuildRequires:  go(github.com/DataDog/agent-payload/v5)
BuildRequires:  go(github.com/DataDog/datadog-agent)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/config)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/flare/builder)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/flare/types)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/hostname/hostnameinterface)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/log/def)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/secrets/def)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/secrets/noop-impl)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/status)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/tagger/def)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/tagger/origindetection)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/tagger/types)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/tagger/utils)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/core/telemetry)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/def)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/forwarder/defaultforwarder)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/forwarder/orchestrator/orchestratorinterface)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/logs/agent/config)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline/logsagentpipelineimpl)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/logsagentexporter)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/serializerexporter)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/metricsclient)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/testutil)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/serializer/logscompression)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/serializer/metricscompression)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/trace/compression/def)
BuildRequires:  go(github.com/DataDog/datadog-agent/comp/trace/compression/impl-gzip)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/aggregator/ckey)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/api)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/collector/check/defaults)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/basic)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/create)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/env)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/helper)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/mock)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/model)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/nodetreemodel)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/setup)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/structure)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/teeconfig)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/utils)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/config/viperconfig)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/fips)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/logs/client)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/logs/diagnostic)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/logs/message)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/logs/metrics)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/logs/pipeline)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/logs/processor)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/logs/sender)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/logs/sources)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/logs/status/statusinterface)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/logs/status/utils)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/logs/types)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/metrics)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/obfuscate)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/inframetadata)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/attributes)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/logs)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/metrics)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/rum)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/orchestrator/model)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/orchestrator/util)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/process/util/api)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/proto)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/remoteconfig/state)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/serializer)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/status/health)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/tagger/types)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/tagset)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/telemetry)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/template)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/trace)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/trace/exportable)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/trace/log)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/trace/otel)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/trace/stats)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/trace/traceutil)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/backoff)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/buf)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/cgroups)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/common)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/compression)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/executable)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/filesystem)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/fxutil)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/hostname/validate)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/http)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/json)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/log)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/log/setup)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/option)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/otel)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/pointer)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/quantile)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/scrubber)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/sort)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/startstop)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/statstracker)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/system)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/util/winutil)
BuildRequires:  go(github.com/DataDog/datadog-agent/pkg/version)
BuildRequires:  go(github.com/DataDog/datadog-api-client-go/v2)
BuildRequires:  go(github.com/DataDog/datadog-go/v5)
BuildRequires:  go(github.com/DataDog/go-sqllexer)
BuildRequires:  go(github.com/DataDog/go-tuf)
BuildRequires:  go(github.com/DataDog/gohai)
BuildRequires:  go(github.com/DataDog/mmh3)
BuildRequires:  go(github.com/DataDog/sketches-go)
BuildRequires:  go(github.com/DataDog/viper)
BuildRequires:  go(github.com/DataDog/zstd)
BuildRequires:  go(github.com/DataDog/zstd_0)
BuildRequires:  go(github.com/DeRuina/timberjack)
BuildRequires:  go(github.com/Djarvur/go-err113)
BuildRequires:  go(github.com/GehirnInc/crypt)
BuildRequires:  go(github.com/GoogleCloudPlatform/grpc-gcp-go/grpcgcp)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/googlemanagedprometheus)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/extension/googleclientauthextension)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping)
BuildRequires:  go(github.com/HdrHistogram/hdrhistogram-go)
BuildRequires:  go(github.com/Khan/genqlient)
BuildRequires:  go(github.com/KimMachineGun/automemlimit)
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/MirrexOne/unqueryvet)
BuildRequires:  go(github.com/OpenPeeDeeP/depguard/v2)
BuildRequires:  go(github.com/ProtonMail/go-crypto)
BuildRequires:  go(github.com/RaduBerinde/axisds)
BuildRequires:  go(github.com/RaduBerinde/btreemap)
BuildRequires:  go(github.com/RoaringBitmap/roaring/v2)
BuildRequires:  go(github.com/SAP/go-hdb)
BuildRequires:  go(github.com/SermoDigital/jose)
BuildRequires:  go(github.com/Showmax/go-fqdn)
BuildRequires:  go(github.com/aerospike/aerospike-client-go/v8)
BuildRequires:  go(github.com/agnivade/levenshtein)
BuildRequires:  go(github.com/alecthomas/chroma/v2)
BuildRequires:  go(github.com/alecthomas/go-check-sumtype)
BuildRequires:  go(github.com/alecthomas/participle/v2)
BuildRequires:  go(github.com/alecthomas/units)
BuildRequires:  go(github.com/alexbrainman/sspi)
BuildRequires:  go(github.com/alexflint/go-arg)
BuildRequires:  go(github.com/alexflint/go-scalar)
BuildRequires:  go(github.com/alexkohler/nakedret/v2)
BuildRequires:  go(github.com/alexkohler/prealloc)
BuildRequires:  go(github.com/alfatraining/structtag)
BuildRequires:  go(github.com/alingse/asasalint)
BuildRequires:  go(github.com/alingse/nilnesserr)
BuildRequires:  go(github.com/aliyun/aliyun-log-go-sdk)
BuildRequires:  go(github.com/andybalholm/brotli)
BuildRequires:  go(github.com/antchfx/xmlquery)
BuildRequires:  go(github.com/antchfx/xpath)
BuildRequires:  go(github.com/apache/arrow-go/v18)
BuildRequires:  go(github.com/apache/cassandra-gocql-driver/v2)
BuildRequires:  go(github.com/apache/pulsar-client-go)
BuildRequires:  go(github.com/apache/thrift)
BuildRequires:  go(github.com/apapsch/go-jsonmerge/v2)
BuildRequires:  go(github.com/ardielle/ardielle-go)
BuildRequires:  go(github.com/armon/go-metrics)
BuildRequires:  go(github.com/ashanbrown/forbidigo/v2)
BuildRequires:  go(github.com/ashanbrown/makezero/v2)
BuildRequires:  go(github.com/aws/aws-lambda-go)
BuildRequires:  go(github.com/aws/aws-msk-iam-sasl-signer-go)
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/config)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/credentials)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/feature/s3/manager)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/feature/s3/transfermanager)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/configsources)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/ini)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/v4a)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/cloudwatch)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ec2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ecs)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/elasticache)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/checksum)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/s3shared)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/kafka)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/kinesis)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/lightsail)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/rds)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/s3)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/secretsmanager)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/servicediscovery)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/signin)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sqs)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sso)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sts)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/xray)
BuildRequires:  go(github.com/aws/smithy-go)
BuildRequires:  go(github.com/axiomhq/hyperloglog)
BuildRequires:  go(github.com/aymanbagabas/go-osc52/v2)
BuildRequires:  go(github.com/bahlo/generic-list-go)
BuildRequires:  go(github.com/basgys/goxml2json)
BuildRequires:  go(github.com/bboreham/go-loser)
BuildRequires:  go(github.com/beevik/ntp)
BuildRequires:  go(github.com/benbjohnson/clock)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/bitfield/gotestdox)
BuildRequires:  go(github.com/bitly/go-simplejson)
BuildRequires:  go(github.com/bits-and-blooms/bitset)
BuildRequires:  go(github.com/bkielbasa/cyclop)
BuildRequires:  go(github.com/blang/semver/v4)
BuildRequires:  go(github.com/blizzy78/varnamelen)
BuildRequires:  go(github.com/bmatcuk/doublestar/v4)
BuildRequires:  go(github.com/bmizerany/pat)
BuildRequires:  go(github.com/bombsimon/wsl/v4)
BuildRequires:  go(github.com/bombsimon/wsl/v5)
BuildRequires:  go(github.com/breml/bidichk)
BuildRequires:  go(github.com/breml/errchkjson)
BuildRequires:  go(github.com/brianvoe/gofakeit/v6)
BuildRequires:  go(github.com/buger/jsonparser)
BuildRequires:  go(github.com/butuzov/ireturn)
BuildRequires:  go(github.com/butuzov/mirror)
BuildRequires:  go(github.com/catenacyber/perfsprint)
BuildRequires:  go(github.com/ccojocar/zxcvbn-go)
BuildRequires:  go(github.com/cenkalti/backoff)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cenkalti/backoff/v5)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/charithe/durationcheck)
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/charmbracelet/x/ansi)
BuildRequires:  go(github.com/charmbracelet/x/cellbuf)
BuildRequires:  go(github.com/charmbracelet/x/term)
BuildRequires:  go(github.com/cihub/seelog)
BuildRequires:  go(github.com/cilium/ebpf)
BuildRequires:  go(github.com/ckaznocha/intrange)
BuildRequires:  go(github.com/client9/misspell)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/cloudflare/circl)
BuildRequires:  go(github.com/cloudfoundry-incubator/uaago)
BuildRequires:  go(github.com/cloudfoundry/go-cfclient/v3)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/cockroachdb/crlib)
BuildRequires:  go(github.com/cockroachdb/errors)
BuildRequires:  go(github.com/cockroachdb/logtags)
BuildRequires:  go(github.com/cockroachdb/pebble/v2)
BuildRequires:  go(github.com/cockroachdb/redact)
BuildRequires:  go(github.com/cockroachdb/swiss)
BuildRequires:  go(github.com/cockroachdb/tokenbucket)
BuildRequires:  go(github.com/codegangsta/inject)
BuildRequires:  go(github.com/containerd/cgroups/v3)
BuildRequires:  go(github.com/containerd/containerd/api)
BuildRequires:  go(github.com/containerd/errdefs)
BuildRequires:  go(github.com/containerd/errdefs/pkg)
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/containerd/platforms)
BuildRequires:  go(github.com/containerd/ttrpc)
BuildRequires:  go(github.com/containerd/typeurl/v2)
BuildRequires:  go(github.com/coreos/go-oidc/v3)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/cpuguy83/dockercfg)
BuildRequires:  go(github.com/curioswitch/go-reassign)
BuildRequires:  go(github.com/cyphar/filepath-securejoin)
BuildRequires:  go(github.com/daixiang0/gci)
BuildRequires:  go(github.com/danieljoos/wincred)
BuildRequires:  go(github.com/dave/dst)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/denis-tingaikin/go-header)
BuildRequires:  go(github.com/dennwc/varint)
BuildRequires:  go(github.com/dgryski/go-metro)
BuildRequires:  go(github.com/digitalocean/go-metadata)
BuildRequires:  go(github.com/digitalocean/godo)
BuildRequires:  go(github.com/distribution/reference)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/dnephin/pflag)
BuildRequires:  go(github.com/docker/go-connections)
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/dvsekhvalnov/jose2go)
BuildRequires:  go(github.com/ebitengine/purego)
BuildRequires:  go(github.com/edsrzf/mmap-go)
BuildRequires:  go(github.com/elastic/elastic-transport-go/v8)
BuildRequires:  go(github.com/elastic/go-docappender/v2)
BuildRequires:  go(github.com/elastic/go-freelru)
BuildRequires:  go(github.com/elastic/go-grok)
BuildRequires:  go(github.com/elastic/go-structform)
BuildRequires:  go(github.com/elastic/lunes)
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/emirpasic/gods)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/envoy)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/ettle/strcase)
BuildRequires:  go(github.com/euank/go-kmsg-parser)
BuildRequires:  go(github.com/evanphx/json-patch/v5)
BuildRequires:  go(github.com/expr-lang/expr)
BuildRequires:  go(github.com/facebook/time)
BuildRequires:  go(github.com/facette/natsort)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/fatih/structtag)
BuildRequires:  go(github.com/felixge/fgprof)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/firefart/nonamedreturns)
BuildRequires:  go(github.com/fluent/fluent-logger-golang)
BuildRequires:  go(github.com/fortytw2/leaktest)
BuildRequires:  go(github.com/foxboron/go-tpm-keyfiles)
BuildRequires:  go(github.com/frankban/quicktest)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/fzipp/gocyclo)
BuildRequires:  go(github.com/gabriel-vasile/mimetype)
BuildRequires:  go(github.com/getsentry/sentry-go)
BuildRequires:  go(github.com/ghostiam/protogetter)
BuildRequires:  go(github.com/go-asn1-ber/asn1-ber)
BuildRequires:  go(github.com/go-critic/go-critic)
BuildRequires:  go(github.com/go-faster/city)
BuildRequires:  go(github.com/go-faster/errors)
BuildRequires:  go(github.com/go-git/gcfg)
BuildRequires:  go(github.com/go-git/go-billy/v5)
BuildRequires:  go(github.com/go-git/go-git/v5)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-json-experiment/json)
BuildRequires:  go(github.com/go-kit/kit)
BuildRequires:  go(github.com/go-kit/log)
BuildRequires:  go(github.com/go-ldap/ldap/v3)
BuildRequires:  go(github.com/go-logfmt/logfmt)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-martini/martini)
BuildRequires:  go(github.com/go-ole/go-ole)
BuildRequires:  go(github.com/go-openapi/analysis)
BuildRequires:  go(github.com/go-openapi/errors)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/go-openapi/loads)
BuildRequires:  go(github.com/go-openapi/spec)
BuildRequires:  go(github.com/go-openapi/strfmt)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/swag/cmdutils)
BuildRequires:  go(github.com/go-openapi/swag/conv)
BuildRequires:  go(github.com/go-openapi/swag/fileutils)
BuildRequires:  go(github.com/go-openapi/swag/jsonname)
BuildRequires:  go(github.com/go-openapi/swag/jsonutils)
BuildRequires:  go(github.com/go-openapi/swag/loading)
BuildRequires:  go(github.com/go-openapi/swag/mangling)
BuildRequires:  go(github.com/go-openapi/swag/netutils)
BuildRequires:  go(github.com/go-openapi/swag/stringutils)
BuildRequires:  go(github.com/go-openapi/swag/typeutils)
BuildRequires:  go(github.com/go-openapi/swag/yamlutils)
BuildRequires:  go(github.com/go-openapi/validate)
BuildRequires:  go(github.com/go-redis/redismock/v9)
BuildRequires:  go(github.com/go-resty/resty/v2)
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
BuildRequires:  go(github.com/go-toolsmith/astcast)
BuildRequires:  go(github.com/go-toolsmith/astcopy)
BuildRequires:  go(github.com/go-toolsmith/astequal)
BuildRequires:  go(github.com/go-toolsmith/astfmt)
BuildRequires:  go(github.com/go-toolsmith/astp)
BuildRequires:  go(github.com/go-toolsmith/strparse)
BuildRequires:  go(github.com/go-toolsmith/typep)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/go-xmlfmt/xmlfmt)
BuildRequires:  go(github.com/go-zookeeper/zk)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/goccy/go-json)
BuildRequires:  go(github.com/goccy/go-yaml)
BuildRequires:  go(github.com/godbus/dbus)
BuildRequires:  go(github.com/godbus/dbus/v5)
BuildRequires:  go(github.com/godoc-lint/godoc-lint)
BuildRequires:  go(github.com/gofrs/flock)
BuildRequires:  go(github.com/gofrs/uuid)
BuildRequires:  go(github.com/gogo/googleapis)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/golang-sql/civil)
BuildRequires:  go(github.com/golang-sql/sqlexp)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/mock)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/golangci/asciicheck)
BuildRequires:  go(github.com/golangci/dupl)
BuildRequires:  go(github.com/golangci/go-printf-func-name)
BuildRequires:  go(github.com/golangci/gofmt)
BuildRequires:  go(github.com/golangci/golangci-lint/v2)
BuildRequires:  go(github.com/golangci/golines)
BuildRequires:  go(github.com/golangci/misspell)
BuildRequires:  go(github.com/golangci/plugin-module-register)
BuildRequires:  go(github.com/golangci/revgrep)
BuildRequires:  go(github.com/golangci/swaggoswag)
BuildRequires:  go(github.com/golangci/unconvert)
BuildRequires:  go(github.com/google/addlicense)
BuildRequires:  go(github.com/google/cadvisor)
BuildRequires:  go(github.com/google/flatbuffers)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-github/v84)
BuildRequires:  go(github.com/google/go-github/v88)
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/google/go-tpm)
BuildRequires:  go(github.com/google/jsonschema-go)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/shlex)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/gophercloud/gophercloud/v2)
BuildRequires:  go(github.com/gordonklaus/ineffassign)
BuildRequires:  go(github.com/gorilla/mux)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/gosnmp/gosnmp)
BuildRequires:  go(github.com/gostaticanalysis/analysisutil)
BuildRequires:  go(github.com/gostaticanalysis/comment)
BuildRequires:  go(github.com/gostaticanalysis/forcetypeassert)
BuildRequires:  go(github.com/gostaticanalysis/nilerr)
BuildRequires:  go(github.com/grafana/clusterurl)
BuildRequires:  go(github.com/grafana/faro/pkg/go)
BuildRequires:  go(github.com/grafana/loki/pkg/push)
BuildRequires:  go(github.com/grafana/regexp)
BuildRequires:  go(github.com/grobie/gomemcache)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/gsterjov/go-libsecret)
BuildRequires:  go(github.com/hamba/avro/v2)
BuildRequires:  go(github.com/hashicorp/consul/api)
BuildRequires:  go(github.com/hashicorp/cronexpr)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix/v2)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)
BuildRequires:  go(github.com/hashicorp/go-rootcerts)
BuildRequires:  go(github.com/hashicorp/go-uuid)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/hashicorp/golang-lru)
BuildRequires:  go(github.com/hashicorp/golang-lru/v2)
BuildRequires:  go(github.com/hashicorp/nomad/api)
BuildRequires:  go(github.com/hashicorp/serf)
BuildRequires:  go(github.com/hectane/go-acl)
BuildRequires:  go(github.com/hetznercloud/hcloud-go/v2)
BuildRequires:  go(github.com/hexops/gotextdiff)
BuildRequires:  go(github.com/huandu/go-clone)
BuildRequires:  go(github.com/huaweicloud/huaweicloud-sdk-go-v3)
BuildRequires:  go(github.com/iancoleman/strcase)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/influxdata/influxdb-client-go/v2)
BuildRequires:  go(github.com/influxdata/influxdb-observability/common)
BuildRequires:  go(github.com/influxdata/influxdb-observability/influx2otel)
BuildRequires:  go(github.com/influxdata/influxdb-observability/otel2influx)
BuildRequires:  go(github.com/influxdata/influxdb1-client)
BuildRequires:  go(github.com/influxdata/line-protocol)
BuildRequires:  go(github.com/influxdata/line-protocol/v2)
BuildRequires:  go(github.com/ionos-cloud/sdk-go/v6)
BuildRequires:  go(github.com/itchyny/go-yaml)
BuildRequires:  go(github.com/itchyny/gojq)
BuildRequires:  go(github.com/itchyny/timefmt-go)
BuildRequires:  go(github.com/jackc/pgpassfile)
BuildRequires:  go(github.com/jackc/pgservicefile)
BuildRequires:  go(github.com/jackc/pgx/v5)
BuildRequires:  go(github.com/jackc/puddle/v2)
BuildRequires:  go(github.com/jaegertracing/jaeger-idl)
BuildRequires:  go(github.com/jaeyo/go-drain3)
BuildRequires:  go(github.com/jbenet/go-context)
BuildRequires:  go(github.com/jcchavezs/porto)
BuildRequires:  go(github.com/jcmturner/aescts/v2)
BuildRequires:  go(github.com/jcmturner/dnsutils/v2)
BuildRequires:  go(github.com/jcmturner/gofork)
BuildRequires:  go(github.com/jcmturner/goidentity/v6)
BuildRequires:  go(github.com/jcmturner/gokrb5/v8)
BuildRequires:  go(github.com/jcmturner/rpc/v2)
BuildRequires:  go(github.com/jellydator/ttlcache/v3)
BuildRequires:  go(github.com/jgautheron/goconst)
BuildRequires:  go(github.com/jingyugao/rowserrcheck)
BuildRequires:  go(github.com/jjti/go-spancheck)
BuildRequires:  go(github.com/jmespath/go-jmespath)
BuildRequires:  go(github.com/jonboulle/clockwork)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/joshdk/go-junit)
BuildRequires:  go(github.com/jpillora/backoff)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/jstemmer/go-junit-report/v2)
BuildRequires:  go(github.com/julienschmidt/httprouter)
BuildRequires:  go(github.com/julz/importas)
BuildRequires:  go(github.com/kamstrup/intmap)
BuildRequires:  go(github.com/kaptinlin/go-i18n)
BuildRequires:  go(github.com/kaptinlin/jsonpointer)
BuildRequires:  go(github.com/kaptinlin/jsonschema)
BuildRequires:  go(github.com/kaptinlin/messageformat-go)
BuildRequires:  go(github.com/karamaru-alpha/copyloopvar)
BuildRequires:  go(github.com/kevinburke/ssh_config)
BuildRequires:  go(github.com/kisielk/errcheck)
BuildRequires:  go(github.com/kkHAIKE/contextcheck)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/knadh/koanf/parsers/yaml)
BuildRequires:  go(github.com/knadh/koanf/providers/confmap)
BuildRequires:  go(github.com/knadh/koanf/providers/env/v2)
BuildRequires:  go(github.com/knadh/koanf/providers/file)
BuildRequires:  go(github.com/knadh/koanf/providers/fs)
BuildRequires:  go(github.com/knadh/koanf/providers/rawbytes)
BuildRequires:  go(github.com/knadh/koanf/v2)
BuildRequires:  go(github.com/kolo/xmlrpc)
BuildRequires:  go(github.com/kr/fs)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/kulti/thelper)
BuildRequires:  go(github.com/kunwardeep/paralleltest)
BuildRequires:  go(github.com/kylelemons/godebug)
BuildRequires:  go(github.com/lasiar/canonicalheader)
BuildRequires:  go(github.com/ldez/exptostd)
BuildRequires:  go(github.com/ldez/gomoddirectives)
BuildRequires:  go(github.com/ldez/grignotin)
BuildRequires:  go(github.com/ldez/tagliatelle)
BuildRequires:  go(github.com/ldez/usetesting)
BuildRequires:  go(github.com/leodido/go-syslog/v4)
BuildRequires:  go(github.com/leodido/ragel-machinery)
BuildRequires:  go(github.com/leonklingele/grouper)
BuildRequires:  go(github.com/lestrrat-go/strftime)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/libp2p/go-reuseport)
BuildRequires:  go(github.com/lightstep/go-expohisto)
BuildRequires:  go(github.com/linkedin/goavro/v2)
BuildRequires:  go(github.com/linode/go-metadata)
BuildRequires:  go(github.com/linode/linodego)
BuildRequires:  go(github.com/logicmonitor/lm-data-sdk-go)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/lufia/plan9stats)
BuildRequires:  go(github.com/macabu/inamedparam)
BuildRequires:  go(github.com/magefile/mage)
BuildRequires:  go(github.com/magiconair/properties)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/manuelarte/embeddedstructfieldcheck)
BuildRequires:  go(github.com/manuelarte/funcorder)
BuildRequires:  go(github.com/maratori/testableexamples)
BuildRequires:  go(github.com/maratori/testpackage)
BuildRequires:  go(github.com/martini-contrib/render)
BuildRequires:  go(github.com/matoous/godox)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/mattn/go-shellwords)
BuildRequires:  go(github.com/maxmind/MaxMind-DB)
BuildRequires:  go(github.com/maxmind/mmdbwriter)
BuildRequires:  go(github.com/mdlayher/socket)
BuildRequires:  go(github.com/mdlayher/vsock)
BuildRequires:  go(github.com/mgechev/revive)
BuildRequires:  go(github.com/michel-laterman/proxy-connect-dialer-go)
BuildRequires:  go(github.com/microsoft/ApplicationInsights-Go)
BuildRequires:  go(github.com/microsoft/go-mssqldb)
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(github.com/minio/minlz)
BuildRequires:  go(github.com/minio/sha256-simd)
BuildRequires:  go(github.com/mistifyio/go-zfs)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/hashstructure/v2)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/moby/docker-image-spec)
BuildRequires:  go(github.com/moby/go-archive)
BuildRequires:  go(github.com/moby/moby/api)
BuildRequires:  go(github.com/moby/moby/client)
BuildRequires:  go(github.com/moby/patternmatcher)
BuildRequires:  go(github.com/moby/sys/mountinfo)
BuildRequires:  go(github.com/moby/sys/sequential)
BuildRequires:  go(github.com/moby/sys/user)
BuildRequires:  go(github.com/moby/sys/userns)
BuildRequires:  go(github.com/moby/term)
BuildRequires:  go(github.com/modelcontextprotocol/go-sdk)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/mohae/deepcopy)
BuildRequires:  go(github.com/mongodb-forks/digest)
BuildRequires:  go(github.com/moricho/tparallel)
BuildRequires:  go(github.com/mschoch/smat)
BuildRequires:  go(github.com/mtibben/percent)
BuildRequires:  go(github.com/muesli/termenv)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/mwitkow/go-conntrack)
BuildRequires:  go(github.com/nakabonne/nestif)
BuildRequires:  go(github.com/ncruces/go-strftime)
BuildRequires:  go(github.com/netsampler/goflow2/v2)
BuildRequires:  go(github.com/nginx/nginx-prometheus-exporter)
BuildRequires:  go(github.com/nishanths/exhaustive)
BuildRequires:  go(github.com/nishanths/predeclared)
BuildRequires:  go(github.com/nunnatsa/ginkgolinter)
BuildRequires:  go(github.com/nxadm/tail)
BuildRequires:  go(github.com/oapi-codegen/runtime)
BuildRequires:  go(github.com/oklog/ulid/v2)
BuildRequires:  go(github.com/onsi/ginkgo)
BuildRequires:  go(github.com/onsi/ginkgo/v2)
BuildRequires:  go(github.com/open-telemetry/opamp-go)
BuildRequires:  go(github.com/open-telemetry/otel-arrow/go)
BuildRequires:  go(github.com/opencontainers/cgroups)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/opencontainers/runtime-spec)
BuildRequires:  go(github.com/opensearch-project/opensearch-go/v4)
BuildRequires:  go(github.com/openshift/api)
BuildRequires:  go(github.com/openshift/client-go)
BuildRequires:  go(github.com/openzipkin/zipkin-go)
BuildRequires:  go(github.com/orcaman/concurrent-map/v2)
BuildRequires:  go(github.com/oschwald/geoip2-golang/v2)
BuildRequires:  go(github.com/oschwald/maxminddb-golang)
BuildRequires:  go(github.com/oschwald/maxminddb-golang/v2)
BuildRequires:  go(github.com/osquery/osquery-go)
BuildRequires:  go(github.com/outcaste-io/ristretto)
BuildRequires:  go(github.com/outscale/osc-sdk-go/v2)
BuildRequires:  go(github.com/ovh/go-ovh)
BuildRequires:  go(github.com/oxtoacart/bpool)
BuildRequires:  go(github.com/parquet-go/bitpack)
BuildRequires:  go(github.com/parquet-go/jsonlite)
BuildRequires:  go(github.com/parquet-go/parquet-go)
BuildRequires:  go(github.com/patrickmn/go-cache)
BuildRequires:  go(github.com/paulmach/orb)
BuildRequires:  go(github.com/pavlo-v-chernykh/keystore-go/v4)
BuildRequires:  go(github.com/pavolloffay/opentelemetry-mcp-server/modules/collectorschema)
BuildRequires:  go(github.com/pb33f/jsonpath)
BuildRequires:  go(github.com/pb33f/libopenapi)
BuildRequires:  go(github.com/pb33f/ordered-map/v2)
BuildRequires:  go(github.com/pbnjay/memory)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/philhofer/fwd)
BuildRequires:  go(github.com/philippgille/chromem-go)
BuildRequires:  go(github.com/pierrec/lz4)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pjbgf/sha1cd)
BuildRequires:  go(github.com/pkg/browser)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pkg/sftp)
BuildRequires:  go(github.com/planetscale/vtprotobuf)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/polyfloyd/go-errorlint)
BuildRequires:  go(github.com/power-devops/perfstat)
BuildRequires:  go(github.com/pquerna/cachecontrol)
BuildRequires:  go(github.com/prometheus-community/pro-bing)
BuildRequires:  go(github.com/prometheus/alertmanager)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_golang/exp)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/common/assets)
BuildRequires:  go(github.com/prometheus/exporter-toolkit)
BuildRequires:  go(github.com/prometheus/otlptranslator)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/prometheus/prometheus)
BuildRequires:  go(github.com/prometheus/sigv4)
BuildRequires:  go(github.com/puzpuzpuz/xsync)
BuildRequires:  go(github.com/puzpuzpuz/xsync/v4)
BuildRequires:  go(github.com/quasilyte/go-ruleguard)
BuildRequires:  go(github.com/quasilyte/go-ruleguard/dsl)
BuildRequires:  go(github.com/quasilyte/gogrep)
BuildRequires:  go(github.com/quasilyte/regex/syntax)
BuildRequires:  go(github.com/quasilyte/stdinfo)
BuildRequires:  go(github.com/rabbitmq/amqp091-go)
BuildRequires:  go(github.com/raeperd/recvcheck)
BuildRequires:  go(github.com/rdforte/gomaxecs)
BuildRequires:  go(github.com/redis/go-redis/v9)
BuildRequires:  go(github.com/relvacode/iso8601)
BuildRequires:  go(github.com/remyoudompheng/bigfft)
BuildRequires:  go(github.com/rhysd/actionlint)
BuildRequires:  go(github.com/richardartoul/molecule)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/robfig/cron/v3)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/rs/cors)
BuildRequires:  go(github.com/ryancurrah/gomodguard)
BuildRequires:  go(github.com/ryanrolds/sqlclosecheck)
BuildRequires:  go(github.com/sagikazarmark/locafero)
BuildRequires:  go(github.com/samber/lo)
BuildRequires:  go(github.com/sanposhiho/wastedassign/v2)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(github.com/sashamelentyev/interfacebloat)
BuildRequires:  go(github.com/sashamelentyev/usestdlibvars)
BuildRequires:  go(github.com/scaleway/scaleway-sdk-go)
BuildRequires:  go(github.com/scalyr/dataset-go)
BuildRequires:  go(github.com/secure-systems-lab/go-securesystemslib)
BuildRequires:  go(github.com/securego/gosec/v2)
BuildRequires:  go(github.com/segmentio/asm)
BuildRequires:  go(github.com/segmentio/encoding)
BuildRequires:  go(github.com/sergi/go-diff)
BuildRequires:  go(github.com/shirou/gopsutil/v3)
BuildRequires:  go(github.com/shirou/gopsutil/v4)
BuildRequires:  go(github.com/shoenig/go-m1cpu)
BuildRequires:  go(github.com/shoenig/test)
BuildRequires:  go(github.com/shopspring/decimal)
BuildRequires:  go(github.com/shurcooL/httpfs)
BuildRequires:  go(github.com/signalfx/com_signalfx_metrics_protobuf)
BuildRequires:  go(github.com/sijms/go-ora/v2)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/sivchari/containedctx)
BuildRequires:  go(github.com/skeema/knownhosts)
BuildRequires:  go(github.com/snowflakedb/gosnowflake/v2)
BuildRequires:  go(github.com/sonatard/noctx)
BuildRequires:  go(github.com/sourcegraph/go-diff)
BuildRequires:  go(github.com/spaolacci/murmur3)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spf13/cast)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/jwalterweatherman)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/spf13/viper)
BuildRequires:  go(github.com/spiffe/go-spiffe/v2)
BuildRequires:  go(github.com/splunk/stef/go/grpc)
BuildRequires:  go(github.com/splunk/stef/go/otel)
BuildRequires:  go(github.com/splunk/stef/go/pdata)
BuildRequires:  go(github.com/splunk/stef/go/pkg)
BuildRequires:  go(github.com/ssgreg/nlreturn/v2)
BuildRequires:  go(github.com/stackitcloud/stackit-sdk-go/core)
BuildRequires:  go(github.com/stbenjam/no-sprintf-host-port)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/subosito/gotenv)
BuildRequires:  go(github.com/tedsuo/rata)
BuildRequires:  go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common)
BuildRequires:  go(github.com/testcontainers/testcontainers-go)
BuildRequires:  go(github.com/tetafro/godot)
BuildRequires:  go(github.com/tg123/go-htpasswd)
BuildRequires:  go(github.com/thda/tds)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/match)
BuildRequires:  go(github.com/tidwall/pretty)
BuildRequires:  go(github.com/tidwall/tinylru)
BuildRequires:  go(github.com/tidwall/wal)
BuildRequires:  go(github.com/tilinna/clock)
BuildRequires:  go(github.com/timakin/bodyclose)
BuildRequires:  go(github.com/timonwong/loggercheck)
BuildRequires:  go(github.com/tinylib/msgp)
BuildRequires:  go(github.com/tj/assert)
BuildRequires:  go(github.com/tjfoc/gmsm)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/tklauser/numcpus)
BuildRequires:  go(github.com/tomarrell/wrapcheck/v2)
BuildRequires:  go(github.com/tommy-muehle/go-mnd/v2)
BuildRequires:  go(github.com/traceloop/go-openllmetry/semconv-ai)
BuildRequires:  go(github.com/twmb/franz-go)
BuildRequires:  go(github.com/twmb/franz-go/pkg/kadm)
BuildRequires:  go(github.com/twmb/franz-go/pkg/kfake)
BuildRequires:  go(github.com/twmb/franz-go/pkg/kmsg)
BuildRequires:  go(github.com/twmb/franz-go/pkg/sasl/kerberos)
BuildRequires:  go(github.com/twmb/franz-go/plugin/kzap)
BuildRequires:  go(github.com/twmb/murmur3)
BuildRequires:  go(github.com/twpayne/go-geom)
BuildRequires:  go(github.com/ua-parser/uap-go)
BuildRequires:  go(github.com/ultraware/funlen)
BuildRequires:  go(github.com/ultraware/whitespace)
BuildRequires:  go(github.com/uudashr/gocognit)
BuildRequires:  go(github.com/uudashr/iface)
BuildRequires:  go(github.com/valyala/fastjson)
BuildRequires:  go(github.com/vektah/gqlparser/v2)
BuildRequires:  go(github.com/vincent-petithory/dataurl)
BuildRequires:  go(github.com/vmihailenco/msgpack/v5)
BuildRequires:  go(github.com/vmihailenco/tagparser/v2)
BuildRequires:  go(github.com/vmware/go-vmware-nsxt)
BuildRequires:  go(github.com/vmware/govmomi)
BuildRequires:  go(github.com/vultr/govultr/v3)
BuildRequires:  go(github.com/wadey/gocovmerge)
BuildRequires:  go(github.com/wk8/go-ordered-map/v2)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(github.com/xanzy/ssh-agent)
BuildRequires:  go(github.com/xdg-go/pbkdf2)
BuildRequires:  go(github.com/xdg-go/scram)
BuildRequires:  go(github.com/xdg-go/stringprep)
BuildRequires:  go(github.com/xeipuuv/gojsonpointer)
BuildRequires:  go(github.com/xeipuuv/gojsonreference)
BuildRequires:  go(github.com/xeipuuv/gojsonschema)
BuildRequires:  go(github.com/xen0n/gosmopolitan)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(github.com/yagipy/maintidx)
BuildRequires:  go(github.com/yeya24/promlinter)
BuildRequires:  go(github.com/ykadowak/zerologlint)
BuildRequires:  go(github.com/yosida95/uritemplate/v3)
BuildRequires:  go(github.com/youmark/pkcs8)
BuildRequires:  go(github.com/yuin/gopher-lua)
BuildRequires:  go(github.com/yusufpapurcu/wmi)
BuildRequires:  go(github.com/zeebo/xxh3)
BuildRequires:  go(gitlab.com/bosi/decorder)
BuildRequires:  go(gitlab.com/gitlab-org/api/client-go/v2)
BuildRequires:  go(go-simpler.org/musttag)
BuildRequires:  go(go-simpler.org/sloglint)
BuildRequires:  go(go.augendre.info/arangolint)
BuildRequires:  go(go.augendre.info/fatcontext)
BuildRequires:  go(go.einride.tech/aip)
BuildRequires:  go(go.elastic.co/fastjson)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(go.mongodb.org/atlas)
BuildRequires:  go(go.mongodb.org/mongo-driver)
BuildRequires:  go(go.mongodb.org/mongo-driver/v2)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/build-tools)
BuildRequires:  go(go.opentelemetry.io/build-tools/checkapi)
BuildRequires:  go(go.opentelemetry.io/build-tools/checkfile)
BuildRequires:  go(go.opentelemetry.io/build-tools/chloggen)
BuildRequires:  go(go.opentelemetry.io/build-tools/crosslink)
BuildRequires:  go(go.opentelemetry.io/build-tools/githubgen)
BuildRequires:  go(go.opentelemetry.io/build-tools/issuegenerator)
BuildRequires:  go(go.opentelemetry.io/build-tools/multimod)
BuildRequires:  go(go.opentelemetry.io/collector)
BuildRequires:  go(go.opentelemetry.io/collector/client)
BuildRequires:  go(go.opentelemetry.io/collector/cmd/builder)
BuildRequires:  go(go.opentelemetry.io/collector/cmd/mdatagen)
BuildRequires:  go(go.opentelemetry.io/collector/component)
BuildRequires:  go(go.opentelemetry.io/collector/component/componentstatus)
BuildRequires:  go(go.opentelemetry.io/collector/component/componenttest)
BuildRequires:  go(go.opentelemetry.io/collector/config/configauth)
BuildRequires:  go(go.opentelemetry.io/collector/config/configcompression)
BuildRequires:  go(go.opentelemetry.io/collector/config/configgrpc)
BuildRequires:  go(go.opentelemetry.io/collector/config/confighttp)
BuildRequires:  go(go.opentelemetry.io/collector/config/configmiddleware)
BuildRequires:  go(go.opentelemetry.io/collector/config/confignet)
BuildRequires:  go(go.opentelemetry.io/collector/config/configopaque)
BuildRequires:  go(go.opentelemetry.io/collector/config/configoptional)
BuildRequires:  go(go.opentelemetry.io/collector/config/configretry)
BuildRequires:  go(go.opentelemetry.io/collector/config/configtelemetry)
BuildRequires:  go(go.opentelemetry.io/collector/config/configtls)
BuildRequires:  go(go.opentelemetry.io/collector/confmap)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/envprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/fileprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/httpprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/provider/yamlprovider)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/xconfmap)
BuildRequires:  go(go.opentelemetry.io/collector/connector)
BuildRequires:  go(go.opentelemetry.io/collector/connector/connectortest)
BuildRequires:  go(go.opentelemetry.io/collector/connector/xconnector)
BuildRequires:  go(go.opentelemetry.io/collector/consumer)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumererror)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumererror/xconsumererror)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/consumertest)
BuildRequires:  go(go.opentelemetry.io/collector/consumer/xconsumer)
BuildRequires:  go(go.opentelemetry.io/collector/exporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/debugexporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/exporterhelper)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/exporterhelper/xexporterhelper)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/exportertest)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/nopexporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/otlpexporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/otlphttpexporter)
BuildRequires:  go(go.opentelemetry.io/collector/exporter/xexporter)
BuildRequires:  go(go.opentelemetry.io/collector/extension)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensionauth)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensionauth/extensionauthtest)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensioncapabilities)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensionmiddleware)
BuildRequires:  go(go.opentelemetry.io/collector/extension/extensiontest)
BuildRequires:  go(go.opentelemetry.io/collector/extension/xextension)
BuildRequires:  go(go.opentelemetry.io/collector/extension/zpagesextension)
BuildRequires:  go(go.opentelemetry.io/collector/featuregate)
BuildRequires:  go(go.opentelemetry.io/collector/filter)
BuildRequires:  go(go.opentelemetry.io/collector/internal/componentalias)
BuildRequires:  go(go.opentelemetry.io/collector/internal/fanoutconsumer)
BuildRequires:  go(go.opentelemetry.io/collector/internal/memorylimiter)
BuildRequires:  go(go.opentelemetry.io/collector/internal/schemagen)
BuildRequires:  go(go.opentelemetry.io/collector/internal/sharedcomponent)
BuildRequires:  go(go.opentelemetry.io/collector/internal/telemetry)
BuildRequires:  go(go.opentelemetry.io/collector/otelcol)
BuildRequires:  go(go.opentelemetry.io/collector/otelcol/otelcoltest)
BuildRequires:  go(go.opentelemetry.io/collector/pdata)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/pprofile)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/testdata)
BuildRequires:  go(go.opentelemetry.io/collector/pdata/xpdata)
BuildRequires:  go(go.opentelemetry.io/collector/pipeline)
BuildRequires:  go(go.opentelemetry.io/collector/pipeline/xpipeline)
BuildRequires:  go(go.opentelemetry.io/collector/processor)
BuildRequires:  go(go.opentelemetry.io/collector/processor/batchprocessor)
BuildRequires:  go(go.opentelemetry.io/collector/processor/memorylimiterprocessor)
BuildRequires:  go(go.opentelemetry.io/collector/processor/processorhelper)
BuildRequires:  go(go.opentelemetry.io/collector/processor/processorhelper/xprocessorhelper)
BuildRequires:  go(go.opentelemetry.io/collector/processor/processortest)
BuildRequires:  go(go.opentelemetry.io/collector/processor/xprocessor)
BuildRequires:  go(go.opentelemetry.io/collector/receiver)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/otlpreceiver)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/receiverhelper)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/receivertest)
BuildRequires:  go(go.opentelemetry.io/collector/receiver/xreceiver)
BuildRequires:  go(go.opentelemetry.io/collector/scraper)
BuildRequires:  go(go.opentelemetry.io/collector/scraper/scraperhelper)
BuildRequires:  go(go.opentelemetry.io/collector/scraper/scraperhelper/xscraperhelper)
BuildRequires:  go(go.opentelemetry.io/collector/scraper/scrapertest)
BuildRequires:  go(go.opentelemetry.io/collector/scraper/xscraper)
BuildRequires:  go(go.opentelemetry.io/collector/semconv)
BuildRequires:  go(go.opentelemetry.io/collector/service)
BuildRequires:  go(go.opentelemetry.io/collector/service/hostcapabilities)
BuildRequires:  go(go.opentelemetry.io/contrib/bridges/otelzap)
BuildRequires:  go(go.opentelemetry.io/contrib/detectors/gcp)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/contrib/otelconf)
BuildRequires:  go(go.opentelemetry.io/contrib/propagators/b3)
BuildRequires:  go(go.opentelemetry.io/contrib/zpages)
BuildRequires:  go(go.opentelemetry.io/ebpf-profiler)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploggrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/prometheus)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutlog)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdoutmetric)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
BuildRequires:  go(go.opentelemetry.io/otel/log)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/schema)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/log)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/log/logtest)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.opentelemetry.io/proto/otlp)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/automaxprocs)
BuildRequires:  go(go.uber.org/dig)
BuildRequires:  go(go.uber.org/fx)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/mock)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.uber.org/zap/exp)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(go4.org/netipx)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/exp/typeparams)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/telemetry)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/vuln)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/evanphx/json-patch.v4)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/ini.v1)
BuildRequires:  go(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  go(gopkg.in/warnings.v0)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(gotest.tools)
BuildRequires:  go(gotest.tools/assert)
BuildRequires:  go(gotest.tools/gotestsum)
BuildRequires:  go(honnef.co/go/tools)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/client-go)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/kubelet)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(modernc.org/b/v2)
BuildRequires:  go(modernc.org/libc)
BuildRequires:  go(modernc.org/mathutil)
BuildRequires:  go(modernc.org/memory)
BuildRequires:  go(modernc.org/sqlite)
BuildRequires:  go(mvdan.cc/gofumpt)
BuildRequires:  go(mvdan.cc/unparam)
BuildRequires:  go(sigs.k8s.io/controller-runtime)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)
BuildRequires:  go(skywalking.apache.org/repo/goapi)
BuildRequires:  go(software.sslmate.com/src/go-pkcs12)
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata

Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/codecovgen) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/golden) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/golden/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/opampsupervisor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/opampsupervisor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/opampsupervisor/supervisor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/opampsupervisor/supervisor/commander) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/opampsupervisor/supervisor/config) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/opampsupervisor/supervisor/extensions) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/opampsupervisor/supervisor/telemetry) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/schemagen) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/schemagen/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/telemetrygen) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/telemetrygen/internal/config) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/telemetrygen/internal/e2etest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/telemetrygen/internal/log) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/telemetrygen/internal/validate) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/telemetrygen/pkg) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/telemetrygen/pkg/logs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/telemetrygen/pkg/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/cmd/telemetrygen/pkg/traces) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/confmap/provider/aesprovider) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/confmap/provider/googlesecretmanagerprovider) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/confmap/provider/s3provider) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/confmap/provider/secretsmanagerprovider) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/countconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/countconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/datadogconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/datadogconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/exceptionsconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/exceptionsconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/failoverconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/failoverconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/failoverconnector/internal/state) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/grafanacloudconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/grafanacloudconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/grafanacloudconnector/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/metricsaslogsconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/metricsaslogsconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/otlpjsonconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/otlpjsonconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/roundrobinconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/roundrobinconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/routingconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/routingconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/routingconnector/internal/pdatautil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/routingconnector/internal/plogutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/routingconnector/internal/plogutiltest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/routingconnector/internal/pmetricutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/routingconnector/internal/pmetricutiltest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/routingconnector/internal/ptraceutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/routingconnector/internal/ptraceutiltest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/servicegraphconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/servicegraphconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/servicegraphconnector/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/servicegraphconnector/internal/store) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/signaltometricsconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/signaltometricsconnector/config) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/signaltometricsconnector/internal/aggregator) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/signaltometricsconnector/internal/customottl) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/signaltometricsconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/signaltometricsconnector/internal/model) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/slowsqlconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/slowsqlconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/spanmetricsconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/spanmetricsconnector/internal/cache) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/spanmetricsconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/spanmetricsconnector/internal/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/sumconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/connector/sumconnector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/alertmanagerexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/alertmanagerexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/alibabacloudlogserviceexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/alibabacloudlogserviceexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awscloudwatchlogsexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awscloudwatchlogsexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awsemfexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awsemfexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awskinesisexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awskinesisexporter/internal/batch) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awskinesisexporter/internal/compress) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awskinesisexporter/internal/key) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awskinesisexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awskinesisexporter/internal/producer) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awss3exporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awss3exporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awss3exporter/internal/upload) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awsxrayexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awsxrayexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/awsxrayexporter/internal/translator) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/azureblobexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/azureblobexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/azuredataexplorerexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/azuredataexplorerexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/azuremonitorexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/azuremonitorexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/bmchelixexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/bmchelixexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/bmchelixexporter/internal/operationsmanagement) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/cassandraexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/cassandraexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/clickhouseexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/clickhouseexporter/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/clickhouseexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/clickhouseexporter/internal/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/clickhouseexporter/internal/sqltemplates) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/coralogixexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/coralogixexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/coralogixexporter/internal/validation) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/datadogexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/datadogexporter/integrationtest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/datadogexporter/internal/logs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/datadogexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/datadogexporter/internal/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/datadogexporter/internal/metrics/sketches) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/datasetexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/datasetexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/dorisexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/dorisexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/integrationtest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/datapoints) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/elasticsearch) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/exphistogram) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/logging) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/lru) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/metricgroup) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/objmodel) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/pool) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/serializer) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/serializer/otelserializer) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/elasticsearchexporter/internal/serializer/otelserializer/serializeprofiles) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/faroexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/faroexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/fileexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/fileexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlecloudexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlecloudexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlecloudexporter/internal/resourcemapping) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlecloudpubsubexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlecloudpubsubexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlecloudstorageexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlecloudstorageexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlemanagedprometheusexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/googlemanagedprometheusexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/honeycombmarkerexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/honeycombmarkerexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/influxdbexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/influxdbexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/kafkaexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/kafkaexporter/internal/kafkaclient) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/kafkaexporter/internal/marshaler) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/kafkaexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/kafkaexporter/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/loadbalancingexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/loadbalancingexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/loadbalancingexporter/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/logicmonitorexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/logicmonitorexporter/internal/logs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/logicmonitorexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/logicmonitorexporter/internal/testutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/logicmonitorexporter/internal/traces) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/logzioexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/logzioexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/mezmoexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/mezmoexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/opensearchexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/opensearchexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/opensearchexporter/internal/objmodel) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/opensearchexporter/internal/pool) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/opensearchexporter/internal/serializer) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/otelarrowexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/otelarrowexporter/internal/arrow) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/otelarrowexporter/internal/arrow/grpcmock) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/otelarrowexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/prometheusexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/prometheusexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/prometheusremotewriteexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/prometheusremotewriteexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/prometheusremotewriteexporter/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/pulsarexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/pulsarexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/rabbitmqexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/rabbitmqexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/rabbitmqexporter/internal/publisher) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sematextexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sematextexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sentryexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sentryexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sentryexporter/internal/ratelimit) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter/internal/apm/correlations) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter/internal/apm/log) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter/internal/apm/requests) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter/internal/apm/requests/requestcounter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter/internal/apm/tracetracker) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter/internal/correlation) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter/internal/dimensions) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter/internal/hostmetadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter/internal/translation) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/signalfxexporter/internal/translation/dpfilters) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/splunkhecexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/splunkhecexporter/internal/integrationtestutils) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/splunkhecexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/stefexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/stefexporter/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/stefexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sumologicexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sumologicexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/sumologicexporter/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/syslogexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/syslogexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/tencentcloudlogserviceexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/tencentcloudlogserviceexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/tencentcloudlogserviceexporter/internal/proto) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/tinybirdexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/tinybirdexporter/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/tinybirdexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/zipkinexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/exporter/zipkinexporter/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/ackextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/ackextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/asapauthextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/asapauthextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/awsproxy) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/awsproxy/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/azureauthextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/azureauthextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/basicauthextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/basicauthextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/bearertokenauthextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/bearertokenauthextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/cgroupruntimeextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/cgroupruntimeextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/datadogextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/datadogextension/internal/componentchecker) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/datadogextension/internal/httpserver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/datadogextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/datadogextension/internal/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/datadogextension/internal/payload) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/avrologencodingextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/avrologencodingextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awscloudwatchmetricstreamsencodingextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awscloudwatchmetricstreamsencodingextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awslogsencodingextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awslogsencodingextension/internal/constants) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awslogsencodingextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awslogsencodingextension/internal/unmarshaler) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awslogsencodingextension/internal/unmarshaler/cloudtraillog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awslogsencodingextension/internal/unmarshaler/elb-access-log) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awslogsencodingextension/internal/unmarshaler/network-firewall-log) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awslogsencodingextension/internal/unmarshaler/s3-access-log) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awslogsencodingextension/internal/unmarshaler/subscription-filter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awslogsencodingextension/internal/unmarshaler/vpc-flow-log) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/awslogsencodingextension/internal/unmarshaler/waf) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/azureencodingextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/azureencodingextension/internal/constants) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/azureencodingextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/azureencodingextension/internal/unmarshaler) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/azureencodingextension/internal/unmarshaler/logs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/azureencodingextension/internal/unmarshaler/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/azureencodingextension/internal/unmarshaler/traces) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/googlecloudlogentryencodingextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/googlecloudlogentryencodingextension/internal/apploadbalancerlog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/googlecloudlogentryencodingextension/internal/auditlog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/googlecloudlogentryencodingextension/internal/constants) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/googlecloudlogentryencodingextension/internal/dnslog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/googlecloudlogentryencodingextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/googlecloudlogentryencodingextension/internal/passthroughnlb) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/googlecloudlogentryencodingextension/internal/proxynlb) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/googlecloudlogentryencodingextension/internal/shared) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/googlecloudlogentryencodingextension/internal/vpcflowlog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/jaegerencodingextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/jaegerencodingextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/jsonlogencodingextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/jsonlogencodingextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/otlpencodingextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/otlpencodingextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/skywalkingencodingextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/skywalkingencodingextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/textencodingextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/textencodingextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/zipkinencodingextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/encoding/zipkinencodingextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/googleclientauthextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/googleclientauthextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/headerssetterextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/headerssetterextension/internal/action) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/headerssetterextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/headerssetterextension/internal/source) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/healthcheckextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/healthcheckextension/internal/healthcheck) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/healthcheckextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/healthcheckv2extension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/healthcheckv2extension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/httpforwarderextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/httpforwarderextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/internal/basicauth) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/internal/credentialsfile) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/jaegerremotesampling) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/jaegerremotesampling/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/jaegerremotesampling/internal/mocks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/jaegerremotesampling/internal/server/grpc) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/jaegerremotesampling/internal/server/http) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/jaegerremotesampling/internal/source) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/jaegerremotesampling/internal/source/filesource) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/jaegerremotesampling/internal/source/remotesource) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/k8sleaderelector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/k8sleaderelector/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/mcp) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/mcp/internal/mcp/tools) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/mcp/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/oauth2clientauthextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/oauth2clientauthextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/cfgardenobserver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/cfgardenobserver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/dockerobserver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/dockerobserver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/ecsobserver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/ecsobserver/internal/ecsmock) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/ecsobserver/internal/errctx) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/ecsobserver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/endpointswatcher) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/hostobserver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/hostobserver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/k8sobserver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/k8sobserver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/kafkatopicsobserver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/observer/kafkatopicsobserver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/oidcauthextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/oidcauthextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/opampcustommessages) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/opampextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/opampextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/pprofextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/pprofextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/remotetapextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/remotetapextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/sigv4authextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/sigv4authextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/solarwindsapmsettingsextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/solarwindsapmsettingsextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/storage) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/storage/dbstorage) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/storage/dbstorage/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/storage/filestorage) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/storage/filestorage/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/storage/redisstorageextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/storage/redisstorageextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/storage/storagetest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/sumologicextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/sumologicextension/internal/api) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/sumologicextension/internal/credentials) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/sumologicextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/sumologicextension/internal/procx) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/tailstorage/pebbletailstorageextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/tailstorage/pebbletailstorageextension/integrationtest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/extension/tailstorage/pebbletailstorageextension/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/awsutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/containerinsight) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/cwlogs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/cwlogs/handler) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/ecsutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/ecsutil/ecsutiltest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/ecsutil/endpoints) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/k8s) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/k8s/k8sclient) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/k8s/k8sutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/proxy) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/xray) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/xray/telemetry) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/aws/xray/telemetry/telemetrytest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/collectd) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/common) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/common/docker) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/common/maps) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/common/priorityqueue) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/common/sanitize) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/common/testutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/common/ttlmap) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/aggregateutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/attraction) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/clientutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/consumerretry) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/errorutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/goldendataset) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/metricstestutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/occonventions) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/parseutils) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/scraperinttest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/textutils) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/timeutils) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/timeutils/internal/ctimefmt) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/tracetranslator) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/coreinternal/traceutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/clientutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/e2e) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/hostmetadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/hostmetadata/internal/azure) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/hostmetadata/internal/ec2) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/hostmetadata/internal/ecs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/hostmetadata/internal/gcp) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/hostmetadata/internal/gohai) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/hostmetadata/internal/k8s) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/hostmetadata/internal/system) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/hostmetadata/provider) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/datadog/scrub) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/docker) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/exp/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/exp/metrics/identity) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/exp/metrics/staleness) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter/expr) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter/filterconfig) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter/filterexpr) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter/filterlog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter/filtermatcher) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter/filtermetric) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter/filterottl) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter/filterset) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter/filterset/regexp) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter/filterset/strict) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/filter/filterspan) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/gopsutilenv) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/grpcutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/healthcheck) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/healthcheck/internal/common) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/healthcheck/internal/grpc) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/healthcheck/internal/http) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/healthcheck/internal/testhelpers) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/k8sconfig) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/k8sinventory) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/k8sinventory/pull) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/k8sinventory/watch) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/k8sleaderelectortest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/kafka) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/kafka/kafkatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/kubelet) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/alibaba/ecs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/aws/ec2) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/aws/eks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/azure) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/consul) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/docker) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/ibmcloud/classic) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/ibmcloud/vpc) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/k8snode) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/kubeadm) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/openshift) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/openstack/nova) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/oraclecloud) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/system) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/tencent/cvm) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/upcloud) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/metadataproviders/vultr) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/otelarrow) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/otelarrow/admission2) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/otelarrow/compression/zstd) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/otelarrow/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/otelarrow/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/otelarrow/netstats) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/otelarrow/testutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/pdatautil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/rabbitmq) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/sharedcomponent) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/splunk) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/sqlquery) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/tools) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/batchperresourceattr) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/batchpersignal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/core/xidutils) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/datadog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/datadog/agentcomponents) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/datadog/apmstats) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/datadog/config) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/datadog/featuregates) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/datadog/hostmetadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/datadog/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/experimentalmetricmetadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/expohisto) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/expohisto/mapping) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/expohisto/mapping/exponent) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/expohisto/mapping/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/expohisto/mapping/logarithm) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/expohisto/structure) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/golden) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/kafka/configkafka) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/kafka/topic) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxcache) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxcommon) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxdatapoint) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxerror) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxexemplar) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxlog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxmetric) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxotelcol) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxprofile) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxprofilecommon) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxprofilesample) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxresource) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxscope) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxspan) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxspanevent) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/ctxutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/logging) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/logprofile) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/internal/pathtest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/ottldatapoint) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/ottlexemplar) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/ottllog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/ottlmetric) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/ottlotelcol) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/ottlprofile) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/ottlprofilesample) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/ottlresource) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/ottlscope) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/ottlspan) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/contexts/ottlspanevent) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/internal/ottlcommon) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/ottlfuncs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/ottl/ottltest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatatest/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatatest/plogtest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatatest/pmetricassert) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatatest/pmetrictest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatatest/pprofiletest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatatest/ptracetest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatautil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/resourcetotelemetry) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/sampling) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/adapter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/entry) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/attrs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/emit) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/archive) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/checkpoint) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/checkpoint/proto) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/compression) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/emittest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/fileset) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/fingerprint) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/header) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/reader) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/scanner) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/internal/tracker) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/matcher) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/matcher/internal/filter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/fileconsumer/matcher/internal/finder) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/flush) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/internal/filetest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/internal/stanzatime) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/helper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/input/file) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/input/generate) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/input/journald) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/input/namedpipe) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/input/stdin) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/input/syslog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/input/tcp) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/input/udp) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/input/windows) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/operatortest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/output/drop) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/output/file) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/output/stdout) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/container) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/csv) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/jsonarray) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/jsonparser) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/keyvalue) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/regex) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/scope) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/severity) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/syslog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/syslog/syslogtest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/timeparser) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/trace) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/parser/uri) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/add) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/assignkeys) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/copy) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/filter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/flatten) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/move) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/noop) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/recombine) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/regexreplace) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/remove) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/retain) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/router) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/sanitizeutf8) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/operator/transformer/unquote) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/pipeline) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/split) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/split/splittest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/stanzaerrors) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/testutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/tokenlen) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/stanza/trim) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/status) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/status/testhelpers) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/azure) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/azurelogs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/azurelogs/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/faro) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/jaeger) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/jaeger/jaegerthriftcoverter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/loki) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/pprof) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/prometheus) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/prometheus/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/prometheusremotewrite) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/signalfx) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/skywalking) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/skywalking/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/splunk) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/zipkin) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/zipkin/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/zipkin/internal/zipkin) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/zipkin/zipkinthriftconverter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/zipkin/zipkinv1) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/translator/zipkin/zipkinv2) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/winperfcounters) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/winperfcounters/internal/third_party/telegraf/win_perf_counters) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/xk8stest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/xstreamencoding) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/attributesprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/attributesprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/awsecsattributesprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/awsecsattributesprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/cardinalityguardianprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/cardinalityguardianprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/cardinalityguardianprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/coralogixprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/coralogixprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/coralogixprocessor/internal/transactions) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/cumulativetodeltaprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/cumulativetodeltaprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/cumulativetodeltaprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/cumulativetodeltaprocessor/internal/tracking) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/data) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/data/expo) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/data/expo/expotest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/data/histo) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/data/histo/histotest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/delta) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/maps) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/putil/pslice) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/telemetry) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/testing/sdktest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/testing/testar) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor/internal/testing/testar/crlf) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatorateprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatorateprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/drainprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/drainprocessor/internal/drain) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/drainprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/drainprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/filterprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/filterprocessor/internal/condition) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/filterprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/filterprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/genainormalizerprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/genainormalizerprocessor/internal/custom) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/genainormalizerprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/genainormalizerprocessor/internal/openinference) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/genainormalizerprocessor/internal/openllmetry) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/genainormalizerprocessor/internal/otelsemconv) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/geoipprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/geoipprocessor/internal/convention) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/geoipprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/geoipprocessor/internal/provider) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/geoipprocessor/internal/provider/maxmindprovider) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/groupbyattrsprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/groupbyattrsprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/groupbyattrsprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/groupbytraceprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/groupbytraceprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/groupbytraceprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/intervalprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/intervalprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/intervalprocessor/internal/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/isolationforestprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/isolationforestprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/k8sattributesprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/k8sattributesprocessor/internal/kube) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/k8sattributesprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/k8sattributesprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/logdedupprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/logdedupprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/logdedupprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/logstransformprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/logstransformprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/lookupprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/lookupprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/lookupprocessor/internal/source/dns) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/lookupprocessor/internal/source/noop) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/lookupprocessor/internal/source/yaml) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/lookupprocessor/lookupsource) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricsgenerationprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricsgenerationprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstarttimeprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstarttimeprocessor/internal/datapointstorage) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstarttimeprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstarttimeprocessor/internal/starttimemetric) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstarttimeprocessor/internal/subtractinitial) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstarttimeprocessor/internal/testhelper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstarttimeprocessor/internal/truereset) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstransformprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/metricstransformprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/probabilisticsamplerprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/probabilisticsamplerprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/probabilisticsamplerprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/redactionprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/redactionprocessor/internal/db) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/redactionprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/redactionprocessor/internal/url) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/remotetapprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/remotetapprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/akamai) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/akamai/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/alibaba/ecs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/alibaba/ecs/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/aws/ec2) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/aws/ec2/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/aws/ecs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/aws/ecs/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/aws/eks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/aws/eks/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/aws/elasticbeanstalk) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/aws/elasticbeanstalk/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/aws/lambda) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/aws/lambda/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/azure) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/azure/aks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/azure/aks/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/azure/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/consul) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/consul/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/digitalocean) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/digitalocean/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/docker) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/docker/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/dynatrace) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/dynatrace/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/env) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/gcp) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/gcp/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/heroku) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/heroku/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/hetzner) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/hetzner/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/ibmcloud/classic) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/ibmcloud/classic/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/ibmcloud/vpc) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/ibmcloud/vpc/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/k8sapi) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/k8sapi/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/kubeadm) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/kubeadm/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/openshift) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/openshift/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/openstack/nova) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/openstack/nova/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/oraclecloud) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/oraclecloud/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/scaleway) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/scaleway/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/system) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/system/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/tencent/cvm) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/tencent/cvm/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/upcloud) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/upcloud/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/vultr) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourcedetectionprocessor/internal/vultr/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourceprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/resourceprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/schemaprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/schemaprocessor/internal/alias) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/schemaprocessor/internal/changelist) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/schemaprocessor/internal/fixture) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/schemaprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/schemaprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/schemaprocessor/internal/migrate) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/schemaprocessor/internal/race) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/schemaprocessor/internal/transformer) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/schemaprocessor/internal/translation) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/spanprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/spanprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/spanpruningprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/spanpruningprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/spanpruningprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/sumologicprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/sumologicprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor/cache) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor/internal/idbatcher) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor/internal/sampling) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor/internal/tailstorageextension) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor/internal/telemetry) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/tailsamplingprocessor/pkg/samplingpolicy) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/transformprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/transformprocessor/internal/common) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/transformprocessor/internal/logs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/transformprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/transformprocessor/internal/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/transformprocessor/internal/profiles) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/transformprocessor/internal/traces) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/unrollprocessor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/unrollprocessor/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/activedirectorydsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/activedirectorydsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/aerospikereceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/aerospikereceiver/cluster) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/aerospikereceiver/internal/cluster/mocks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/aerospikereceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/aerospikereceiver/internal/mocks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/apachereceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/apachereceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/apachesparkreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/apachesparkreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/apachesparkreceiver/internal/mocks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/apachesparkreceiver/internal/models) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscloudwatchreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscloudwatchreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscontainerinsightreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscontainerinsightreceiver/internal/cadvisor) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscontainerinsightreceiver/internal/cadvisor/extractors) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscontainerinsightreceiver/internal/cadvisor/testutils) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscontainerinsightreceiver/internal/ecsInfo) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscontainerinsightreceiver/internal/host) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscontainerinsightreceiver/internal/k8sapiserver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscontainerinsightreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscontainerinsightreceiver/internal/stores) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awscontainerinsightreceiver/internal/stores/kubeletutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsecscontainermetricsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsecscontainermetricsreceiver/internal/awsecscontainermetrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsecscontainermetricsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsfirehosereceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsfirehosereceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsfirehosereceiver/internal/unmarshaler/cwlog) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsfirehosereceiver/internal/unmarshaler/cwmetricstream) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsfirehosereceiver/internal/unmarshaler/unmarshalertest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awslambdareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awslambdareceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awslambdareceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awss3receiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awss3receiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsxrayreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsxrayreceiver/internal/errors) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsxrayreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsxrayreceiver/internal/socketconn) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsxrayreceiver/internal/tracesegment) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsxrayreceiver/internal/translator) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/awsxrayreceiver/internal/udppoller) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azureblobreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azureblobreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azureeventhubreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azureeventhubreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azurefunctionsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azurefunctionsreceiver/internal/eventhub) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azurefunctionsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azurefunctionsreceiver/internal/protocol) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azurefunctionsreceiver/internal/transport) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azurefunctionsreceiver/internal/trigger) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azuremonitorreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/azuremonitorreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/carbonreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/carbonreceiver/internal/client) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/carbonreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/carbonreceiver/internal/transport) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/carbonreceiver/protocol) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/chronyreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/chronyreceiver/internal/chrony) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/chronyreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/ciscoosreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/ciscoosreceiver/internal/connection) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/ciscoosreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/ciscoosreceiver/internal/scraper/interfacesscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/ciscoosreceiver/internal/scraper/interfacesscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/ciscoosreceiver/internal/scraper/systemscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/ciscoosreceiver/internal/scraper/systemscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/cloudflarereceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/cloudflarereceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/cloudfoundryreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/cloudfoundryreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/collectdreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/collectdreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/couchdbreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/couchdbreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/datadogreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/datadogreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/datadogreceiver/internal/translator) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/datadogreceiver/internal/translator/header) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/dockerstatsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/dockerstatsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/elasticsearchreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/elasticsearchreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/elasticsearchreceiver/internal/mocks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/elasticsearchreceiver/internal/model) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/envoyalsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/envoyalsreceiver/internal/als) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/envoyalsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/expvarreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/expvarreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/faroreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/faroreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/filelogreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/filelogreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/filelogreceiver/internal/testutil) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/filestatsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/filestatsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/flinkmetricsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/flinkmetricsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/flinkmetricsreceiver/internal/mocks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/flinkmetricsreceiver/internal/models) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/fluentforwardreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/fluentforwardreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/fluentforwardreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/fluentforwardreceiver/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/githubreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/githubreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/githubreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/githubreceiver/internal/scraper/githubscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/gitlabreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/gitlabreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudmonitoringreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudmonitoringreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudmonitoringreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudpubsubpushreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudpubsubpushreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudpubsubpushreceiver/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudpubsubreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudpubsubreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudpubsubreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudpubsubreceiver/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudspannerreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudspannerreceiver/internal/datasource) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudspannerreceiver/internal/filter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudspannerreceiver/internal/filterfactory) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudspannerreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudspannerreceiver/internal/metadataparser) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/googlecloudspannerreceiver/internal/statsreader) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/haproxyreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/haproxyreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/precision) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/cpuscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/cpuscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/cpuscraper/ucal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/diskscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/diskscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/filesystemscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/filesystemscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/loadscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/loadscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/memoryscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/memoryscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/networkscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/networkscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/nfsscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/nfsscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/pagingscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/pagingscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/processesscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/processesscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/processscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/processscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/processscraper/ucal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/systemscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/scraper/systemscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/hostmetricsreceiver/internal/testmocks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/httpcheckreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/httpcheckreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/huaweicloudcesreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/huaweicloudcesreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/huaweicloudcesreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/huaweicloudcesreceiver/internal/mocks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/icmpcheckreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/icmpcheckreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/iisreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/iisreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/influxdbreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/influxdbreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jaegerreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jaegerreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jaegerreceiver/internal/udpserver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jaegerreceiver/internal/udpserver/thriftudp) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jmxreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jmxreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/jmxreceiver/internal/subprocess) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/journaldreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/journaldreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/clusterresourcequota) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/collection) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/constants) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/container) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/cronjob) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/daemonset) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/deployment) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/endpointslice) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/gvk) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/hpa) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/jobs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/namespace) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/node) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/persistentvolume) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/persistentvolumeclaim) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/pod) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/replicaset) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/replicationcontroller) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/resourcequota) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/service) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/statefulset) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sclusterreceiver/internal/testutils) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8seventsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8seventsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8seventsreceiver/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sobjectsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/k8sobjectsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kafkametricsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kafkametricsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kafkareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kafkareceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kafkareceiver/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kafkareceiver/internal/unmarshaler) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kubeletstatsreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kubeletstatsreceiver/internal/kubelet) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/kubeletstatsreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/libhoneyreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/libhoneyreceiver/internal/codec) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/libhoneyreceiver/internal/eventtime) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/libhoneyreceiver/internal/libhoneyevent) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/libhoneyreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/libhoneyreceiver/internal/parser) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/libhoneyreceiver/internal/response) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/lokireceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/lokireceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/lokireceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/macosunifiedloggingreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/macosunifiedloggingreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/memcachedreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/memcachedreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/mongodbatlasreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/mongodbatlasreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/mongodbatlasreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/mongodbatlasreceiver/internal/model) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/mongodbreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/mongodbreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/mysqlreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/mysqlreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/namedpipereceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/namedpipereceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/netflowreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/netflowreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/nginxreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/nginxreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/nsxtreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/nsxtreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/nsxtreceiver/internal/model) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/ntpreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/ntpreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/oracledbreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/oracledbreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/osqueryreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/osqueryreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otelarrowreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otelarrowreceiver/internal/arrow) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otelarrowreceiver/internal/arrow/mock) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otelarrowreceiver/internal/logs) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otelarrowreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otelarrowreceiver/internal/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otelarrowreceiver/internal/statuserr) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otelarrowreceiver/internal/testconsumer) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otelarrowreceiver/internal/trace) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otlpjsonfilereceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/otlpjsonfilereceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/podmanreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/podmanreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/postgresqlreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/postgresqlreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/pprofreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/pprofreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/pprofreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusreceiver/internal/targetallocator) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusremotewritereceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/prometheusremotewritereceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/pulsarreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/pulsarreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/purefareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/purefareceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/purefareceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/purefbreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/purefbreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/purefbreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/rabbitmqreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/rabbitmqreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/rabbitmqreceiver/internal/mocks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/rabbitmqreceiver/internal/models) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/receivercreator) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/receivercreator/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/redfishreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/redfishreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/redfishreceiver/internal/redfish) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/redisreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/redisreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/riakreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/riakreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/riakreceiver/internal/mocks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/riakreceiver/internal/model) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/saphanareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/saphanareceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/signalfxreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/signalfxreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/simpleprometheusreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/simpleprometheusreceiver/examples/federation/prom-counter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/simpleprometheusreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/skywalkingreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/skywalkingreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/skywalkingreceiver/internal/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/skywalkingreceiver/internal/trace) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/snmpreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/snmpreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/snmpreceiver/internal/mocks) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/snowflakereceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/snowflakereceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/solacereceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/solacereceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/solacereceiver/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/solacereceiver/internal/model/egress/v1) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/solacereceiver/internal/model/move/v1) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/solacereceiver/internal/model/receive/v1) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/splunkenterprisereceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/splunkenterprisereceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/splunkhecreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/splunkhecreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/sqlqueryreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/sqlqueryreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/sqlqueryreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/sqlserverreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/sqlserverreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/sshcheckreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/sshcheckreceiver/internal/configssh) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/sshcheckreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/statsdreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/statsdreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/statsdreceiver/internal/metadatatest) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/statsdreceiver/internal/parser) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/statsdreceiver/internal/transport) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/statsdreceiver/internal/transport/client) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/statsdreceiver/protocol) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/stefreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/stefreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/stefreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/syslogreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/syslogreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/systemdreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/systemdreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/tcpcheckreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/tcpcheckreceiver/internal/configtcp) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/tcpcheckreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/tcplogreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/tcplogreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/tlscheckreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/tlscheckreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/udplogreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/udplogreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/vcenterreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/vcenterreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/vcenterreceiver/internal/mockserver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/vcrreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/vcrreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/wavefrontreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/wavefrontreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/webhookeventreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/webhookeventreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/windowseventlogreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/windowseventlogreceiver/internal/discovery) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/windowseventlogreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/windowseventlogreceiver/internal/sidcache) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/windowsperfcountersreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/windowsperfcountersreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/windowsservicereceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/windowsservicereceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/yanggrpcreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/yanggrpcreceiver/internal) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/yanggrpcreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/yanggrpcreceiver/internal/proto/generated/proto) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/zipkinreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/zipkinreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/zookeeperreceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/receiver/zookeeperreceiver/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/scraper/zookeeperscraper) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/scraper/zookeeperscraper/internal/metadata) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/correctnesstests) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/correctnesstests/connectors) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/correctnesstests/metrics) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/correctnesstests/traces) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/dataconnectors/routingdataconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/dataconnectors/spanmetricsdataconnector) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datareceivers/carbondatareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datareceivers/datadogdatareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datareceivers/jaegerdatareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datareceivers/otelarrowdatareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datareceivers/prometheusdatareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datareceivers/signalfxdatareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datareceivers/splunkdatareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datareceivers/stefdatareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datareceivers/syslogdatareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datareceivers/zipkindatareceiver) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/datadogdatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/fluentdatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/jaegerdatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/k8sdatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/otelarrowdatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/prometheusdatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/prometheusstaticdatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/signalfxdatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/stanzadatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/stefdatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/syslogdatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/tcpudpdatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/datasenders/zipkindatasender) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/mockdatasenders/mockdatadogagentexporter) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/testbed) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/testbed/components) = %{version}
Provides:       go(github.com/open-telemetry/opentelemetry-collector-contrib/testbed/tests) = %{version}

Requires:       go(bitbucket.org/atlassian/go-asap/v2)
Requires:       go(cloud.google.com/go/compute)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(cloud.google.com/go/monitoring)
Requires:       go(cloud.google.com/go/pubsub/v2)
Requires:       go(cloud.google.com/go/secretmanager)
Requires:       go(cloud.google.com/go/spanner)
Requires:       go(cloud.google.com/go/storage)
Requires:       go(code.cloudfoundry.org/garden)
Requires:       go(code.cloudfoundry.org/go-loggregator)
Requires:       go(github.com/Arize-ai/openinference/go/openinference-semantic-conventions)
Requires:       go(github.com/Azure/azure-kusto-go)
Requires:       go(github.com/Azure/azure-kusto-go/azkustodata)
Requires:       go(github.com/Azure/azure-kusto-go/azkustoingest)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/messaging/azeventhubs/v2)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/monitor/query/azmetrics)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/monitor/armmonitor)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resources/armresources/v3)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resources/armsubscriptions)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob)
Requires:       go(github.com/Azure/go-amqp)
Requires:       go(github.com/ClickHouse/clickhouse-go/v2)
Requires:       go(github.com/DataDog/agent-payload/v5)
Requires:       go(github.com/DataDog/datadog-agent)
Requires:       go(github.com/DataDog/datadog-agent/comp/core/config)
Requires:       go(github.com/DataDog/datadog-agent/comp/core/hostname/hostnameinterface)
Requires:       go(github.com/DataDog/datadog-agent/comp/core/log/def)
Requires:       go(github.com/DataDog/datadog-agent/comp/core/tagger/types)
Requires:       go(github.com/DataDog/datadog-agent/comp/forwarder/defaultforwarder)
Requires:       go(github.com/DataDog/datadog-agent/comp/logs/agent/config)
Requires:       go(github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline)
Requires:       go(github.com/DataDog/datadog-agent/comp/otelcol/logsagentpipeline/logsagentpipelineimpl)
Requires:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/logsagentexporter)
Requires:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/exporter/serializerexporter)
Requires:       go(github.com/DataDog/datadog-agent/comp/otelcol/otlp/components/metricsclient)
Requires:       go(github.com/DataDog/datadog-agent/comp/serializer/logscompression)
Requires:       go(github.com/DataDog/datadog-agent/comp/trace/compression/impl-gzip)
Requires:       go(github.com/DataDog/datadog-agent/pkg/config/model)
Requires:       go(github.com/DataDog/datadog-agent/pkg/config/setup)
Requires:       go(github.com/DataDog/datadog-agent/pkg/config/utils)
Requires:       go(github.com/DataDog/datadog-agent/pkg/config/viperconfig)
Requires:       go(github.com/DataDog/datadog-agent/pkg/logs/sources)
Requires:       go(github.com/DataDog/datadog-agent/pkg/metrics)
Requires:       go(github.com/DataDog/datadog-agent/pkg/obfuscate)
Requires:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/inframetadata)
Requires:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/attributes)
Requires:       go(github.com/DataDog/datadog-agent/pkg/opentelemetry-mapping-go/otlp/metrics)
Requires:       go(github.com/DataDog/datadog-agent/pkg/proto)
Requires:       go(github.com/DataDog/datadog-agent/pkg/serializer)
Requires:       go(github.com/DataDog/datadog-agent/pkg/tagset)
Requires:       go(github.com/DataDog/datadog-agent/pkg/trace)
Requires:       go(github.com/DataDog/datadog-agent/pkg/trace/exportable)
Requires:       go(github.com/DataDog/datadog-agent/pkg/trace/log)
Requires:       go(github.com/DataDog/datadog-agent/pkg/trace/otel)
Requires:       go(github.com/DataDog/datadog-agent/pkg/trace/stats)
Requires:       go(github.com/DataDog/datadog-agent/pkg/trace/traceutil)
Requires:       go(github.com/DataDog/datadog-agent/pkg/util/compression)
Requires:       go(github.com/DataDog/datadog-agent/pkg/util/hostname/validate)
Requires:       go(github.com/DataDog/datadog-agent/pkg/util/log)
Requires:       go(github.com/DataDog/datadog-agent/pkg/util/option)
Requires:       go(github.com/DataDog/datadog-agent/pkg/util/quantile)
Requires:       go(github.com/DataDog/datadog-api-client-go/v2)
Requires:       go(github.com/DataDog/datadog-go/v5)
Requires:       go(github.com/DataDog/gohai)
Requires:       go(github.com/DeRuina/timberjack)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/googlemanagedprometheus)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/extension/googleclientauthextension)
Requires:       go(github.com/Khan/genqlient)
Requires:       go(github.com/KimMachineGun/automemlimit)
Requires:       go(github.com/Masterminds/semver/v3)
Requires:       go(github.com/Microsoft/go-winio)
Requires:       go(github.com/SAP/go-hdb)
Requires:       go(github.com/SermoDigital/jose)
Requires:       go(github.com/Showmax/go-fqdn)
Requires:       go(github.com/aerospike/aerospike-client-go/v8)
Requires:       go(github.com/alecthomas/participle/v2)
Requires:       go(github.com/alexbrainman/sspi)
Requires:       go(github.com/aliyun/aliyun-log-go-sdk)
Requires:       go(github.com/antchfx/xmlquery)
Requires:       go(github.com/antchfx/xpath)
Requires:       go(github.com/apache/cassandra-gocql-driver/v2)
Requires:       go(github.com/apache/pulsar-client-go)
Requires:       go(github.com/apache/thrift)
Requires:       go(github.com/aws/aws-lambda-go)
Requires:       go(github.com/aws/aws-msk-iam-sasl-signer-go)
Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/config)
Requires:       go(github.com/aws/aws-sdk-go-v2/credentials)
Requires:       go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
Requires:       go(github.com/aws/aws-sdk-go-v2/feature/s3/transfermanager)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/cloudwatch)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/cloudwatchlogs)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ec2)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ecs)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/kinesis)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/s3)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/secretsmanager)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/servicediscovery)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sqs)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sts)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/xray)
Requires:       go(github.com/aws/smithy-go)
Requires:       go(github.com/axiomhq/hyperloglog)
Requires:       go(github.com/basgys/goxml2json)
Requires:       go(github.com/beevik/ntp)
Requires:       go(github.com/bmatcuk/doublestar/v4)
Requires:       go(github.com/buger/jsonparser)
Requires:       go(github.com/cenkalti/backoff/v4)
Requires:       go(github.com/cenkalti/backoff/v5)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/cloudfoundry-incubator/uaago)
Requires:       go(github.com/cloudfoundry/go-cfclient/v3)
Requires:       go(github.com/cockroachdb/pebble/v2)
Requires:       go(github.com/containerd/cgroups/v3)
Requires:       go(github.com/containerd/errdefs)
Requires:       go(github.com/coreos/go-oidc/v3)
Requires:       go(github.com/digitalocean/go-metadata)
Requires:       go(github.com/distribution/reference)
Requires:       go(github.com/elastic/elastic-transport-go/v8)
Requires:       go(github.com/elastic/go-docappender/v2)
Requires:       go(github.com/elastic/go-freelru)
Requires:       go(github.com/elastic/go-grok)
Requires:       go(github.com/elastic/go-structform)
Requires:       go(github.com/elastic/lunes)
Requires:       go(github.com/envoyproxy/go-control-plane/envoy)
Requires:       go(github.com/expr-lang/expr)
Requires:       go(github.com/facebook/time)
Requires:       go(github.com/fluent/fluent-logger-golang)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/getsentry/sentry-go)
Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(github.com/go-kit/log)
Requires:       go(github.com/go-ldap/ldap/v3)
Requires:       go(github.com/go-logfmt/logfmt)
Requires:       go(github.com/go-sql-driver/mysql)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/gobwas/glob)
Requires:       go(github.com/goccy/go-json)
Requires:       go(github.com/goccy/go-yaml)
Requires:       go(github.com/godbus/dbus/v5)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang-jwt/jwt/v5)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/snappy)
Requires:       go(github.com/google/cadvisor)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-github/v88)
Requires:       go(github.com/google/pprof)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/gorilla/mux)
Requires:       go(github.com/gosnmp/gosnmp)
Requires:       go(github.com/grafana/clusterurl)
Requires:       go(github.com/grafana/faro/pkg/go)
Requires:       go(github.com/grafana/loki/pkg/push)
Requires:       go(github.com/grafana/regexp)
Requires:       go(github.com/grobie/gomemcache)
Requires:       go(github.com/hashicorp/consul/api)
Requires:       go(github.com/hashicorp/go-hclog)
Requires:       go(github.com/hashicorp/go-version)
Requires:       go(github.com/hashicorp/golang-lru/v2)
Requires:       go(github.com/hetznercloud/hcloud-go/v2)
Requires:       go(github.com/huandu/go-clone)
Requires:       go(github.com/huaweicloud/huaweicloud-sdk-go-v3)
Requires:       go(github.com/iancoleman/strcase)
Requires:       go(github.com/influxdata/influxdb-observability/common)
Requires:       go(github.com/influxdata/influxdb-observability/influx2otel)
Requires:       go(github.com/influxdata/influxdb-observability/otel2influx)
Requires:       go(github.com/influxdata/line-protocol/v2)
Requires:       go(github.com/itchyny/timefmt-go)
Requires:       go(github.com/jackc/pgx/v5)
Requires:       go(github.com/jaegertracing/jaeger-idl)
Requires:       go(github.com/jaeyo/go-drain3)
Requires:       go(github.com/jcmturner/gokrb5/v8)
Requires:       go(github.com/jellydator/ttlcache/v3)
Requires:       go(github.com/jonboulle/clockwork)
Requires:       go(github.com/jpillora/backoff)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/julienschmidt/httprouter)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/knadh/koanf/maps)
Requires:       go(github.com/knadh/koanf/parsers/yaml)
Requires:       go(github.com/knadh/koanf/providers/rawbytes)
Requires:       go(github.com/knadh/koanf/v2)
Requires:       go(github.com/leodido/go-syslog/v4)
Requires:       go(github.com/lestrrat-go/strftime)
Requires:       go(github.com/lib/pq)
Requires:       go(github.com/lightstep/go-expohisto)
Requires:       go(github.com/linkedin/goavro/v2)
Requires:       go(github.com/linode/go-metadata)
Requires:       go(github.com/logicmonitor/lm-data-sdk-go)
Requires:       go(github.com/microsoft/ApplicationInsights-Go)
Requires:       go(github.com/microsoft/go-mssqldb)
Requires:       go(github.com/mitchellh/hashstructure/v2)
Requires:       go(github.com/moby/moby/api)
Requires:       go(github.com/moby/moby/client)
Requires:       go(github.com/modelcontextprotocol/go-sdk)
Requires:       go(github.com/mongodb-forks/digest)
Requires:       go(github.com/mwitkow/go-conntrack)
Requires:       go(github.com/netsampler/goflow2/v2)
Requires:       go(github.com/nginx/nginx-prometheus-exporter)
Requires:       go(github.com/oklog/ulid/v2)
Requires:       go(github.com/open-telemetry/opamp-go)
Requires:       go(github.com/open-telemetry/otel-arrow/go)
Requires:       go(github.com/opensearch-project/opensearch-go/v4)
Requires:       go(github.com/openshift/api)
Requires:       go(github.com/openshift/client-go)
Requires:       go(github.com/openzipkin/zipkin-go)
Requires:       go(github.com/orcaman/concurrent-map/v2)
Requires:       go(github.com/oschwald/geoip2-golang/v2)
Requires:       go(github.com/osquery/osquery-go)
Requires:       go(github.com/parquet-go/parquet-go)
Requires:       go(github.com/patrickmn/go-cache)
Requires:       go(github.com/pavlo-v-chernykh/keystore-go/v4)
Requires:       go(github.com/pavolloffay/opentelemetry-mcp-server/modules/collectorschema)
Requires:       go(github.com/pierrec/lz4)
Requires:       go(github.com/pkg/sftp)
Requires:       go(github.com/prometheus-community/pro-bing)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_golang/exp)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/exporter-toolkit)
Requires:       go(github.com/prometheus/otlptranslator)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/prometheus/prometheus)
Requires:       go(github.com/puzpuzpuz/xsync)
Requires:       go(github.com/puzpuzpuz/xsync/v4)
Requires:       go(github.com/rabbitmq/amqp091-go)
Requires:       go(github.com/rdforte/gomaxecs)
Requires:       go(github.com/redis/go-redis/v9)
Requires:       go(github.com/relvacode/iso8601)
Requires:       go(github.com/scaleway/scaleway-sdk-go)
Requires:       go(github.com/scalyr/dataset-go)
Requires:       go(github.com/shirou/gopsutil/v4)
Requires:       go(github.com/signalfx/com_signalfx_metrics_protobuf)
Requires:       go(github.com/sijms/go-ora/v2)
Requires:       go(github.com/snowflakedb/gosnowflake/v2)
Requires:       go(github.com/spf13/cast)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/splunk/stef/go/grpc)
Requires:       go(github.com/splunk/stef/go/otel)
Requires:       go(github.com/splunk/stef/go/pdata)
Requires:       go(github.com/splunk/stef/go/pkg)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common)
Requires:       go(github.com/testcontainers/testcontainers-go)
Requires:       go(github.com/tg123/go-htpasswd)
Requires:       go(github.com/thda/tds)
Requires:       go(github.com/tidwall/gjson)
Requires:       go(github.com/tidwall/wal)
Requires:       go(github.com/tilinna/clock)
Requires:       go(github.com/tinylib/msgp)
Requires:       go(github.com/traceloop/go-openllmetry/semconv-ai)
Requires:       go(github.com/twmb/franz-go)
Requires:       go(github.com/twmb/franz-go/pkg/kadm)
Requires:       go(github.com/twmb/franz-go/pkg/kfake)
Requires:       go(github.com/twmb/franz-go/pkg/kmsg)
Requires:       go(github.com/twmb/franz-go/pkg/sasl/kerberos)
Requires:       go(github.com/twmb/franz-go/plugin/kzap)
Requires:       go(github.com/twmb/murmur3)
Requires:       go(github.com/ua-parser/uap-go)
Requires:       go(github.com/valyala/fastjson)
Requires:       go(github.com/vmihailenco/msgpack/v5)
Requires:       go(github.com/vmware/go-vmware-nsxt)
Requires:       go(github.com/vmware/govmomi)
Requires:       go(github.com/wk8/go-ordered-map/v2)
Requires:       go(github.com/zeebo/xxh3)
Requires:       go(gitlab.com/gitlab-org/api/client-go/v2)
Requires:       go(go.etcd.io/bbolt)
Requires:       go(go.mongodb.org/atlas)
Requires:       go(go.mongodb.org/mongo-driver/v2)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/collector)
Requires:       go(go.opentelemetry.io/collector/client)
Requires:       go(go.opentelemetry.io/collector/component)
Requires:       go(go.opentelemetry.io/collector/component/componentstatus)
Requires:       go(go.opentelemetry.io/collector/component/componenttest)
Requires:       go(go.opentelemetry.io/collector/config/configauth)
Requires:       go(go.opentelemetry.io/collector/config/configcompression)
Requires:       go(go.opentelemetry.io/collector/config/configgrpc)
Requires:       go(go.opentelemetry.io/collector/config/confighttp)
Requires:       go(go.opentelemetry.io/collector/config/confignet)
Requires:       go(go.opentelemetry.io/collector/config/configopaque)
Requires:       go(go.opentelemetry.io/collector/config/configoptional)
Requires:       go(go.opentelemetry.io/collector/config/configretry)
Requires:       go(go.opentelemetry.io/collector/config/configtelemetry)
Requires:       go(go.opentelemetry.io/collector/config/configtls)
Requires:       go(go.opentelemetry.io/collector/confmap)
Requires:       go(go.opentelemetry.io/collector/confmap/provider/envprovider)
Requires:       go(go.opentelemetry.io/collector/confmap/provider/fileprovider)
Requires:       go(go.opentelemetry.io/collector/confmap/xconfmap)
Requires:       go(go.opentelemetry.io/collector/connector)
Requires:       go(go.opentelemetry.io/collector/connector/connectortest)
Requires:       go(go.opentelemetry.io/collector/connector/xconnector)
Requires:       go(go.opentelemetry.io/collector/consumer)
Requires:       go(go.opentelemetry.io/collector/consumer/consumererror)
Requires:       go(go.opentelemetry.io/collector/consumer/consumertest)
Requires:       go(go.opentelemetry.io/collector/consumer/xconsumer)
Requires:       go(go.opentelemetry.io/collector/exporter)
Requires:       go(go.opentelemetry.io/collector/exporter/debugexporter)
Requires:       go(go.opentelemetry.io/collector/exporter/exporterhelper)
Requires:       go(go.opentelemetry.io/collector/exporter/exporterhelper/xexporterhelper)
Requires:       go(go.opentelemetry.io/collector/exporter/exportertest)
Requires:       go(go.opentelemetry.io/collector/exporter/otlpexporter)
Requires:       go(go.opentelemetry.io/collector/exporter/otlphttpexporter)
Requires:       go(go.opentelemetry.io/collector/exporter/xexporter)
Requires:       go(go.opentelemetry.io/collector/extension)
Requires:       go(go.opentelemetry.io/collector/extension/extensionauth)
Requires:       go(go.opentelemetry.io/collector/extension/extensioncapabilities)
Requires:       go(go.opentelemetry.io/collector/extension/extensiontest)
Requires:       go(go.opentelemetry.io/collector/extension/xextension)
Requires:       go(go.opentelemetry.io/collector/extension/zpagesextension)
Requires:       go(go.opentelemetry.io/collector/featuregate)
Requires:       go(go.opentelemetry.io/collector/filter)
Requires:       go(go.opentelemetry.io/collector/otelcol)
Requires:       go(go.opentelemetry.io/collector/pdata)
Requires:       go(go.opentelemetry.io/collector/pdata/pprofile)
Requires:       go(go.opentelemetry.io/collector/pdata/xpdata)
Requires:       go(go.opentelemetry.io/collector/pipeline)
Requires:       go(go.opentelemetry.io/collector/pipeline/xpipeline)
Requires:       go(go.opentelemetry.io/collector/processor)
Requires:       go(go.opentelemetry.io/collector/processor/batchprocessor)
Requires:       go(go.opentelemetry.io/collector/processor/memorylimiterprocessor)
Requires:       go(go.opentelemetry.io/collector/processor/processorhelper)
Requires:       go(go.opentelemetry.io/collector/processor/processorhelper/xprocessorhelper)
Requires:       go(go.opentelemetry.io/collector/processor/processortest)
Requires:       go(go.opentelemetry.io/collector/processor/xprocessor)
Requires:       go(go.opentelemetry.io/collector/receiver)
Requires:       go(go.opentelemetry.io/collector/receiver/otlpreceiver)
Requires:       go(go.opentelemetry.io/collector/receiver/receiverhelper)
Requires:       go(go.opentelemetry.io/collector/receiver/receivertest)
Requires:       go(go.opentelemetry.io/collector/receiver/xreceiver)
Requires:       go(go.opentelemetry.io/collector/scraper)
Requires:       go(go.opentelemetry.io/collector/scraper/scraperhelper)
Requires:       go(go.opentelemetry.io/collector/scraper/scraperhelper/xscraperhelper)
Requires:       go(go.opentelemetry.io/collector/scraper/xscraper)
Requires:       go(go.opentelemetry.io/collector/semconv)
Requires:       go(go.opentelemetry.io/collector/service)
Requires:       go(go.opentelemetry.io/collector/service/hostcapabilities)
Requires:       go(go.opentelemetry.io/contrib/bridges/otelzap)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/contrib/otelconf)
Requires:       go(go.opentelemetry.io/ebpf-profiler)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploggrpc)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp)
Requires:       go(go.opentelemetry.io/otel/exporters/prometheus)
Requires:       go(go.opentelemetry.io/otel/log)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/schema)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/log)
Requires:       go(go.opentelemetry.io/otel/sdk/log/logtest)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.uber.org/automaxprocs)
Requires:       go(go.uber.org/mock)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(go.uber.org/zap/exp)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(golang.org/x/tools)
Requires:       go(gonum.org/v1/gonum)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/yaml.v3)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/client-go)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kubelet)
Requires:       go(k8s.io/utils)
Requires:       go(modernc.org/sqlite)
Requires:       go(sigs.k8s.io/controller-runtime)
Requires:       go(skywalking.apache.org/repo/goapi)
Requires:       go(software.sslmate.com/src/go-pkcs12)

%description
This package installs the Go source modules from one Collector contrib
repository snapshot, including receivers, exporters, processors, connectors,
extensions, and their shared libraries and tests.

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}"
cp -a ./. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/"

%check
%go_common
# Test the installed layout, including nested modules, without loading a
# second copy of the repository or using the system's older source package.
install -d "%{_builddir}/go/src"
cp -a "%{buildroot}%{go_sys_gopath}/." "%{_builddir}/go/src/"
_go_packages=$(go list -e -f '{{.ImportPath}}' github.com/open-telemetry/opentelemetry-collector-contrib/...)
_go_packages=$(printf '%s\n' "${_go_packages}" | sort -u)
_go_tests=
set -f
for _package in ${_go_packages}; do
    _skip=0
    for _exclude in %{?go_test_exclude}; do
        if [ "${_package}" = "${_exclude}" ]; then _skip=1; fi
    done
    for _exclude in %{?go_test_exclude_glob}; do
        case "${_package}" in ${_exclude}) _skip=1 ;; esac
    done
    if [ "${_skip}" -eq 1 ]; then
        # Excluded tests still compile against the packaged dependencies.
        go test %{go_test_flags_default} -run '^$' "${_package}"
    else
        _go_tests="${_go_tests} ${_package}"
    fi
done
set +f
test -n "${_go_tests}"
go test %{go_test_flags_default} ${_go_tests}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
