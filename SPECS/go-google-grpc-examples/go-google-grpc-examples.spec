# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           examples
%define go_import_path  google.golang.org/grpc/examples
%define go_source_subdir examples
%define commit_id 609310837bbc7fab1553fa53f2d1312bd7d85275

Name:           go-google-grpc-examples
Version:        0+git20260522.609310837
Release:        %autorelease
Summary:        gRPC examples module for Go
License:        Apache-2.0
URL:            https://github.com/grpc/grpc-go
#!RemoteAsset:  sha256:36ee6dfd00593aaee885ad624d1a93439aceb71eb1168449824eb10fcf64d4d1
Source0:        https://github.com/grpc/grpc-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n grpc-go-%{commit_id}
# This package owns a Go module below the repository root; the explicit
# %%install/%%check sections below copy only %%{go_source_subdir}, because
# the default golangmodules phases would copy the full archive under
# %%{go_import_path} and create invalid import paths.

BuildRequires:  go
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/config)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/credentials)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/configsources)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/ini)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/signin)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sso)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sts)
BuildRequires:  go(github.com/aws/smithy-go)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/census-instrumentation/opencensus-proto)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/envoy)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/planetscale/vtprotobuf)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/otlptranslator)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/spiffe/go-spiffe/v2)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/detectors/gcp)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/prometheus)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.yaml.in/yaml/v2)
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
BuildRequires:  go(google.golang.org/grpc/authz)
BuildRequires:  go(google.golang.org/grpc/backoff)
BuildRequires:  go(google.golang.org/grpc/balancer)
BuildRequires:  go(google.golang.org/grpc/balancer/base)
BuildRequires:  go(google.golang.org/grpc/balancer/endpointsharding)
BuildRequires:  go(google.golang.org/grpc/balancer/pickfirst)
BuildRequires:  go(google.golang.org/grpc/balancer/roundrobin)
BuildRequires:  go(google.golang.org/grpc/channelz)
BuildRequires:  go(google.golang.org/grpc/channelz/service)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/connectivity)
BuildRequires:  go(google.golang.org/grpc/credentials)
BuildRequires:  go(google.golang.org/grpc/credentials/alts)
BuildRequires:  go(google.golang.org/grpc/credentials/insecure)
BuildRequires:  go(google.golang.org/grpc/credentials/oauth)
BuildRequires:  go(google.golang.org/grpc/credentials/tls/certprovider)
BuildRequires:  go(google.golang.org/grpc/credentials/tls/certprovider/pemfile)
BuildRequires:  go(google.golang.org/grpc/credentials/xds)
BuildRequires:  go(google.golang.org/grpc/encoding)
BuildRequires:  go(google.golang.org/grpc/encoding/gzip)
BuildRequires:  go(google.golang.org/grpc/encoding/proto)
BuildRequires:  go(google.golang.org/grpc/experimental/opentelemetry)
BuildRequires:  go(google.golang.org/grpc/experimental/stats)
BuildRequires:  go(google.golang.org/grpc/gcp/observability)
BuildRequires:  go(google.golang.org/grpc/grpclog)
BuildRequires:  go(google.golang.org/grpc/health)
BuildRequires:  go(google.golang.org/grpc/health/grpc_health_v1)
BuildRequires:  go(google.golang.org/grpc/internal)
BuildRequires:  go(google.golang.org/grpc/internal/backoff)
BuildRequires:  go(google.golang.org/grpc/internal/balancer/gracefulswitch)
BuildRequires:  go(google.golang.org/grpc/internal/balancerload)
BuildRequires:  go(google.golang.org/grpc/internal/binarylog)
BuildRequires:  go(google.golang.org/grpc/internal/channelz)
BuildRequires:  go(google.golang.org/grpc/internal/credentials)
BuildRequires:  go(google.golang.org/grpc/internal/grpcsync)
BuildRequires:  go(google.golang.org/grpc/internal/grpcutil)
BuildRequires:  go(google.golang.org/grpc/internal/idle)
BuildRequires:  go(google.golang.org/grpc/internal/metadata)
BuildRequires:  go(google.golang.org/grpc/internal/pretty)
BuildRequires:  go(google.golang.org/grpc/internal/resolver)
BuildRequires:  go(google.golang.org/grpc/internal/resolver/delegatingresolver)
BuildRequires:  go(google.golang.org/grpc/internal/resolver/passthrough)
BuildRequires:  go(google.golang.org/grpc/internal/resolver/unix)
BuildRequires:  go(google.golang.org/grpc/internal/serviceconfig)
BuildRequires:  go(google.golang.org/grpc/internal/stats)
BuildRequires:  go(google.golang.org/grpc/internal/status)
BuildRequires:  go(google.golang.org/grpc/internal/transport)
BuildRequires:  go(google.golang.org/grpc/keepalive)
BuildRequires:  go(google.golang.org/grpc/mem)
BuildRequires:  go(google.golang.org/grpc/metadata)
BuildRequires:  go(google.golang.org/grpc/orca)
BuildRequires:  go(google.golang.org/grpc/peer)
BuildRequires:  go(google.golang.org/grpc/reflection)
BuildRequires:  go(google.golang.org/grpc/resolver)
BuildRequires:  go(google.golang.org/grpc/resolver/dns)
BuildRequires:  go(google.golang.org/grpc/resolver/manual)
BuildRequires:  go(google.golang.org/grpc/security/advancedtls)
BuildRequires:  go(google.golang.org/grpc/serviceconfig)
BuildRequires:  go(google.golang.org/grpc/stats)
BuildRequires:  go(google.golang.org/grpc/stats/opencensus)
BuildRequires:  go(google.golang.org/grpc/stats/opentelemetry)
BuildRequires:  go(google.golang.org/grpc/stats/opentelemetry/csm)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(google.golang.org/grpc/tap)
BuildRequires:  go(google.golang.org/grpc/xds)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(google.golang.org/grpc/examples) = %{version}

