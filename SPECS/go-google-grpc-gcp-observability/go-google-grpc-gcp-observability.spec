# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           observability
%define go_import_path  google.golang.org/grpc/gcp/observability
%define go_source_subdir gcp/observability

Name:           go-google-grpc-gcp-observability
Version:        1.0.1
Release:        %autorelease
Summary:        gRPC GCP observability module for Go
License:        Apache-2.0
URL:            https://github.com/grpc/grpc-go
#!RemoteAsset:  sha256:2538be0662d2222b9a800723aa433ea5ea3c2fcc29df04bf03542b666ea2e63b
Source0:        https://github.com/grpc/grpc-go/archive/refs/tags/gcp/observability/v1.0.1.tar.gz#/%{_name}-%{version}.tar.gz
Patch2000:      2000-treat-empty-and-nil-logged-messages-as-equal.patch
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n grpc-go-gcp-observability-v1.0.1
# This package owns a Go module below the repository root; the explicit
# %%install/%%check sections below copy only %%{go_source_subdir}, because
# the default golangmodules phases would copy the full archive under
# %%{go_import_path} and create invalid import paths.
# The patch keeps logging tests compatible with the current grpc binarylog
# dependency, which returns an empty message slice where this older module
# expected nil.

BuildRequires:  go
BuildRequires:  go(cloud.google.com/go/logging)
BuildRequires:  go(contrib.go.opencensus.io/exporter/stackdriver)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/config)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/credentials)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/configsources)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/internal/ini)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sso)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/service/sts)
BuildRequires:  go(github.com/aws/smithy-go)
BuildRequires:  go(github.com/census-instrumentation/opencensus-proto)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/appengine)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/backoff)
BuildRequires:  go(google.golang.org/grpc/balancer)
BuildRequires:  go(google.golang.org/grpc/balancer/base)
BuildRequires:  go(google.golang.org/grpc/balancer/grpclb)
BuildRequires:  go(google.golang.org/grpc/balancer/roundrobin)
BuildRequires:  go(google.golang.org/grpc/binarylog/grpc_binarylog_v1)
BuildRequires:  go(google.golang.org/grpc/channelz)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/connectivity)
BuildRequires:  go(google.golang.org/grpc/credentials)
BuildRequires:  go(google.golang.org/grpc/credentials/google)
BuildRequires:  go(google.golang.org/grpc/credentials/insecure)
BuildRequires:  go(google.golang.org/grpc/credentials/oauth)
BuildRequires:  go(google.golang.org/grpc/encoding)
BuildRequires:  go(google.golang.org/grpc/encoding/proto)
BuildRequires:  go(google.golang.org/grpc/grpclog)
BuildRequires:  go(google.golang.org/grpc/internal)
BuildRequires:  go(google.golang.org/grpc/internal/backoff)
BuildRequires:  go(google.golang.org/grpc/internal/balancer/gracefulswitch)
BuildRequires:  go(google.golang.org/grpc/internal/balancerload)
BuildRequires:  go(google.golang.org/grpc/internal/binarylog)
BuildRequires:  go(google.golang.org/grpc/internal/channelz)
BuildRequires:  go(google.golang.org/grpc/internal/envconfig)
BuildRequires:  go(google.golang.org/grpc/internal/grpclog)
BuildRequires:  go(google.golang.org/grpc/internal/grpcrand)
BuildRequires:  go(google.golang.org/grpc/internal/grpcsync)
BuildRequires:  go(google.golang.org/grpc/internal/grpctest)
BuildRequires:  go(google.golang.org/grpc/internal/grpcutil)
BuildRequires:  go(google.golang.org/grpc/internal/idle)
BuildRequires:  go(google.golang.org/grpc/internal/leakcheck)
BuildRequires:  go(google.golang.org/grpc/internal/metadata)
BuildRequires:  go(google.golang.org/grpc/internal/pretty)
BuildRequires:  go(google.golang.org/grpc/internal/resolver)
BuildRequires:  go(google.golang.org/grpc/internal/resolver/passthrough)
BuildRequires:  go(google.golang.org/grpc/internal/resolver/unix)
BuildRequires:  go(google.golang.org/grpc/internal/serviceconfig)
BuildRequires:  go(google.golang.org/grpc/internal/status)
BuildRequires:  go(google.golang.org/grpc/internal/stubserver)
BuildRequires:  go(google.golang.org/grpc/internal/testutils)
BuildRequires:  go(google.golang.org/grpc/internal/transport)
BuildRequires:  go(google.golang.org/grpc/interop/grpc_testing)
BuildRequires:  go(google.golang.org/grpc/keepalive)
BuildRequires:  go(google.golang.org/grpc/metadata)
BuildRequires:  go(google.golang.org/grpc/peer)
BuildRequires:  go(google.golang.org/grpc/resolver)
BuildRequires:  go(google.golang.org/grpc/resolver/dns)
BuildRequires:  go(google.golang.org/grpc/serviceconfig)
BuildRequires:  go(google.golang.org/grpc/stats)
BuildRequires:  go(google.golang.org/grpc/stats/opencensus)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(google.golang.org/grpc/tap)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(google.golang.org/grpc/gcp/observability) = %{version}

