# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testcontainers-go
%define go_import_path  github.com/testcontainers/testcontainers-go
# Integration packages require a container runtime unavailable in OBS workers.
# The remaining patterns are independently versioned modules in this repository.
%define go_test_exclude_glob  %{shrink:
    %{go_import_path}
    %{go_import_path}/network
    %{go_import_path}/wait
    %{go_import_path}/examples*
    %{go_import_path}/modulegen*
    %{go_import_path}/modules*
    %{go_import_path}/usage-metrics*
    %{go_import_path}/wait/testdata/http*
}

Name:           go-github-testcontainers-testcontainers-go
Version:        0.44.0
Release:        %autorelease
Summary:        Container-based integration testing for Go
License:        MIT
URL:            https://github.com/testcontainers/testcontainers-go
#!RemoteAsset:  sha256:63824450478790f6fc5dc38fa6189093ba8bae8e493335d7929482dd213f3324
Source0:        https://github.com/testcontainers/testcontainers-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use the numeric mount type's correct formatting verb.
Patch2000:      2000-Fix-mount-type-format-verb.patch

BuildRequires:  go
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(cloud.google.com/go)
BuildRequires:  go(cloud.google.com/go/bigquery)
BuildRequires:  go(cloud.google.com/go/bigtable)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/datastore)
BuildRequires:  go(cloud.google.com/go/firestore)
BuildRequires:  go(cloud.google.com/go/iam)
BuildRequires:  go(cloud.google.com/go/longrunning)
BuildRequires:  go(cloud.google.com/go/pubsub)
BuildRequires:  go(cloud.google.com/go/spanner)
BuildRequires:  go(dario.cat/mergo)
BuildRequires:  go(github.com/99designs/go-keychain)
BuildRequires:  go(github.com/99designs/keyring)
BuildRequires:  go(github.com/AthenZ/athenz)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/data/azcosmos)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/data/aztables)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/internal)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/messaging/azeventhubs)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/messaging/azservicebus)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/azcertificates)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/azkeys)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/azsecrets)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/security/keyvault/internal)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/storage/azblob)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/storage/azqueue)
BuildRequires:  go(github.com/Azure/go-amqp)
BuildRequires:  go(github.com/Azure/go-ansiterm)
BuildRequires:  go(github.com/Azure/go-ntlmssp)
BuildRequires:  go(github.com/AzureAD/microsoft-authentication-library-for-go)
BuildRequires:  go(github.com/BraspagDevelopers/mock-server-client)
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/ClickHouse/ch-go)
BuildRequires:  go(github.com/ClickHouse/clickhouse-go/v2)
BuildRequires:  go(github.com/DataDog/zstd)
BuildRequires:  go(github.com/DefangLabs/secret-detector)
BuildRequires:  go(github.com/IBM/sarama)
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/Shopify/toxiproxy/v2)
BuildRequires:  go(github.com/acarl005/stripansi)
BuildRequires:  go(github.com/aerospike/aerospike-client-go/v8)
BuildRequires:  go(github.com/amikos-tech/chroma-go)
BuildRequires:  go(github.com/amikos-tech/pure-tokenizers)
BuildRequires:  go(github.com/andybalholm/brotli)
BuildRequires:  go(github.com/apache/arrow/go/v14)
BuildRequires:  go(github.com/apache/pulsar-client-go)
BuildRequires:  go(github.com/apache/thrift)
BuildRequires:  go(github.com/apapsch/go-jsonmerge/v2)
BuildRequires:  go(github.com/arangodb/go-driver/v2)
BuildRequires:  go(github.com/arangodb/go-velocypack)
BuildRequires:  go(github.com/ardielle/ardielle-go)
BuildRequires:  go(github.com/armon/go-metrics)
BuildRequires:  go(github.com/asaskevich/govalidator)
BuildRequires:  go(github.com/avast/retry-go)
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/aws/protocol/eventstream)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/config)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/credentials)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/configsources)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/ini)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/v4a)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/dynamodb)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/checksum)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/endpoint-discovery)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/s3shared)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/s3)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/signin)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sso)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sts)
BuildRequires:  go(github.com/aws/smithy-go)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/bits-and-blooms/bitset)
BuildRequires:  go(github.com/blang/semver/v4)
BuildRequires:  go(github.com/bradfitz/gomemcache)
BuildRequires:  go(github.com/buger/goterm)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cenkalti/backoff/v5)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cilium/ebpf)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/cockroachdb/errors)
BuildRequires:  go(github.com/cockroachdb/logtags)
BuildRequires:  go(github.com/cockroachdb/redact)
BuildRequires:  go(github.com/compose-spec/compose-go/v2)
BuildRequires:  go(github.com/containerd/cgroups/v3)
BuildRequires:  go(github.com/containerd/console)
BuildRequires:  go(github.com/containerd/containerd/api)
BuildRequires:  go(github.com/containerd/containerd/v2)
BuildRequires:  go(github.com/containerd/continuity)
BuildRequires:  go(github.com/containerd/errdefs)
BuildRequires:  go(github.com/containerd/errdefs/pkg)
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/containerd/platforms)
BuildRequires:  go(github.com/containerd/ttrpc)
BuildRequires:  go(github.com/containerd/typeurl/v2)
BuildRequires:  go(github.com/coreos/go-oidc/v3)
BuildRequires:  go(github.com/coreos/go-semver)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/couchbase/gocb/v2)
BuildRequires:  go(github.com/couchbase/gocbcore/v10)
BuildRequires:  go(github.com/couchbase/gocbcoreps)
BuildRequires:  go(github.com/couchbase/goprotostellar)
BuildRequires:  go(github.com/couchbaselabs/gocbconnstr/v2)
BuildRequires:  go(github.com/cpuguy83/dockercfg)
BuildRequires:  go(github.com/creasty/defaults)
BuildRequires:  go(github.com/danieljoos/wincred)
BuildRequires:  go(github.com/datafuselabs/databend-go)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/dchest/siphash)
BuildRequires:  go(github.com/dexidp/dex/api/v2)
BuildRequires:  go(github.com/dgryski/go-rendezvous)
BuildRequires:  go(github.com/distribution/reference)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/docker/buildx)
BuildRequires:  go(github.com/docker/cli)
BuildRequires:  go(github.com/docker/compose/v5)
BuildRequires:  go(github.com/docker/docker)
BuildRequires:  go(github.com/docker/docker-credential-helpers)
BuildRequires:  go(github.com/docker/go-connections)
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/dvsekhvalnov/jose2go)
BuildRequires:  go(github.com/eapache/go-resiliency)
BuildRequires:  go(github.com/eapache/go-xerial-snappy)
BuildRequires:  go(github.com/eapache/queue)
BuildRequires:  go(github.com/ebitengine/purego)
BuildRequires:  go(github.com/eiannone/keyboard)
BuildRequires:  go(github.com/elastic/elastic-transport-go/v8)
BuildRequires:  go(github.com/elastic/go-elasticsearch/v8)
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/envoy)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/form3tech-oss/jwt-go)
BuildRequires:  go(github.com/fsnotify/fsevents)
BuildRequires:  go(github.com/fvbommel/sortorder)
BuildRequires:  go(github.com/gabriel-vasile/mimetype)
BuildRequires:  go(github.com/getsentry/sentry-go)
BuildRequires:  go(github.com/go-asn1-ber/asn1-ber)
BuildRequires:  go(github.com/go-faster/city)
BuildRequires:  go(github.com/go-faster/errors)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-ldap/ldap/v3)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-ole/go-ole)
BuildRequires:  go(github.com/go-openapi/analysis)
BuildRequires:  go(github.com/go-openapi/errors)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/go-openapi/loads)
BuildRequires:  go(github.com/go-openapi/runtime)
BuildRequires:  go(github.com/go-openapi/spec)
BuildRequires:  go(github.com/go-openapi/strfmt)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/validate)
BuildRequires:  go(github.com/go-playground/locales)
BuildRequires:  go(github.com/go-playground/universal-translator)
BuildRequires:  go(github.com/go-playground/validator/v10)
BuildRequires:  go(github.com/go-redis/redis/v8)
BuildRequires:  go(github.com/go-resty/resty/v2)
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/go-stomp/stomp/v3)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/goccy/go-json)
BuildRequires:  go(github.com/gocql/gocql)
BuildRequires:  go(github.com/godbus/dbus)
BuildRequires:  go(github.com/godbus/dbus/v5)
BuildRequires:  go(github.com/gofrs/flock)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/golang-sql/civil)
BuildRequires:  go(github.com/golang-sql/sqlexp)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/google/btree)
BuildRequires:  go(github.com/google/flatbuffers)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/gofuzz)
BuildRequires:  go(github.com/google/jsonschema-go)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/shlex)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/gsterjov/go-libsecret)
BuildRequires:  go(github.com/hailocab/go-hostpool)
BuildRequires:  go(github.com/hamba/avro/v2)
BuildRequires:  go(github.com/hashicorp/consul/api)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)
BuildRequires:  go(github.com/hashicorp/go-rootcerts)
BuildRequires:  go(github.com/hashicorp/go-secure-stdlib/strutil)
BuildRequires:  go(github.com/hashicorp/go-uuid)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/hashicorp/golang-lru)
BuildRequires:  go(github.com/hashicorp/serf)
BuildRequires:  go(github.com/hashicorp/vault-client-go)
BuildRequires:  go(github.com/imdario/mergo)
BuildRequires:  go(github.com/in-toto/attestation)
BuildRequires:  go(github.com/in-toto/in-toto-golang)
BuildRequires:  go(github.com/inbucket/inbucket)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/influxdata/influxdb-client-go/v2)
BuildRequires:  go(github.com/influxdata/influxdb1-client)
BuildRequires:  go(github.com/influxdata/line-protocol)
BuildRequires:  go(github.com/inhies/go-bytesize)
BuildRequires:  go(github.com/jackc/pgpassfile)
BuildRequires:  go(github.com/jackc/pgservicefile)
BuildRequires:  go(github.com/jackc/pgx/v5)
BuildRequires:  go(github.com/jackc/puddle/v2)
BuildRequires:  go(github.com/jcmturner/aescts/v2)
BuildRequires:  go(github.com/jcmturner/dnsutils/v2)
BuildRequires:  go(github.com/jcmturner/gofork)
BuildRequires:  go(github.com/jcmturner/gokrb5/v8)
BuildRequires:  go(github.com/jcmturner/rpc/v2)
BuildRequires:  go(github.com/jhillyerd/inbucket)
BuildRequires:  go(github.com/jmespath/go-jmespath)
BuildRequires:  go(github.com/jolestar/go-commons-pool)
BuildRequires:  go(github.com/jonboulle/clockwork)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/kkdai/maglev)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/kylelemons/godebug)
BuildRequires:  go(github.com/leodido/go-urn)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/lufia/plan9stats)
BuildRequires:  go(github.com/magiconair/properties)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/mattn/go-shellwords)
BuildRequires:  go(github.com/matttproud/golang_protobuf_extensions)
BuildRequires:  go(github.com/mdelapenya/tlscert)
BuildRequires:  go(github.com/microsoft/go-mssqldb)
BuildRequires:  go(github.com/milvus-io/milvus-proto/go-api/v2)
BuildRequires:  go(github.com/milvus-io/milvus/client/v2)
BuildRequires:  go(github.com/milvus-io/milvus/pkg/v2)
BuildRequires:  go(github.com/minio/md5-simd)
BuildRequires:  go(github.com/minio/minio-go/v7)
BuildRequires:  go(github.com/minio/sha256-simd)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/hashstructure/v2)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/moby/buildkit)
BuildRequires:  go(github.com/moby/docker-image-spec)
BuildRequires:  go(github.com/moby/go-archive)
BuildRequires:  go(github.com/moby/locker)
BuildRequires:  go(github.com/moby/moby/api)
BuildRequires:  go(github.com/moby/moby/client)
BuildRequires:  go(github.com/moby/patternmatcher)
BuildRequires:  go(github.com/moby/sys/atomicwriter)
BuildRequires:  go(github.com/moby/sys/capability)
BuildRequires:  go(github.com/moby/sys/sequential)
BuildRequires:  go(github.com/moby/sys/signal)
BuildRequires:  go(github.com/moby/sys/symlink)
BuildRequires:  go(github.com/moby/sys/user)
BuildRequires:  go(github.com/moby/sys/userns)
BuildRequires:  go(github.com/moby/term)
BuildRequires:  go(github.com/modelcontextprotocol/go-sdk)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/morikuni/aec)
BuildRequires:  go(github.com/mtibben/percent)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/nats-io/nats.go)
BuildRequires:  go(github.com/nats-io/nkeys)
BuildRequires:  go(github.com/nats-io/nuid)
BuildRequires:  go(github.com/nebula-contrib/nebula-sirius)
BuildRequires:  go(github.com/neo4j/neo4j-go-driver/v5)
BuildRequires:  go(github.com/oapi-codegen/runtime)
BuildRequires:  go(github.com/oklog/ulid)
BuildRequires:  go(github.com/openai/openai-go)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/opencontainers/runtime-spec)
BuildRequires:  go(github.com/openfga/go-sdk)
BuildRequires:  go(github.com/opentracing/opentracing-go)
BuildRequires:  go(github.com/panjf2000/ants/v2)
BuildRequires:  go(github.com/paulmach/orb)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/pierrec/lz4)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pinecone-io/go-pinecone/v2)
BuildRequires:  go(github.com/pkg/browser)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pkoukk/tiktoken-go)
BuildRequires:  go(github.com/planetscale/vtprotobuf)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/power-devops/perfstat)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/qdrant/go-client)
BuildRequires:  go(github.com/rabbitmq/amqp091-go)
BuildRequires:  go(github.com/rcrowley/go-metrics)
BuildRequires:  go(github.com/redis/go-redis/v9)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/rs/xid)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/ryanuber/go-glob)
BuildRequires:  go(github.com/samber/lo)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(github.com/secure-systems-lab/go-securesystemslib)
BuildRequires:  go(github.com/segmentio/asm)
BuildRequires:  go(github.com/segmentio/encoding)
BuildRequires:  go(github.com/shibumi/go-pathspec)
BuildRequires:  go(github.com/shirou/gopsutil/v3)
BuildRequires:  go(github.com/shirou/gopsutil/v4)
BuildRequires:  go(github.com/shopspring/decimal)
BuildRequires:  go(github.com/sigstore/sigstore)
BuildRequires:  go(github.com/sigstore/sigstore-go)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/skratchdot/open-golang)
BuildRequires:  go(github.com/soheilhy/cmux)
BuildRequires:  go(github.com/spaolacci/murmur3)
BuildRequires:  go(github.com/spf13/cast)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/spiffe/go-spiffe/v2)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/surrealdb/surrealdb.go)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/match)
BuildRequires:  go(github.com/tidwall/pretty)
BuildRequires:  go(github.com/tidwall/sjson)
BuildRequires:  go(github.com/tilt-dev/fsnotify)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(github.com/tklauser/numcpus)
BuildRequires:  go(github.com/tmc/grpc-websocket-proxy)
BuildRequires:  go(github.com/tmc/langchaingo)
BuildRequires:  go(github.com/tonistiigi/dchapes-mode)
BuildRequires:  go(github.com/tonistiigi/fsutil)
BuildRequires:  go(github.com/tonistiigi/go-csvvalue)
BuildRequires:  go(github.com/tonistiigi/units)
BuildRequires:  go(github.com/tonistiigi/vt100)
BuildRequires:  go(github.com/twmb/franz-go)
BuildRequires:  go(github.com/twmb/franz-go/pkg/kadm)
BuildRequires:  go(github.com/twmb/franz-go/pkg/kmsg)
BuildRequires:  go(github.com/uber/jaeger-client-go)
BuildRequires:  go(github.com/valkey-io/valkey-go)
BuildRequires:  go(github.com/wadey/gocovmerge)
BuildRequires:  go(github.com/weaviate/weaviate)
BuildRequires:  go(github.com/weaviate/weaviate-go-client/v5)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(github.com/xdg-go/pbkdf2)
BuildRequires:  go(github.com/xdg-go/scram)
BuildRequires:  go(github.com/xdg-go/stringprep)
BuildRequires:  go(github.com/xhit/go-str2duration/v2)
BuildRequires:  go(github.com/xiang90/probing)
BuildRequires:  go(github.com/yalue/onnxruntime_go)
BuildRequires:  go(github.com/yosida95/uritemplate/v3)
BuildRequires:  go(github.com/youmark/pkcs8)
BuildRequires:  go(github.com/yugabyte/gocql)
BuildRequires:  go(github.com/yuin/gopher-lua)
BuildRequires:  go(github.com/yusufpapurcu/wmi)
BuildRequires:  go(github.com/zeebo/xxh3)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(go.etcd.io/etcd/api/v3)
BuildRequires:  go(go.etcd.io/etcd/client/pkg/v3)
BuildRequires:  go(go.etcd.io/etcd/client/v2)
BuildRequires:  go(go.etcd.io/etcd/client/v3)
BuildRequires:  go(go.etcd.io/etcd/pkg/v3)
BuildRequires:  go(go.etcd.io/etcd/raft/v3)
BuildRequires:  go(go.etcd.io/etcd/server/v3)
BuildRequires:  go(go.mongodb.org/mongo-driver)
BuildRequires:  go(go.mongodb.org/mongo-driver/v2)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib)
BuildRequires:  go(go.opentelemetry.io/contrib/bridges/otelslog)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/runtime)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/prometheus)
BuildRequires:  go(go.opentelemetry.io/otel/log)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/log)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.opentelemetry.io/proto/otlp)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/automaxprocs)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
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
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/ini.v1)
BuildRequires:  go(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(gotest.tools/v3)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/client-go)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v4)
BuildRequires:  go(sigs.k8s.io/yaml)
BuildRequires:  go(software.sslmate.com/src/go-pkcs12)
BuildRequires:  go(solace.dev/go/messaging)
BuildRequires:  go(tags.cncf.io/container-device-interface)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/testcontainers/testcontainers-go) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/examples/nginx) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/exec) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/internal) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/internal/config) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/internal/core) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/internal/core/bootstrap) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/internal/core/network) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/log) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/cmd) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/cmd/modules) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/internal) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/internal/context) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/internal/dependabot) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/internal/make) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/internal/mkdocs) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/internal/modfile) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/internal/module) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/internal/template) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/internal/tools) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modulegen/internal/vscode) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/activemq) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/aerospike) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/arangodb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/artemis) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/azure) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/azure/azurite) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/azure/cosmosdb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/azure/eventhubs) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/azure/lowkeyvault) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/azure/servicebus) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/azure/sqledge) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/azurite) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/cassandra) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/chroma) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/clickhouse) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/cockroachdb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/compose) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/consul) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/couchbase) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/couchdb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/cratedb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/databend) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/dex) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/dind) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/dockermcpgateway) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/dockermodelrunner) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/dockermodelrunner/internal/sdk/client) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/dockermodelrunner/internal/sdk/types) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/dolt) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/dynamodb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/elasticsearch) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/etcd) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/fakegcsserver) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/firebird) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/forgejo) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/gcloud) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/gcloud/bigquery) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/gcloud/bigtable) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/gcloud/datastore) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/gcloud/firestore) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/gcloud/internal/shared) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/gcloud/pubsub) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/gcloud/spanner) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/grafana-lgtm) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/inbucket) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/influxdb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/k3s) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/k6) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/kafka) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/kurrentdb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/localstack) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/mailpit) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/mariadb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/meilisearch) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/memcached) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/milvus) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/minio) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/mockserver) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/mongodb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/mongodb/atlaslocal) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/mosquitto) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/mssql) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/mysql) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/nats) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/nebulagraph) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/neo4j) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/nginx) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/ollama) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/openfga) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/openldap) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/opensearch) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/orientdb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/papercutsmtp) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/pinecone) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/postgres) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/presto) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/pulsar) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/qdrant) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/questdb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/rabbitmq) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/ravendb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/redis) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/redpanda) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/registry) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/s3mock) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/scylladb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/sftp) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/socat) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/solace) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/solr) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/surrealdb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/tidb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/timeplus) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/toxiproxy) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/trino) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/typesense) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/valkey) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/vault) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/vearch) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/weaviate) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/modules/yugabytedb) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/network) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/usage-metrics) = %{version}
Provides:       go(github.com/testcontainers/testcontainers-go/wait) = %{version}

