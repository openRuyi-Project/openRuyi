# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           prometheus
%define go_import_path  github.com/prometheus/prometheus

Name:           go-github-prometheus-prometheus
Version:        0.311.3
Release:        %autorelease
Summary:        Prometheus monitoring system
License:        Apache-2.0
URL:            https://github.com/prometheus/prometheus
#!RemoteAsset:  sha256:5a61d9b1ce2cf2caf5606fedd0d9c46237740f87d74d2e1ff7115967af353046
Source0:        https://github.com/prometheus/prometheus/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n prometheus-0.311.3

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/alecthomas/kingpin/v2)
BuildRequires:  go(github.com/alecthomas/units)
BuildRequires:  go(github.com/apapsch/go-jsonmerge/v2)
BuildRequires:  go(github.com/armon/go-metrics)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/config)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/credentials)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/configsources)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/ini)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ec2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ecs)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/elasticache)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/kafka)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/lightsail)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/rds)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/signin)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sso)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sts)
BuildRequires:  go(github.com/aws/smithy-go)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/internal)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/compute/armcompute/v5)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/network/armnetwork/v4)
BuildRequires:  go(github.com/AzureAD/microsoft-authentication-library-for-go)
BuildRequires:  go(github.com/bahlo/generic-list-go)
BuildRequires:  go(github.com/basgys/goxml2json)
BuildRequires:  go(github.com/bboreham/go-loser)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/buger/jsonparser)
BuildRequires:  go(github.com/cenkalti/backoff/v5)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/Code-Hex/go-generics-cache)
BuildRequires:  go(github.com/containerd/errdefs)
BuildRequires:  go(github.com/containerd/errdefs/pkg)
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/dennwc/varint)
BuildRequires:  go(github.com/digitalocean/godo)
BuildRequires:  go(github.com/distribution/reference)
BuildRequires:  go(github.com/docker/docker)
BuildRequires:  go(github.com/docker/go-connections)
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/edsrzf/mmap-go)
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/envoy)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/facette/natsort)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/felixge/fgprof)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
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
BuildRequires:  go(github.com/go-resty/resty/v2)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/go-zookeeper/zk)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/gophercloud/gophercloud/v2)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/grafana/regexp)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/hashicorp/consul/api)
BuildRequires:  go(github.com/hashicorp/cronexpr)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/hashicorp/go-cleanhttp)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-immutable-radix)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/hashicorp/go-retryablehttp)
BuildRequires:  go(github.com/hashicorp/go-rootcerts)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/hashicorp/golang-lru)
BuildRequires:  go(github.com/hashicorp/nomad/api)
BuildRequires:  go(github.com/hashicorp/serf)
BuildRequires:  go(github.com/hetznercloud/hcloud-go/v2)
BuildRequires:  go(github.com/influxdata/influxdb-client-go/v2)
BuildRequires:  go(github.com/influxdata/line-protocol)
BuildRequires:  go(github.com/ionos-cloud/sdk-go/v6)
BuildRequires:  go(github.com/jpillora/backoff)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/julienschmidt/httprouter)
BuildRequires:  go(github.com/KimMachineGun/automemlimit)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/knadh/koanf/providers/confmap)
BuildRequires:  go(github.com/knadh/koanf/v2)
BuildRequires:  go(github.com/kolo/xmlrpc)
BuildRequires:  go(github.com/kylelemons/godebug)
BuildRequires:  go(github.com/linode/linodego)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mdlayher/socket)
BuildRequires:  go(github.com/mdlayher/vsock)
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go(github.com/moby/docker-image-spec)
BuildRequires:  go(github.com/moby/sys/atomicwriter)
BuildRequires:  go(github.com/moby/term)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/morikuni/aec)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/mwitkow/go-conntrack)
BuildRequires:  go(github.com/nsf/jsondiff)
BuildRequires:  go(github.com/oapi-codegen/runtime)
BuildRequires:  go(github.com/oklog/run)
BuildRequires:  go(github.com/oklog/ulid/v2)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/exp/metrics)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatautil)
BuildRequires:  go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/ovh/go-ovh)
BuildRequires:  go(github.com/pb33f/jsonpath)
BuildRequires:  go(github.com/pb33f/libopenapi)
BuildRequires:  go(github.com/pb33f/libopenapi-validator)
BuildRequires:  go(github.com/pb33f/ordered-map/v2)
BuildRequires:  go(github.com/pbnjay/memory)
BuildRequires:  go(github.com/pkg/browser)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/planetscale/vtprotobuf)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prometheus/alertmanager)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_golang/exp)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/common/assets)
BuildRequires:  go(github.com/prometheus/exporter-toolkit)
BuildRequires:  go(github.com/prometheus/otlptranslator)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/prometheus/sigv4)
BuildRequires:  go(github.com/puzpuzpuz/xsync/v4)
BuildRequires:  go(github.com/russross/blackfriday/v2)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(github.com/scaleway/scaleway-sdk-go)
BuildRequires:  go(github.com/shurcooL/httpfs)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stackitcloud/stackit-sdk-go/core)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/vultr/govultr/v3)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(github.com/xhit/go-str2duration/v2)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/collector/component)
BuildRequires:  go(go.opentelemetry.io/collector/confmap)
BuildRequires:  go(go.opentelemetry.io/collector/confmap/xconfmap)
BuildRequires:  go(go.opentelemetry.io/collector/consumer)
BuildRequires:  go(go.opentelemetry.io/collector/featuregate)
BuildRequires:  go(go.opentelemetry.io/collector/internal/componentalias)
BuildRequires:  go(go.opentelemetry.io/collector/pdata)
BuildRequires:  go(go.opentelemetry.io/collector/pipeline)
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
BuildRequires:  go(go.opentelemetry.io/proto/otlp)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/automaxprocs)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/evanphx/json-patch.v4)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/ini.v1)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(gotest.tools/v3)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/client-go)
BuildRequires:  go(k8s.io/klog)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/prometheus/prometheus) = %{version}
Provides:       go(github.com/prometheus/prometheus/config) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/aws) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/azure) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/consul) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/digitalocean) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/dns) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/eureka) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/file) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/gce) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/hetzner) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/http) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/install) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/ionos) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/kubernetes) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/linode) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/marathon) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/moby) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/nomad) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/openstack) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/ovhcloud) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/puppetdb) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/refresh) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/scaleway) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/stackit) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/targetgroup) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/triton) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/uyuni) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/vultr) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/xds) = %{version}
Provides:       go(github.com/prometheus/prometheus/discovery/zookeeper) = %{version}
Provides:       go(github.com/prometheus/prometheus/model/exemplar) = %{version}
Provides:       go(github.com/prometheus/prometheus/model/histogram) = %{version}
Provides:       go(github.com/prometheus/prometheus/model/labels) = %{version}
Provides:       go(github.com/prometheus/prometheus/model/metadata) = %{version}
Provides:       go(github.com/prometheus/prometheus/model/relabel) = %{version}
Provides:       go(github.com/prometheus/prometheus/model/rulefmt) = %{version}
Provides:       go(github.com/prometheus/prometheus/model/textparse) = %{version}
Provides:       go(github.com/prometheus/prometheus/model/timestamp) = %{version}
Provides:       go(github.com/prometheus/prometheus/model/value) = %{version}
Provides:       go(github.com/prometheus/prometheus/notifier) = %{version}
Provides:       go(github.com/prometheus/prometheus/plugins) = %{version}
Provides:       go(github.com/prometheus/prometheus/prompb) = %{version}
Provides:       go(github.com/prometheus/prometheus/prompb/io/prometheus/client) = %{version}
Provides:       go(github.com/prometheus/prometheus/prompb/io/prometheus/write/v2) = %{version}
Provides:       go(github.com/prometheus/prometheus/prompb/rwcommon) = %{version}
Provides:       go(github.com/prometheus/prometheus/promql) = %{version}
Provides:       go(github.com/prometheus/prometheus/promql/parser) = %{version}
Provides:       go(github.com/prometheus/prometheus/promql/parser/posrange) = %{version}
Provides:       go(github.com/prometheus/prometheus/promql/promqltest) = %{version}
Provides:       go(github.com/prometheus/prometheus/rules) = %{version}
Provides:       go(github.com/prometheus/prometheus/schema) = %{version}
Provides:       go(github.com/prometheus/prometheus/scrape) = %{version}
Provides:       go(github.com/prometheus/prometheus/storage) = %{version}
Provides:       go(github.com/prometheus/prometheus/storage/remote) = %{version}
Provides:       go(github.com/prometheus/prometheus/storage/remote/azuread) = %{version}
Provides:       go(github.com/prometheus/prometheus/storage/remote/googleiam) = %{version}
Provides:       go(github.com/prometheus/prometheus/storage/remote/otlptranslator/prometheusremotewrite) = %{version}
Provides:       go(github.com/prometheus/prometheus/template) = %{version}
Provides:       go(github.com/prometheus/prometheus/tracing) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/agent) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/chunkenc) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/chunks) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/compression) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/encoding) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/fileutil) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/goversion) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/index) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/record) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/tombstones) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/tsdbutil) = %{version}
Provides:       go(github.com/prometheus/prometheus/tsdb/wlog) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/almost) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/annotations) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/compression) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/convertnhcb) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/documentcli) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/features) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/fmtutil) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/fuzzing) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/gate) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/httputil) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/jsonutil) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/junitxml) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/kahansum) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/logging) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/namevalidationutil) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/netconnlimit) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/notifications) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/osutil) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/pool) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/runtime) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/runutil) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/stats) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/strutil) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/testrecord) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/teststorage) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/testutil) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/testutil/synctest) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/testwal) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/treecache) = %{version}
Provides:       go(github.com/prometheus/prometheus/util/zeropool) = %{version}
Provides:       go(github.com/prometheus/prometheus/web) = %{version}
Provides:       go(github.com/prometheus/prometheus/web/api/testhelpers) = %{version}
Provides:       go(github.com/prometheus/prometheus/web/api/v1) = %{version}
Provides:       go(github.com/prometheus/prometheus/web/ui) = %{version}