Requires:       go(cloud.google.com/go/logging)
Requires:       go(contrib.go.opencensus.io/exporter/stackdriver)
Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/config)
Requires:       go(github.com/aws/aws-sdk-go-v2/credentials)
Requires:       go(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/configsources)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)
Requires:       go(github.com/aws/aws-sdk-go-v2/internal/ini)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sso)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/ssooidc)
Requires:       go(github.com/aws/aws-sdk-go-v2/service/sts)
Requires:       go(github.com/aws/smithy-go)
Requires:       go(github.com/census-instrumentation/opencensus-proto)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/s2a-go)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(go.opencensus.io)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/appengine)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/backoff)
Requires:       go(google.golang.org/grpc/balancer)
Requires:       go(google.golang.org/grpc/balancer/base)
Requires:       go(google.golang.org/grpc/balancer/grpclb)
Requires:       go(google.golang.org/grpc/balancer/roundrobin)
Requires:       go(google.golang.org/grpc/binarylog/grpc_binarylog_v1)
Requires:       go(google.golang.org/grpc/channelz)
Requires:       go(google.golang.org/grpc/codes)
Requires:       go(google.golang.org/grpc/connectivity)
Requires:       go(google.golang.org/grpc/credentials)
Requires:       go(google.golang.org/grpc/credentials/google)
Requires:       go(google.golang.org/grpc/credentials/insecure)
Requires:       go(google.golang.org/grpc/credentials/oauth)
Requires:       go(google.golang.org/grpc/encoding)
Requires:       go(google.golang.org/grpc/encoding/proto)
Requires:       go(google.golang.org/grpc/grpclog)
Requires:       go(google.golang.org/grpc/internal)
Requires:       go(google.golang.org/grpc/internal/backoff)
Requires:       go(google.golang.org/grpc/internal/balancer/gracefulswitch)
Requires:       go(google.golang.org/grpc/internal/balancerload)
Requires:       go(google.golang.org/grpc/internal/binarylog)
Requires:       go(google.golang.org/grpc/internal/channelz)
Requires:       go(google.golang.org/grpc/internal/envconfig)
Requires:       go(google.golang.org/grpc/internal/grpclog)
Requires:       go(google.golang.org/grpc/internal/grpcrand)
Requires:       go(google.golang.org/grpc/internal/grpcsync)
Requires:       go(google.golang.org/grpc/internal/grpcutil)
Requires:       go(google.golang.org/grpc/internal/idle)
Requires:       go(google.golang.org/grpc/internal/metadata)
Requires:       go(google.golang.org/grpc/internal/pretty)
Requires:       go(google.golang.org/grpc/internal/resolver)
Requires:       go(google.golang.org/grpc/internal/resolver/passthrough)
Requires:       go(google.golang.org/grpc/internal/resolver/unix)
Requires:       go(google.golang.org/grpc/internal/serviceconfig)
Requires:       go(google.golang.org/grpc/internal/status)
Requires:       go(google.golang.org/grpc/internal/transport)
Requires:       go(google.golang.org/grpc/keepalive)
Requires:       go(google.golang.org/grpc/metadata)
Requires:       go(google.golang.org/grpc/peer)
Requires:       go(google.golang.org/grpc/resolver)
Requires:       go(google.golang.org/grpc/resolver/dns)
Requires:       go(google.golang.org/grpc/serviceconfig)
Requires:       go(google.golang.org/grpc/stats)
Requires:       go(google.golang.org/grpc/stats/opencensus)
Requires:       go(google.golang.org/grpc/status)
Requires:       go(google.golang.org/grpc/tap)
Requires:       go(google.golang.org/protobuf)

%description
This package provides gRPC GCP observability module for Go.

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