Requires:       go(cel.dev/expr)
Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/config)
Requires:       go(github.com/aws/aws-sdk-go-v2/credentials)
Requires:       go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/configsources)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/ini)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/signin)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sso)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sts)
Requires:       go(github.com/aws/smithy-go)
Requires:       go(github.com/beorn7/perks)
Requires:       go(github.com/census-instrumentation/opencensus-proto)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/cncf/xds/go)
Requires:       go(github.com/envoyproxy/go-control-plane/envoy)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/s2a-go)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
Requires:       go(github.com/munnerz/goautoneg)
Requires:       go(github.com/planetscale/vtprotobuf)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/otlptranslator)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/spiffe/go-spiffe/v2)
Requires:       go(go.opencensus.io)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib/detectors/gcp)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/exporters/prometheus)
Requires:       go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/authz)
Requires:       go(google.golang.org/grpc/backoff)
Requires:       go(google.golang.org/grpc/balancer)
Requires:       go(google.golang.org/grpc/balancer/base)
Requires:       go(google.golang.org/grpc/balancer/endpointsharding)
Requires:       go(google.golang.org/grpc/balancer/pickfirst)
Requires:       go(google.golang.org/grpc/balancer/roundrobin)
Requires:       go(google.golang.org/grpc/channelz)
Requires:       go(google.golang.org/grpc/channelz/service)
Requires:       go(google.golang.org/grpc/codes)
Requires:       go(google.golang.org/grpc/connectivity)
Requires:       go(google.golang.org/grpc/credentials)
Requires:       go(google.golang.org/grpc/credentials/alts)
Requires:       go(google.golang.org/grpc/credentials/insecure)
Requires:       go(google.golang.org/grpc/credentials/oauth)
Requires:       go(google.golang.org/grpc/credentials/tls/certprovider)
Requires:       go(google.golang.org/grpc/credentials/tls/certprovider/pemfile)
Requires:       go(google.golang.org/grpc/credentials/xds)
Requires:       go(google.golang.org/grpc/encoding)
Requires:       go(google.golang.org/grpc/encoding/gzip)
Requires:       go(google.golang.org/grpc/encoding/proto)
Requires:       go(google.golang.org/grpc/experimental/opentelemetry)
Requires:       go(google.golang.org/grpc/experimental/stats)
Requires:       go(google.golang.org/grpc/gcp/observability)
Requires:       go(google.golang.org/grpc/grpclog)
Requires:       go(google.golang.org/grpc/health)
Requires:       go(google.golang.org/grpc/health/grpc_health_v1)
Requires:       go(google.golang.org/grpc/internal)
Requires:       go(google.golang.org/grpc/internal/backoff)
Requires:       go(google.golang.org/grpc/internal/balancer/gracefulswitch)
Requires:       go(google.golang.org/grpc/internal/balancerload)
Requires:       go(google.golang.org/grpc/internal/binarylog)
Requires:       go(google.golang.org/grpc/internal/channelz)
Requires:       go(google.golang.org/grpc/internal/credentials)
Requires:       go(google.golang.org/grpc/internal/grpcsync)
Requires:       go(google.golang.org/grpc/internal/grpcutil)
Requires:       go(google.golang.org/grpc/internal/idle)
Requires:       go(google.golang.org/grpc/internal/metadata)
Requires:       go(google.golang.org/grpc/internal/pretty)
Requires:       go(google.golang.org/grpc/internal/resolver)
Requires:       go(google.golang.org/grpc/internal/resolver/delegatingresolver)
Requires:       go(google.golang.org/grpc/internal/resolver/passthrough)
Requires:       go(google.golang.org/grpc/internal/resolver/unix)
Requires:       go(google.golang.org/grpc/internal/serviceconfig)
Requires:       go(google.golang.org/grpc/internal/stats)
Requires:       go(google.golang.org/grpc/internal/status)
Requires:       go(google.golang.org/grpc/internal/transport)
Requires:       go(google.golang.org/grpc/keepalive)
Requires:       go(google.golang.org/grpc/mem)
Requires:       go(google.golang.org/grpc/metadata)
Requires:       go(google.golang.org/grpc/orca)
Requires:       go(google.golang.org/grpc/peer)
Requires:       go(google.golang.org/grpc/reflection)
Requires:       go(google.golang.org/grpc/resolver)
Requires:       go(google.golang.org/grpc/resolver/dns)
Requires:       go(google.golang.org/grpc/resolver/manual)
Requires:       go(google.golang.org/grpc/security/advancedtls)
Requires:       go(google.golang.org/grpc/serviceconfig)
Requires:       go(google.golang.org/grpc/stats)
Requires:       go(google.golang.org/grpc/stats/opencensus)
Requires:       go(google.golang.org/grpc/stats/opentelemetry)
Requires:       go(google.golang.org/grpc/stats/opentelemetry/csm)
Requires:       go(google.golang.org/grpc/status)
Requires:       go(google.golang.org/grpc/tap)
Requires:       go(google.golang.org/grpc/xds)
Requires:       go(google.golang.org/protobuf)