Requires:       go(dario.cat/mergo)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/data/azcosmos)
Requires:       go(github.com/cenkalti/backoff/v4)
Requires:       go(github.com/compose-spec/compose-go/v2)
Requires:       go(github.com/containerd/errdefs)
Requires:       go(github.com/containerd/platforms)
Requires:       go(github.com/cpuguy83/dockercfg)
Requires:       go(github.com/dexidp/dex/api/v2)
Requires:       go(github.com/docker/cli)
Requires:       go(github.com/docker/compose/v5)
Requires:       go(github.com/docker/go-units)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/jackc/pgx/v5)
Requires:       go(github.com/magiconair/properties)
Requires:       go(github.com/mdelapenya/tlscert)
Requires:       go(github.com/moby/go-archive)
Requires:       go(github.com/moby/moby/api)
Requires:       go(github.com/moby/moby/client)
Requires:       go(github.com/moby/patternmatcher)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(github.com/shirou/gopsutil/v4)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/tidwall/gjson)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/grpc)
Requires:       go(gopkg.in/yaml.v3)
Requires:       go(software.sslmate.com/src/go-pkcs12)

%description
Testcontainers for Go creates and manages disposable containers for integration
tests through Docker-compatible container runtimes.

%install
# All published modules use this repository's root import prefix, so the
# standard macro preserves the complete source tree and nested go.mod files.
%buildsystem_golangmodules_install

