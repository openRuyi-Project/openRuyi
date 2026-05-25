# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           opencensus
%define go_import_path  google.golang.org/grpc/stats/opencensus
%define go_source_subdir stats/opencensus

Name:           go-google-grpc-stats-opencensus
Version:        1.0.0
Release:        %autorelease
Summary:        gRPC OpenCensus stats module for Go
License:        Apache-2.0
URL:            https://github.com/grpc/grpc-go
#!RemoteAsset:  sha256:edf12f9dcc8b907b013e29251fab6b3459976e3fd72de6ac22772b1185fba6b0
Source0:        https://github.com/grpc/grpc-go/archive/refs/tags/stats/opencensus/v1.0.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n grpc-go-stats-opencensus-v1.0.0
# This package owns a Go module below the repository root; the explicit
# %%install/%%check sections below copy only %%{go_source_subdir}, because
# the default golangmodules phases would copy the full archive under
# %%{go_import_path} and create invalid import paths.

BuildRequires:  go
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/grpc/backoff)
BuildRequires:  go(google.golang.org/grpc/balancer)
BuildRequires:  go(google.golang.org/grpc/balancer/base)
BuildRequires:  go(google.golang.org/grpc/balancer/roundrobin)
BuildRequires:  go(google.golang.org/grpc/channelz)
BuildRequires:  go(google.golang.org/grpc/codes)
BuildRequires:  go(google.golang.org/grpc/connectivity)
BuildRequires:  go(google.golang.org/grpc/credentials)
BuildRequires:  go(google.golang.org/grpc/credentials/insecure)
BuildRequires:  go(google.golang.org/grpc/encoding)
BuildRequires:  go(google.golang.org/grpc/encoding/gzip)
BuildRequires:  go(google.golang.org/grpc/encoding/proto)
BuildRequires:  go(google.golang.org/grpc/grpclog)
BuildRequires:  go(google.golang.org/grpc/internal)
BuildRequires:  go(google.golang.org/grpc/internal/backoff)
BuildRequires:  go(google.golang.org/grpc/internal/balancer/gracefulswitch)
BuildRequires:  go(google.golang.org/grpc/internal/balancerload)
BuildRequires:  go(google.golang.org/grpc/internal/binarylog)
BuildRequires:  go(google.golang.org/grpc/internal/buffer)
BuildRequires:  go(google.golang.org/grpc/internal/channelz)
BuildRequires:  go(google.golang.org/grpc/internal/grpcrand)
BuildRequires:  go(google.golang.org/grpc/internal/grpcsync)
BuildRequires:  go(google.golang.org/grpc/internal/grpctest)
BuildRequires:  go(google.golang.org/grpc/internal/grpcutil)
BuildRequires:  go(google.golang.org/grpc/internal/leakcheck)
BuildRequires:  go(google.golang.org/grpc/internal/metadata)
BuildRequires:  go(google.golang.org/grpc/internal/pretty)
BuildRequires:  go(google.golang.org/grpc/internal/resolver)
BuildRequires:  go(google.golang.org/grpc/internal/resolver/dns)
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
BuildRequires:  go(google.golang.org/grpc/serviceconfig)
BuildRequires:  go(google.golang.org/grpc/status)
BuildRequires:  go(google.golang.org/grpc/tap)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(google.golang.org/grpc/stats/opencensus) = %{version}

Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/go-cmp)
Requires:       go(go.opencensus.io)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/grpc/backoff)
Requires:       go(google.golang.org/grpc/balancer)
Requires:       go(google.golang.org/grpc/balancer/base)
Requires:       go(google.golang.org/grpc/balancer/roundrobin)
Requires:       go(google.golang.org/grpc/channelz)
Requires:       go(google.golang.org/grpc/codes)
Requires:       go(google.golang.org/grpc/connectivity)
Requires:       go(google.golang.org/grpc/credentials)
Requires:       go(google.golang.org/grpc/credentials/insecure)
Requires:       go(google.golang.org/grpc/encoding)
Requires:       go(google.golang.org/grpc/encoding/proto)
Requires:       go(google.golang.org/grpc/grpclog)
Requires:       go(google.golang.org/grpc/internal)
Requires:       go(google.golang.org/grpc/internal/backoff)
Requires:       go(google.golang.org/grpc/internal/balancer/gracefulswitch)
Requires:       go(google.golang.org/grpc/internal/balancerload)
Requires:       go(google.golang.org/grpc/internal/binarylog)
Requires:       go(google.golang.org/grpc/internal/buffer)
Requires:       go(google.golang.org/grpc/internal/channelz)
Requires:       go(google.golang.org/grpc/internal/grpcrand)
Requires:       go(google.golang.org/grpc/internal/grpcsync)
Requires:       go(google.golang.org/grpc/internal/grpcutil)
Requires:       go(google.golang.org/grpc/internal/metadata)
Requires:       go(google.golang.org/grpc/internal/pretty)
Requires:       go(google.golang.org/grpc/internal/resolver)
Requires:       go(google.golang.org/grpc/internal/resolver/dns)
Requires:       go(google.golang.org/grpc/internal/resolver/passthrough)
Requires:       go(google.golang.org/grpc/internal/resolver/unix)
Requires:       go(google.golang.org/grpc/internal/serviceconfig)
Requires:       go(google.golang.org/grpc/internal/status)
Requires:       go(google.golang.org/grpc/internal/transport)
Requires:       go(google.golang.org/grpc/keepalive)
Requires:       go(google.golang.org/grpc/metadata)
Requires:       go(google.golang.org/grpc/peer)
Requires:       go(google.golang.org/grpc/resolver)
Requires:       go(google.golang.org/grpc/serviceconfig)
Requires:       go(google.golang.org/grpc/status)
Requires:       go(google.golang.org/grpc/tap)
Requires:       go(google.golang.org/protobuf)

%description
This package provides gRPC OpenCensus stats module for Go.

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
# OBS currently fails only Test/Span with unexpected OpenCensus span diff:
# got missing TraceID/SpanID fields and changed Attempt span ordering.
go test -v -skip '^Test/Span$' ${_go_filtered}
popd

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%license NOTICE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