%description
This package provides gRPC examples module for Go.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
export GO111MODULE=off
# Submodule tests import packages, including internal packages, from the parent
# grpc module. Copy the installed parent tree into the temporary GOPATH first so
# Go's internal package visibility checks use a single physical tree.
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
_go_parent=%{go_import_path}
_go_parent_copy=
while :; do
    _go_next_parent=${_go_parent%/*}
    [ "${_go_next_parent}" = "${_go_parent}" ] && break
    _go_parent=${_go_next_parent}
    if [ -d "%{_datadir}/gocode/src/${_go_parent}" ] &&
       { [ -f "%{_datadir}/gocode/src/${_go_parent}/go.mod" ] ||
         [ -n "$(find "%{_datadir}/gocode/src/${_go_parent}" -maxdepth 1 -name '*.go' -print -quit 2>/dev/null)" ]; }; then
        _go_parent_copy=${_go_parent}
    fi
done
if [ -n "${_go_parent_copy}" ]; then
    mkdir -p "%{_builddir}/go/src/$(dirname "${_go_parent_copy}")"
    rm -rf "%{_builddir}/go/src/${_go_parent_copy}"
    cp -a "%{_datadir}/gocode/src/${_go_parent_copy}" "%{_builddir}/go/src/${_go_parent_copy}"
fi
mkdir -p "%{_builddir}/go/src/$(dirname "%{go_import_path}")"
rm -rf %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}
_go_pkgs="%{?go_test_include}"
if [ -z "${_go_pkgs}" ]; then
    _go_pkgs=$(go list -e -f '{{.ImportPath}}' ./...)
fi
_go_exclude="%{?go_test_exclude}"
_go_exclude_glob="%{?go_test_exclude_glob}"
_go_filtered=""
set -f
for _pkg in ${_go_pkgs}; do
    _skip=0
    for _ex in ${_go_exclude}; do
        [ "${_pkg}" = "${_ex}" ] && _skip=1
    done
    for _ex in ${_go_exclude_glob}; do
        case "${_pkg}" in ${_ex}) _skip=1 ;; esac
    done
    [ ${_skip} -eq 0 ] && _go_filtered="${_go_filtered} ${_pkg}"
done
set +f
test -n "${_go_filtered}"
go test -v ${_go_filtered}
popd

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%license NOTICE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
