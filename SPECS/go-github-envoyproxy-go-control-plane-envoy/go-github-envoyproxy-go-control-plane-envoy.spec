# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           envoy
%define go_import_path  github.com/envoyproxy/go-control-plane

Name:           go-github-envoyproxy-go-control-plane-envoy
Version:        1.37.0
Release:        %autorelease
Summary:        Envoy API Go module from go-control-plane
License:        Apache-2.0
URL:            https://github.com/envoyproxy/go-control-plane
#!RemoteAsset:  sha256:311e84ca6659b8eb0a88bf7193579196a543305736ce8a0e12dc450a8faa1139
Source0:        https://github.com/envoyproxy/go-control-plane/archive/refs/tags/envoy/v1.37.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-control-plane-envoy-v1.37.0
# The archive is tagged for the envoy module, but the generated packages live
# under envoy/ while the module path remains github.com/envoyproxy/go-control-plane.
# Keep %check scoped to that subtree so the installed import paths match Provides.
%define go_test_include %{go_import_path}/envoy/...

BuildRequires:  go
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/envoyproxy/go-control-plane)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/planetscale/vtprotobuf)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(go.opentelemetry.io/proto/otlp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/envoyproxy/go-control-plane/envoy) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/admin/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/admin/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/annotations) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/api/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/api/v2/auth) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/api/v2/cluster) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/api/v2/core) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/api/v2/endpoint) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/api/v2/listener) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/api/v2/ratelimit) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/api/v2/route) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/accesslog/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/accesslog/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/bootstrap/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/bootstrap/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/cluster/aggregate/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/cluster/dynamic_forward_proxy/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/cluster/redis) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/cluster/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/common/dynamic_forward_proxy/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/common/key_value/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/common/matcher/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/common/mutation_rules/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/common/tap/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/core/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/endpoint/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/accesslog/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/dubbo/router/v2alpha1) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/fault/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/adaptive_concurrency/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/aws_lambda/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/aws_request_signing/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/buffer/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/cache/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/compressor/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/cors/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/csrf/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/dynamic_forward_proxy/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/dynamo/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/ext_authz/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/fault/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/grpc_http1_bridge/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/grpc_http1_reverse_bridge/v2alpha1) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/grpc_stats/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/grpc_web/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/gzip/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/header_to_metadata/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/health_check/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/ip_tagging/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/jwt_authn/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/lua/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/on_demand/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/original_src/v2alpha1) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/rate_limit/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/rbac/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/router/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/squash/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/tap/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/http/transcoder/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/listener/http_inspector/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/listener/original_dst/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/listener/original_src/v2alpha1) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/listener/proxy_protocol/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/listener/tls_inspector/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/client_ssl_auth/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/direct_response/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/dubbo_proxy/v2alpha1) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/echo/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/ext_authz/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/http_connection_manager/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/kafka_broker/v2alpha1) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/local_rate_limit/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/mongo_proxy/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/mysql_proxy/v1alpha1) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/rate_limit/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/rbac/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/redis_proxy/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/sni_cluster/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/tcp_proxy/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/thrift_proxy/v2alpha1) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/network/zookeeper_proxy/v1alpha1) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/thrift/rate_limit/v2alpha1) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/thrift/router/v2alpha1) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/filter/udp/udp_proxy/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/grpc_credential/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/grpc_credential/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/health_checker/redis/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/listener/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/listener/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/metrics/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/metrics/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/overload/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/overload/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/ratelimit/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/ratelimit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/rbac/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/rbac/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/resource_monitor/fixed_heap/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/resource_monitor/injected_resource/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/retry/omit_canary_hosts/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/retry/omit_host_metadata/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/retry/previous_hosts/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/retry/previous_priorities) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/route/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/tap/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/trace/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/trace/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/trace/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/transport_socket/alts/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/transport_socket/raw_buffer/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/transport_socket/tap/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/config/upstream/local_address_selector/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/data/accesslog/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/data/accesslog/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/data/cluster/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/data/cluster/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/data/core/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/data/core/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/data/dns/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/data/dns/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/data/tap/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/data/tap/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/dynamic_modules/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/file/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/filters/cel/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/filters/process_ratelimit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/fluentd/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/grpc/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/open_telemetry/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/stats/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/stream/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/wasm/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/bootstrap/dynamic_modules/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/bootstrap/internal_listener/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/bootstrap/reverse_tunnel/downstream_socket_interface/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/bootstrap/reverse_tunnel/upstream_socket_interface/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/clusters/aggregate/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/clusters/common/dns/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/clusters/composite/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/clusters/dns/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/clusters/dynamic_forward_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/clusters/redis/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/clusters/reverse_connection/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/common/async_files/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/common/aws/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/common/dynamic_forward_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/common/matching/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/common/ratelimit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/common/tap/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/compression/brotli/compressor/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/compression/brotli/decompressor/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/compression/gzip/compressor/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/compression/gzip/decompressor/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/compression/zstd/compressor/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/compression/zstd/decompressor/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/config/validators/minimum_clusters/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/dynamic_modules/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/early_data/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/common/dependency/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/common/fault/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/common/matcher/action/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/common/set_filter_state/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/adaptive_concurrency/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/admission_control/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/alternate_protocols_cache/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/api_key_auth/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/aws_lambda/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/aws_request_signing/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/bandwidth_limit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/basic_auth/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/buffer/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/cache/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/cache_v2/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/cdn_loop/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/composite/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/compressor/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/connect_grpc_bridge/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/cors/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/credential_injector/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/csrf/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/custom_response/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/decompressor/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/dynamic_forward_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/dynamic_modules/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/ext_authz/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/ext_proc/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/fault/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/file_system_buffer/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/gcp_authn/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/geoip/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/grpc_field_extraction/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/grpc_http1_bridge/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/grpc_http1_reverse_bridge/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/grpc_json_reverse_transcoder/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/grpc_json_transcoder/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/grpc_stats/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/grpc_web/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/gzip/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/header_mutation/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/header_to_metadata/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/health_check/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/ip_tagging/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/json_to_metadata/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/jwt_authn/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/kill_request/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/local_ratelimit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/lua/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/mcp/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/mcp_router/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/oauth2/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/on_demand/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/original_src/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/proto_api_scrubber/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/proto_message_extraction/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/rate_limit_quota/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/ratelimit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/rbac/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/router/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/set_filter_state/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/set_metadata/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/stateful_session/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/tap/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/thrift_to_metadata/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/transform/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/upstream_codec/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/wasm/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/listener/dynamic_modules/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/listener/http_inspector/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/listener/local_ratelimit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/listener/original_dst/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/listener/original_src/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/listener/proxy_protocol/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/listener/tls_inspector/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/connection_limit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/direct_response/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/dubbo_proxy/router/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/dubbo_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/dynamic_modules/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/echo/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/ext_authz/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/ext_proc/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/generic_proxy/action/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/generic_proxy/codecs/dubbo/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/generic_proxy/codecs/http1/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/generic_proxy/matcher/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/generic_proxy/router/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/generic_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/geoip/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/http_connection_manager/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/local_ratelimit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/mongo_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/ratelimit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/rbac/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/redis_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/reverse_tunnel/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/set_filter_state/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/sni_cluster/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/sni_dynamic_forward_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/tcp_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/thrift_proxy/filters/header_to_metadata/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/thrift_proxy/filters/payload_to_metadata/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/thrift_proxy/filters/ratelimit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/thrift_proxy/router/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/thrift_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/wasm/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/zookeeper_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/udp/dns_filter/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/udp/dynamic_modules/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/udp/udp_proxy/session/dynamic_forward_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/udp/udp_proxy/session/http_capsule/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/filters/udp/udp_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/formatter/cel/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/formatter/metadata/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/formatter/req_without_query/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/geoip_providers/common/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/geoip_providers/maxmind/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/call_credentials/access_token/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/call_credentials/file_based_metadata/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/call_credentials/google_compute_engine/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/call_credentials/google_iam/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/call_credentials/google_refresh_token/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/call_credentials/service_account_jwt_access/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/call_credentials/sts_service/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/channel_credentials/google_default/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/channel_credentials/insecure/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/channel_credentials/local/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/channel_credentials/tls/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/grpc_service/channel_credentials/xds/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/health_check/event_sinks/file/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/health_checkers/redis/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/health_checkers/thrift/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/cache/file_system_http_cache/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/cache/simple_http_cache/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/cache_v2/file_system_http_cache/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/cache_v2/simple_http_cache/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/custom_response/local_response_policy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/custom_response/redirect_policy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/early_header_mutation/header_mutation/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/ext_proc/processing_request_modifiers/mapped_attribute_builder/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/ext_proc/response_processors/save_processing_response/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/header_formatters/preserve_case/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/header_validators/envoy_default/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/injected_credentials/generic/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/injected_credentials/oauth2/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/original_ip_detection/custom_header/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/original_ip_detection/xff/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/stateful_session/cookie/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/stateful_session/envelope/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/http/stateful_session/header/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/internal_redirect/allow_listed_routes/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/internal_redirect/previous_routes/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/internal_redirect/safe_cross_scheme/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/key_value/file_based/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/client_side_weighted_round_robin/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/cluster_provided/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/common/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/least_request/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/maglev/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/override_host/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/pick_first/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/random/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/random_subsetting/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/ring_hash/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/round_robin/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/subset/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/wrr_locality/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/local_address_selectors/filter_state_override/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/matching/common_inputs/environment_variable/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/matching/common_inputs/network/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/matching/common_inputs/ssl/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/matching/common_inputs/stats/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/matching/common_inputs/transport_socket/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/matching/input_matchers/consistent_hashing/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/matching/input_matchers/ip/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/matching/input_matchers/metadata/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/matching/input_matchers/runtime_fraction/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/network/dns_resolver/apple/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/network/dns_resolver/cares/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/network/dns_resolver/getaddrinfo/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/network/socket_interface/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/outlier_detection_monitors/common/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/outlier_detection_monitors/consecutive_errors/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/path/match/uri_template/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/path/rewrite/uri_template/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/quic/client_writer_factory/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/quic/connection_debug_visitor/quic_stats/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/quic/connection_debug_visitor/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/quic/connection_id_generator/quic_lb/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/quic/connection_id_generator/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/quic/crypto_stream/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/quic/proof_source/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/quic/server_preferred_address/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/rate_limit_descriptors/expr/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/rbac/audit_loggers/stream/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/rbac/matchers/upstream_ip_port/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/rbac/principals/mtls_authenticated/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/regex_engines/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/request_id/uuid/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/resource_monitors/cgroup_memory/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/resource_monitors/cpu_utilization/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/resource_monitors/downstream_connections/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/resource_monitors/fixed_heap/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/resource_monitors/injected_resource/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/retry/host/omit_canary_hosts/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/retry/host/omit_host_metadata/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/retry/host/previous_hosts/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/retry/priority/previous_priorities/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/router/cluster_specifiers/lua/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/router/cluster_specifiers/matcher/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/stat_sinks/graphite_statsd/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/stat_sinks/open_telemetry/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/stat_sinks/wasm/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/string_matcher/lua/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/tracers/fluentd/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/tracers/opentelemetry/resource_detectors/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/tracers/opentelemetry/samplers/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/alts/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/http_11_proxy/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/internal_upstream/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/proxy_protocol/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/quic/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/raw_buffer/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/s2a/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/starttls/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/tap/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/tcp_stats/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/tls/cert_mappers/sni/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/tls/cert_mappers/static_name/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/tls/cert_selectors/on_demand_secret/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/tls/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/udp_packet_writer/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/upstreams/http/generic/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/upstreams/http/http/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/upstreams/http/tcp/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/upstreams/http/udp/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/upstreams/http/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/upstreams/tcp/generic/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/upstreams/tcp/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/wasm/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/extensions/watchdog/profile_action/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/accesslog/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/accesslog/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/auth/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/auth/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/auth/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/cluster/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/discovery/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/discovery/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/endpoint/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/event_reporting/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/event_reporting/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/ext_proc/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/extension/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/health/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/listener/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/load_stats/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/load_stats/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/metrics/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/metrics/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/network_ext_proc/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/rate_limit_quota/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/ratelimit/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/ratelimit/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/redis_auth/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/route/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/runtime/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/secret/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/status/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/status/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/tap/v2alpha) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/service/tap/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/type) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/type/http/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/type/matcher) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/type/matcher/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/type/metadata/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/type/metadata/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/type/tracing/v2) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/type/tracing/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/type/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/envoy/watchdog/v3) = %{version}

Requires:       go(cel.dev/expr)
Requires:       go(github.com/cncf/xds/go)
Requires:       go(github.com/envoyproxy/go-control-plane)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(github.com/planetscale/vtprotobuf)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(go.opentelemetry.io/proto/otlp)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package provides Envoy API Go module from go-control-plane.

%install -a
find %{buildroot}%{go_sys_gopath}/%{go_import_path} -mindepth 1 -maxdepth 1 ! -name envoy -exec rm -rf {} +

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}/envoy

%changelog
%autochangelog