Requires:       go(cloud.google.com/go/auth)
Requires:       go(cloud.google.com/go/auth/oauth2adapt)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(github.com/alecthomas/kingpin/v2)
Requires:       go(github.com/alecthomas/units)
Requires:       go(github.com/apapsch/go-jsonmerge/v2)
Requires:       go(github.com/armon/go-metrics)
Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/config)
Requires:       go(github.com/aws/aws-sdk-go-v2/credentials)
Requires:       go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/configsources)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/ini)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ec2)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ecs)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/elasticache)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/kafka)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/lightsail)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/rds)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/signin)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sso)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sts)
Requires:       go(github.com/aws/smithy-go)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/internal)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/compute/armcompute/v5)
Requires:       go(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/network/armnetwork/v4)
Requires:       go(github.com/AzureAD/microsoft-authentication-library-for-go)
Requires:       go(github.com/bahlo/generic-list-go)
Requires:       go(github.com/basgys/goxml2json)
Requires:       go(github.com/bboreham/go-loser)
Requires:       go(github.com/beorn7/perks)
Requires:       go(github.com/buger/jsonparser)
Requires:       go(github.com/cenkalti/backoff/v5)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/cncf/xds/go)
Requires:       go(github.com/Code-Hex/go-generics-cache)
Requires:       go(github.com/containerd/errdefs)
Requires:       go(github.com/containerd/errdefs/pkg)
Requires:       go(github.com/containerd/log)
Requires:       go(github.com/coreos/go-systemd/v22)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/dennwc/varint)
Requires:       go(github.com/digitalocean/godo)
Requires:       go(github.com/distribution/reference)
Requires:       go(github.com/docker/docker)
Requires:       go(github.com/docker/go-connections)
Requires:       go(github.com/docker/go-units)
Requires:       go(github.com/edsrzf/mmap-go)
Requires:       go(github.com/emicklei/go-restful/v3)
Requires:       go(github.com/envoyproxy/go-control-plane/envoy)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(github.com/facette/natsort)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/felixge/fgprof)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/fxamacker/cbor/v2)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/go-openapi/analysis)
Requires:       go(github.com/go-openapi/errors)
Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/go-openapi/jsonreference)
Requires:       go(github.com/go-openapi/loads)
Requires:       go(github.com/go-openapi/spec)
Requires:       go(github.com/go-openapi/strfmt)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/go-openapi/swag/cmdutils)
Requires:       go(github.com/go-openapi/swag/conv)
Requires:       go(github.com/go-openapi/swag/fileutils)
Requires:       go(github.com/go-openapi/swag/jsonname)
Requires:       go(github.com/go-openapi/swag/jsonutils)
Requires:       go(github.com/go-openapi/swag/loading)
Requires:       go(github.com/go-openapi/swag/mangling)
Requires:       go(github.com/go-openapi/swag/netutils)
Requires:       go(github.com/go-openapi/swag/stringutils)
Requires:       go(github.com/go-openapi/swag/typeutils)
Requires:       go(github.com/go-openapi/swag/yamlutils)
Requires:       go(github.com/go-openapi/validate)
Requires:       go(github.com/go-resty/resty/v2)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/go-zookeeper/zk)
Requires:       go(github.com/gobwas/glob)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang-jwt/jwt/v5)
Requires:       go(github.com/golang/snappy)
Requires:       go(github.com/google/gnostic-models)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-querystring)
Requires:       go(github.com/google/pprof)
Requires:       go(github.com/google/s2a-go)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/gophercloud/gophercloud/v2)
Requires:       go(github.com/gorilla/websocket)
Requires:       go(github.com/grafana/regexp)
Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(github.com/hashicorp/consul/api)
Requires:       go(github.com/hashicorp/cronexpr)
Requires:       go(github.com/hashicorp/errwrap)
Requires:       go(github.com/hashicorp/go-cleanhttp)
Requires:       go(github.com/hashicorp/go-hclog)
Requires:       go(github.com/hashicorp/go-immutable-radix)
Requires:       go(github.com/hashicorp/go-multierror)
Requires:       go(github.com/hashicorp/go-retryablehttp)
Requires:       go(github.com/hashicorp/go-rootcerts)
Requires:       go(github.com/hashicorp/go-version)
Requires:       go(github.com/hashicorp/golang-lru)
Requires:       go(github.com/hashicorp/nomad/api)
Requires:       go(github.com/hashicorp/serf)
Requires:       go(github.com/hetznercloud/hcloud-go/v2)
Requires:       go(github.com/influxdata/influxdb-client-go/v2)
Requires:       go(github.com/influxdata/line-protocol)
Requires:       go(github.com/ionos-cloud/sdk-go/v6)
Requires:       go(github.com/jpillora/backoff)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/julienschmidt/httprouter)
Requires:       go(github.com/KimMachineGun/automemlimit)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/knadh/koanf/maps)
Requires:       go(github.com/knadh/koanf/providers/confmap)
Requires:       go(github.com/knadh/koanf/v2)
Requires:       go(github.com/kolo/xmlrpc)
Requires:       go(github.com/kylelemons/godebug)
Requires:       go(github.com/linode/linodego)
Requires:       go(github.com/mattn/go-colorable)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/mdlayher/socket)
Requires:       go(github.com/mdlayher/vsock)
Requires:       go(github.com/Microsoft/go-winio)
Requires:       go(github.com/miekg/dns)
Requires:       go(github.com/mitchellh/copystructure)
Requires:       go(github.com/mitchellh/go-homedir)
Requires:       go(github.com/mitchellh/mapstructure)
Requires:       go(github.com/mitchellh/reflectwalk)
Requires:       go(github.com/moby/docker-image-spec)
Requires:       go(github.com/moby/sys/atomicwriter)
Requires:       go(github.com/moby/term)
Requires:       go(github.com/modern-go/concurrent)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(github.com/morikuni/aec)
Requires:       go(github.com/munnerz/goautoneg)
Requires:       go(github.com/mwitkow/go-conntrack)
Requires:       go(github.com/nsf/jsondiff)
Requires:       go(github.com/oapi-codegen/runtime)
Requires:       go(github.com/oklog/run)
Requires:       go(github.com/oklog/ulid/v2)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/internal/exp/metrics)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/pkg/pdatautil)
Requires:       go(github.com/open-telemetry/opentelemetry-collector-contrib/processor/deltatocumulativeprocessor)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(github.com/ovh/go-ovh)
Requires:       go(github.com/pb33f/jsonpath)
Requires:       go(github.com/pb33f/libopenapi)
Requires:       go(github.com/pb33f/libopenapi-validator)
Requires:       go(github.com/pb33f/ordered-map/v2)
Requires:       go(github.com/pbnjay/memory)
Requires:       go(github.com/pkg/browser)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/planetscale/vtprotobuf)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/prometheus/alertmanager)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_golang/exp)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/common/assets)
Requires:       go(github.com/prometheus/exporter-toolkit)
Requires:       go(github.com/prometheus/otlptranslator)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/prometheus/sigv4)
Requires:       go(github.com/puzpuzpuz/xsync/v4)
Requires:       go(github.com/russross/blackfriday/v2)
Requires:       go(github.com/santhosh-tekuri/jsonschema/v6)
Requires:       go(github.com/scaleway/scaleway-sdk-go)
Requires:       go(github.com/shurcooL/httpfs)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/stackitcloud/stackit-sdk-go/core)
Requires:       go(github.com/stretchr/objx)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/vultr/govultr/v3)
Requires:       go(github.com/x448/float16)
Requires:       go(github.com/xhit/go-str2duration/v2)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/collector/component)
Requires:       go(go.opentelemetry.io/collector/confmap)
Requires:       go(go.opentelemetry.io/collector/confmap/xconfmap)
Requires:       go(go.opentelemetry.io/collector/consumer)
Requires:       go(go.opentelemetry.io/collector/featuregate)
Requires:       go(go.opentelemetry.io/collector/internal/componentalias)
Requires:       go(go.opentelemetry.io/collector/pdata)
Requires:       go(go.opentelemetry.io/collector/pipeline)
Requires:       go(go.opentelemetry.io/collector/processor)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
Requires:       go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.opentelemetry.io/proto/otlp)
Requires:       go(go.uber.org/atomic)
Requires:       go(go.uber.org/automaxprocs)
Requires:       go(go.uber.org/goleak)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(go.yaml.in/yaml/v4)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(golang.org/x/tools)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/evanphx/json-patch.v4)
Requires:       go(gopkg.in/inf.v0)
Requires:       go(gopkg.in/ini.v1)
Requires:       go(gopkg.in/yaml.v2)
Requires:       go(gopkg.in/yaml.v3)
Requires:       go(gotest.tools/v3)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/client-go)
Requires:       go(k8s.io/klog)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kube-openapi)
Requires:       go(k8s.io/utils)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)
Requires:       go(sigs.k8s.io/yaml)

%description
This package provides Prometheus monitoring system.

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%license NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