%check
# Timer tests require synchronous timer channels in GOPATH mode.
export GODEBUG=asynctimerchan=0
%go_common
install -d "%{_builddir}/go/src"
cp -a "%{buildroot}%{go_sys_gopath}/." "%{_builddir}/go/src/"
_module_files=$(find . -name go.mod -not -path './.git/*' -not -path '*/testdata/*' | sort)
_test_module() {
    _module_import=$1
    _go_packages=$(go list -e -f '{{.ImportPath}}' ./...)
    _go_tests=
    set -f
    for _package in ${_go_packages}; do
        _skip=0
        for _exclude in %{?go_test_exclude}; do
            [ "${_package}" = "${_exclude}" ] && _skip=1
        done
        for _exclude in %{?go_test_exclude_glob}; do
            case "${_package}" in ${_exclude}) _skip=1 ;; esac
        done
        [ "${_skip}" -eq 0 ] && _go_tests="${_go_tests} ${_package}"
    done
    set +f
    [ -z "${_go_tests}" ] || go test %{go_test_flags_default} ${_go_tests}
}
while read -r _modfile; do
    _source=${_modfile%/go.mod}
    _import=$(awk '$1 == "module" {gsub(/"/, "", $2); print $2; exit}' "${_modfile}")
    case "${_import}" in
        %{go_import_path}|%{go_import_path}/*) ;;
        *) continue ;;
    esac
    pushd "%{_builddir}/go/src/${_import}"
    _test_module "${_import}"
    popd
done <<EOF
${_module_files}
EOF

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
