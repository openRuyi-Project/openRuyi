# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           grpc
%define go_import_path  google.golang.org/grpc

Name:           go-google-grpc
Version:        1.82.0~dev
Release:        %autorelease
Summary:        Go module dependency for Prometheus
License:        Apache-2.0
URL:            https://github.com/grpc/grpc-go
#!RemoteAsset:  sha256:907c7003d53833492a87c98c1dbb3daf8806c5ff84a28029383d23cde25bf7e5
Source0:        https://github.com/grpc/grpc-go/archive/v1.82.0-dev.tar.gz#/%{_name}-1.82.0-dev.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# advancedtls FileWatcherCRLProvider fails in OBS with Go/OpenSSL certificate
# chain validation reporting "no unrevoked chains found: map[2:1]".
Patch0:         2000-skip-advancedtls-filewatcher-crl-provider-test.patch

BuildOption(prep):  -n grpc-go-1.82.0-dev
# The upstream archive contains sibling Go modules. GOPATH-mode %gocheck would
# otherwise scan those module trees and pull in their separate Google Cloud,
# OpenCensus, and example dependency chains from the main grpc package.
# go-google-grpc and go-spiffe also mutually import each other's source packages;
# keep the runtime Requires on go-spiffe, but avoid a clean-project BuildRequires
# cycle and skip only grpc packages that directly need go-spiffe in %check.
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/cmd/protoc-gen-go-grpc*
    %{go_import_path}/credentials/tls/certprovider*
    %{go_import_path}/credentials/xds*
    %{go_import_path}/examples*
    %{go_import_path}/gcp/observability*
    %{go_import_path}/internal/credentials/spiffe*
    %{go_import_path}/internal/credentials/xds*
    %{go_import_path}/internal/xds/balancer/clusterimpl*
    %{go_import_path}/internal/xds/bootstrap*
    %{go_import_path}/internal/xds/server*
    %{go_import_path}/interop/observability*
    %{go_import_path}/interop/xds*
    %{go_import_path}/security/advancedtls*
    %{go_import_path}/stats/opencensus*
    %{go_import_path}/test/tools*
    %{go_import_path}/xds*
}

BuildRequires:  go
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/envoyproxy/go-control-plane)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/envoy)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/ratelimit)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/golang/glog)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/detectors/gcp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/oauth2/google)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(google.golang.org/grpc) = %{version}
Provides:       go(google.golang.org/grpc/admin) = %{version}
Provides:       go(google.golang.org/grpc/admin/test) = %{version}
Provides:       go(google.golang.org/grpc/attributes) = %{version}
Provides:       go(google.golang.org/grpc/authz) = %{version}
Provides:       go(google.golang.org/grpc/authz/audit) = %{version}
Provides:       go(google.golang.org/grpc/authz/audit/stdout) = %{version}
Provides:       go(google.golang.org/grpc/backoff) = %{version}
Provides:       go(google.golang.org/grpc/balancer) = %{version}
Provides:       go(google.golang.org/grpc/balancer/base) = %{version}
Provides:       go(google.golang.org/grpc/balancer/endpointsharding) = %{version}
Provides:       go(google.golang.org/grpc/balancer/grpclb) = %{version}
Provides:       go(google.golang.org/grpc/balancer/grpclb/grpc_lb_v1) = %{version}
Provides:       go(google.golang.org/grpc/balancer/grpclb/state) = %{version}
Provides:       go(google.golang.org/grpc/balancer/lazy) = %{version}
Provides:       go(google.golang.org/grpc/balancer/leastrequest) = %{version}
Provides:       go(google.golang.org/grpc/balancer/pickfirst) = %{version}
Provides:       go(google.golang.org/grpc/balancer/pickfirst/internal) = %{version}
Provides:       go(google.golang.org/grpc/balancer/pickfirst/pickfirstleaf) = %{version}
Provides:       go(google.golang.org/grpc/balancer/randomsubsetting) = %{version}
Provides:       go(google.golang.org/grpc/balancer/ringhash) = %{version}
Provides:       go(google.golang.org/grpc/balancer/rls) = %{version}
Provides:       go(google.golang.org/grpc/balancer/rls/internal/adaptive) = %{version}
Provides:       go(google.golang.org/grpc/balancer/rls/internal/keys) = %{version}
Provides:       go(google.golang.org/grpc/balancer/rls/internal/test/e2e) = %{version}
Provides:       go(google.golang.org/grpc/balancer/roundrobin) = %{version}
Provides:       go(google.golang.org/grpc/balancer/weightedroundrobin) = %{version}
Provides:       go(google.golang.org/grpc/balancer/weightedroundrobin/internal) = %{version}
Provides:       go(google.golang.org/grpc/balancer/weightedtarget) = %{version}
Provides:       go(google.golang.org/grpc/balancer/weightedtarget/weightedaggregator) = %{version}
Provides:       go(google.golang.org/grpc/benchmark) = %{version}
Provides:       go(google.golang.org/grpc/benchmark/flags) = %{version}
Provides:       go(google.golang.org/grpc/benchmark/latency) = %{version}
Provides:       go(google.golang.org/grpc/benchmark/primitives) = %{version}
Provides:       go(google.golang.org/grpc/benchmark/stats) = %{version}
Provides:       go(google.golang.org/grpc/binarylog) = %{version}
Provides:       go(google.golang.org/grpc/binarylog/grpc_binarylog_v1) = %{version}
Provides:       go(google.golang.org/grpc/channelz) = %{version}
Provides:       go(google.golang.org/grpc/channelz/grpc_channelz_v1) = %{version}
Provides:       go(google.golang.org/grpc/channelz/internal/protoconv) = %{version}
Provides:       go(google.golang.org/grpc/channelz/service) = %{version}
Provides:       go(google.golang.org/grpc/codes) = %{version}
Provides:       go(google.golang.org/grpc/connectivity) = %{version}
Provides:       go(google.golang.org/grpc/credentials) = %{version}
Provides:       go(google.golang.org/grpc/credentials/alts) = %{version}
Provides:       go(google.golang.org/grpc/credentials/alts/internal) = %{version}
Provides:       go(google.golang.org/grpc/credentials/alts/internal/authinfo) = %{version}
Provides:       go(google.golang.org/grpc/credentials/alts/internal/conn) = %{version}
Provides:       go(google.golang.org/grpc/credentials/alts/internal/handshaker) = %{version}
Provides:       go(google.golang.org/grpc/credentials/alts/internal/handshaker/service) = %{version}
Provides:       go(google.golang.org/grpc/credentials/alts/internal/proto/grpc_gcp) = %{version}
Provides:       go(google.golang.org/grpc/credentials/alts/internal/testutil) = %{version}
Provides:       go(google.golang.org/grpc/credentials/google) = %{version}
Provides:       go(google.golang.org/grpc/credentials/insecure) = %{version}
Provides:       go(google.golang.org/grpc/credentials/jwt) = %{version}
Provides:       go(google.golang.org/grpc/credentials/local) = %{version}
Provides:       go(google.golang.org/grpc/credentials/oauth) = %{version}
Provides:       go(google.golang.org/grpc/credentials/sts) = %{version}
Provides:       go(google.golang.org/grpc/credentials/tls/certprovider) = %{version}
Provides:       go(google.golang.org/grpc/credentials/tls/certprovider/pemfile) = %{version}
Provides:       go(google.golang.org/grpc/credentials/xds) = %{version}
Provides:       go(google.golang.org/grpc/encoding) = %{version}
Provides:       go(google.golang.org/grpc/encoding/gzip) = %{version}
Provides:       go(google.golang.org/grpc/encoding/internal) = %{version}
Provides:       go(google.golang.org/grpc/encoding/proto) = %{version}
Provides:       go(google.golang.org/grpc/examples/helloworld/helloworld) = %{version}
Provides:       go(google.golang.org/grpc/experimental) = %{version}
Provides:       go(google.golang.org/grpc/experimental/credentials) = %{version}
Provides:       go(google.golang.org/grpc/experimental/credentials/internal) = %{version}
Provides:       go(google.golang.org/grpc/experimental/opentelemetry) = %{version}
Provides:       go(google.golang.org/grpc/experimental/stats) = %{version}
Provides:       go(google.golang.org/grpc/grpclog) = %{version}
Provides:       go(google.golang.org/grpc/grpclog/glogger) = %{version}
Provides:       go(google.golang.org/grpc/grpclog/internal) = %{version}
Provides:       go(google.golang.org/grpc/health) = %{version}
Provides:       go(google.golang.org/grpc/health/grpc_health_v1) = %{version}
Provides:       go(google.golang.org/grpc/internal) = %{version}
Provides:       go(google.golang.org/grpc/internal/admin) = %{version}
Provides:       go(google.golang.org/grpc/internal/backoff) = %{version}
Provides:       go(google.golang.org/grpc/internal/balancer/gracefulswitch) = %{version}
Provides:       go(google.golang.org/grpc/internal/balancer/nop) = %{version}
Provides:       go(google.golang.org/grpc/internal/balancer/stub) = %{version}
Provides:       go(google.golang.org/grpc/internal/balancer/weight) = %{version}
Provides:       go(google.golang.org/grpc/internal/balancergroup) = %{version}
Provides:       go(google.golang.org/grpc/internal/balancerload) = %{version}
Provides:       go(google.golang.org/grpc/internal/binarylog) = %{version}
Provides:       go(google.golang.org/grpc/internal/buffer) = %{version}
Provides:       go(google.golang.org/grpc/internal/cache) = %{version}
Provides:       go(google.golang.org/grpc/internal/channelz) = %{version}
Provides:       go(google.golang.org/grpc/internal/credentials) = %{version}
Provides:       go(google.golang.org/grpc/internal/credentials/spiffe) = %{version}
Provides:       go(google.golang.org/grpc/internal/credentials/xds) = %{version}
Provides:       go(google.golang.org/grpc/internal/envconfig) = %{version}
Provides:       go(google.golang.org/grpc/internal/googlecloud) = %{version}
Provides:       go(google.golang.org/grpc/internal/grpclog) = %{version}
Provides:       go(google.golang.org/grpc/internal/grpcrand) = %{version}
Provides:       go(google.golang.org/grpc/internal/grpcsync) = %{version}
Provides:       go(google.golang.org/grpc/internal/grpctest) = %{version}
Provides:       go(google.golang.org/grpc/internal/grpcutil) = %{version}
Provides:       go(google.golang.org/grpc/internal/hierarchy) = %{version}
Provides:       go(google.golang.org/grpc/internal/idle) = %{version}
Provides:       go(google.golang.org/grpc/internal/leakcheck) = %{version}
Provides:       go(google.golang.org/grpc/internal/mem) = %{version}
Provides:       go(google.golang.org/grpc/internal/metadata) = %{version}
Provides:       go(google.golang.org/grpc/internal/pretty) = %{version}
Provides:       go(google.golang.org/grpc/internal/profiling) = %{version}
Provides:       go(google.golang.org/grpc/internal/profiling/buffer) = %{version}
Provides:       go(google.golang.org/grpc/internal/proto/grpc_lookup_v1) = %{version}
Provides:       go(google.golang.org/grpc/internal/proxyattributes) = %{version}
Provides:       go(google.golang.org/grpc/internal/resolver) = %{version}
Provides:       go(google.golang.org/grpc/internal/resolver/delegatingresolver) = %{version}
Provides:       go(google.golang.org/grpc/internal/resolver/dns) = %{version}
Provides:       go(google.golang.org/grpc/internal/resolver/dns/internal) = %{version}
Provides:       go(google.golang.org/grpc/internal/resolver/passthrough) = %{version}
Provides:       go(google.golang.org/grpc/internal/resolver/unix) = %{version}
Provides:       go(google.golang.org/grpc/internal/ringhash) = %{version}
Provides:       go(google.golang.org/grpc/internal/serviceconfig) = %{version}
Provides:       go(google.golang.org/grpc/internal/stats) = %{version}
Provides:       go(google.golang.org/grpc/internal/status) = %{version}
Provides:       go(google.golang.org/grpc/internal/stubserver) = %{version}
Provides:       go(google.golang.org/grpc/internal/syscall) = %{version}
Provides:       go(google.golang.org/grpc/internal/testutils) = %{version}
Provides:       go(google.golang.org/grpc/internal/testutils/fakegrpclb) = %{version}
Provides:       go(google.golang.org/grpc/internal/testutils/pickfirst) = %{version}
Provides:       go(google.golang.org/grpc/internal/testutils/proxyserver) = %{version}
Provides:       go(google.golang.org/grpc/internal/testutils/rls) = %{version}
Provides:       go(google.golang.org/grpc/internal/testutils/roundrobin) = %{version}
Provides:       go(google.golang.org/grpc/internal/testutils/stats) = %{version}
Provides:       go(google.golang.org/grpc/internal/testutils/xds/e2e) = %{version}
Provides:       go(google.golang.org/grpc/internal/testutils/xds/e2e/setup) = %{version}
Provides:       go(google.golang.org/grpc/internal/testutils/xds/fakeserver) = %{version}
Provides:       go(google.golang.org/grpc/internal/transport) = %{version}
Provides:       go(google.golang.org/grpc/internal/transport/networktype) = %{version}
Provides:       go(google.golang.org/grpc/internal/transport/readyreader) = %{version}
Provides:       go(google.golang.org/grpc/internal/wrr) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/cdsbalancer) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/cdsbalancer/e2e_test) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/clusterimpl) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/clusterimpl/internal) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/clusterimpl/tests) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/clustermanager) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/clustermanager/e2e_test) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/loadstore) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/outlierdetection) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/outlierdetection/e2e_test) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/priority) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/balancer/wrrlocality) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/bootstrap) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/bootstrap/jwtcreds) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/bootstrap/tlscreds) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/grpctransport) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/internal) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/internal/backoff) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/internal/buffer) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/internal/pretty) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/internal/syncutil) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/internal/testutils) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/internal/testutils/e2e) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/internal/testutils/fakeserver) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/internal/testutils/faketransport) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/lrsclient) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/lrsclient/internal) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/xdsclient) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/xdsclient/internal) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/xdsclient/internal/xdsresource) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/xdsclient/metrics) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clients/xdsclient/test) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clusterspecifier) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/clusterspecifier/rls) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/httpfilter) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/httpfilter/fault) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/httpfilter/rbac) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/httpfilter/router) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/matcher) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/rbac) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/resolver) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/resolver/internal) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/server) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/test/e2e) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/testutils) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/testutils/fakeclient) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/xdsclient) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/xdsclient/internal) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/xdsclient/pool) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/xdsclient/tests) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/xdsclient/tests/fallback) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/xdsclient/xdslbregistry) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/xdsclient/xdslbregistry/converter) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/xdsclient/xdsresource) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/xdsclient/xdsresource/tests) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/xdsclient/xdsresource/version) = %{version}
Provides:       go(google.golang.org/grpc/internal/xds/xdsdepmgr) = %{version}
Provides:       go(google.golang.org/grpc/interop) = %{version}
Provides:       go(google.golang.org/grpc/interop/grpc_testing) = %{version}
Provides:       go(google.golang.org/grpc/interop/grpc_testing/core) = %{version}
Provides:       go(google.golang.org/grpc/interop/stress/grpc_testing) = %{version}
Provides:       go(google.golang.org/grpc/keepalive) = %{version}
Provides:       go(google.golang.org/grpc/mem) = %{version}
Provides:       go(google.golang.org/grpc/metadata) = %{version}
Provides:       go(google.golang.org/grpc/orca) = %{version}
Provides:       go(google.golang.org/grpc/orca/internal) = %{version}
Provides:       go(google.golang.org/grpc/peer) = %{version}
Provides:       go(google.golang.org/grpc/profiling) = %{version}
Provides:       go(google.golang.org/grpc/profiling/proto) = %{version}
Provides:       go(google.golang.org/grpc/profiling/service) = %{version}
Provides:       go(google.golang.org/grpc/reflection) = %{version}
Provides:       go(google.golang.org/grpc/reflection/grpc_reflection_v1) = %{version}
Provides:       go(google.golang.org/grpc/reflection/grpc_reflection_v1alpha) = %{version}
Provides:       go(google.golang.org/grpc/reflection/grpc_testing) = %{version}
Provides:       go(google.golang.org/grpc/reflection/internal) = %{version}
Provides:       go(google.golang.org/grpc/reflection/test) = %{version}
Provides:       go(google.golang.org/grpc/resolver) = %{version}
Provides:       go(google.golang.org/grpc/resolver/dns) = %{version}
Provides:       go(google.golang.org/grpc/resolver/manual) = %{version}
Provides:       go(google.golang.org/grpc/resolver/passthrough) = %{version}
Provides:       go(google.golang.org/grpc/resolver/ringhash) = %{version}
Provides:       go(google.golang.org/grpc/serviceconfig) = %{version}
Provides:       go(google.golang.org/grpc/stats) = %{version}
Provides:       go(google.golang.org/grpc/stats/opentelemetry) = %{version}
Provides:       go(google.golang.org/grpc/stats/opentelemetry/csm) = %{version}
Provides:       go(google.golang.org/grpc/stats/opentelemetry/internal) = %{version}
Provides:       go(google.golang.org/grpc/stats/opentelemetry/internal/testutils) = %{version}
Provides:       go(google.golang.org/grpc/stats/opentelemetry/internal/tracing) = %{version}
Provides:       go(google.golang.org/grpc/status) = %{version}
Provides:       go(google.golang.org/grpc/tap) = %{version}
Provides:       go(google.golang.org/grpc/test) = %{version}
Provides:       go(google.golang.org/grpc/test/bufconn) = %{version}
Provides:       go(google.golang.org/grpc/test/codec_perf) = %{version}
Provides:       go(google.golang.org/grpc/test/xds) = %{version}
Provides:       go(google.golang.org/grpc/xds) = %{version}
Provides:       go(google.golang.org/grpc/xds/bootstrap) = %{version}
Provides:       go(google.golang.org/grpc/xds/csds) = %{version}
Provides:       go(google.golang.org/grpc/xds/googledirectpath) = %{version}
Provides:       go(google.golang.org/grpc/xds/test) = %{version}

Requires:       go(cel.dev/expr)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/cncf/xds/go)
Requires:       go(github.com/envoyproxy/go-control-plane)
Requires:       go(github.com/envoyproxy/go-control-plane/envoy)
Requires:       go(github.com/envoyproxy/go-control-plane/ratelimit)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/golang/glog)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
Requires:       go(github.com/spiffe/go-spiffe/v2)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib/detectors/gcp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/oauth2/google)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(gonum.org/v1/gonum)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/protobuf)

%description
Go module dependency for Prometheus. Generated by go2spec.

# stats/opencensus, security/advancedtls, and gcp/observability are nested Go
# modules packaged separately. Remove them from the main package to avoid file
# ownership conflicts while keeping the rest of grpc available.
%install -a
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/stats/opencensus \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/security/advancedtls \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/gcp/observability

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%license NOTICE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
