# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           etcd
%define go_import_path  go.etcd.io/etcd/v3
%define git_sha         68c065e562994b89e333e77b039ad066f933c586

Name:           etcd
Version:        3.7.2
Release:        %autorelease
Summary:        Distributed reliable key-value store
License:        Apache-2.0
URL:            https://github.com/etcd-io/etcd
#!RemoteAsset:  sha256:5f5bfff6886c47ac841f46097b30f9aae917e918adf158d0b81042d078af93d0
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        etcd.service
Source2:        etcd.sysusers
Source3:        etcd.tmpfiles

BuildRequires:  go >= 1.26
BuildRequires:  go-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  go(github.com/bgentry/speakeasy)
BuildRequires:  go(github.com/cheggaaa/pb/v3)
BuildRequires:  go(github.com/coreos/go-semver)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/creack/pty)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware/v2)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/jonboulle/clockwork)
BuildRequires:  go(github.com/olekukonko/tablewriter) >= 1.1.4
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/soheilhy/cmux)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tmc/grpc-websocket-proxy)
BuildRequires:  go(github.com/xiang90/probing)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(go.etcd.io/raft/v3)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  go(gotest.tools/v3)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/yaml)

%{?systemd_requires}

%description
etcd is a strongly consistent, distributed key-value store that provides a
reliable way to store data that must be accessed by a distributed system or
cluster of machines. Kubernetes uses etcd as its primary backing store for
cluster state.

%prep
%autosetup -n %{name}-%{version}
# etcd is a multi-module repository. Map its first-party modules into GOPATH;
# all third-party modules are supplied by distribution Go provider packages.
install -d %{_builddir}/go/src/go.etcd.io/etcd
ln -snf "$(pwd)" %{_builddir}/go/src/go.etcd.io/etcd/v3
install -d %{_builddir}/go/src/go.etcd.io/etcd/cache
ln -snf "$(pwd)/cache" %{_builddir}/go/src/go.etcd.io/etcd/cache/v3
install -d %{_builddir}/go/src/go.etcd.io/etcd/api
ln -snf "$(pwd)/api" %{_builddir}/go/src/go.etcd.io/etcd/api/v3
install -d %{_builddir}/go/src/go.etcd.io/etcd/client/pkg
ln -snf "$(pwd)/client/pkg" %{_builddir}/go/src/go.etcd.io/etcd/client/pkg/v3
ln -snf "$(pwd)/client/v3" %{_builddir}/go/src/go.etcd.io/etcd/client/v3
install -d %{_builddir}/go/src/go.etcd.io/etcd/etcdctl
ln -snf "$(pwd)/etcdctl" %{_builddir}/go/src/go.etcd.io/etcd/etcdctl/v3
install -d %{_builddir}/go/src/go.etcd.io/etcd/etcdutl
ln -snf "$(pwd)/etcdutl" %{_builddir}/go/src/go.etcd.io/etcd/etcdutl/v3
install -d %{_builddir}/go/src/go.etcd.io/etcd/pkg
ln -snf "$(pwd)/pkg" %{_builddir}/go/src/go.etcd.io/etcd/pkg/v3
install -d %{_builddir}/go/src/go.etcd.io/etcd/server
ln -snf "$(pwd)/server" %{_builddir}/go/src/go.etcd.io/etcd/server/v3

%build
%go_common
export GOCACHE=%{_builddir}/go-build-cache
export GO111MODULE=off
export GONOSUMDB="*"
export GOPROXY=off
export GOTOOLCHAIN=local
go_ldflags="-X=go.etcd.io/etcd/api/v3/version.GitSHA=%{git_sha}"
build_root="$(pwd)"
install -d bin

(
    cd %{_builddir}/go/src/go.etcd.io/etcd/server/v3
    CGO_ENABLED=0 %{__go} build -trimpath -installsuffix=cgo \
        -ldflags "${go_ldflags}" -o "${build_root}/bin/etcd" .
)

(
    cd %{_builddir}/go/src/go.etcd.io/etcd/etcdctl/v3
    CGO_ENABLED=0 %{__go} build -trimpath -installsuffix=cgo \
        -ldflags "${go_ldflags}" -o "${build_root}/bin/etcdctl" .
)

(
    cd %{_builddir}/go/src/go.etcd.io/etcd/etcdutl/v3
    CGO_ENABLED=0 %{__go} build -trimpath -installsuffix=cgo \
        -ldflags "${go_ldflags}" -o "${build_root}/bin/etcdutl" .
)

%install
install -Dpm0755 bin/etcd %{buildroot}%{_bindir}/etcd
install -Dpm0755 bin/etcdctl %{buildroot}%{_bindir}/etcdctl
install -Dpm0755 bin/etcdutl %{buildroot}%{_bindir}/etcdutl
install -Dpm0644 %{SOURCE1} %{buildroot}%{_unitdir}/etcd.service
install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/etcd.conf
install -Dpm0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/etcd.conf
install -dpm0750 %{buildroot}%{_localstatedir}/lib/etcd

%check
%go_common
export GOTOOLCHAIN=local
export GOCACHE=%{_builddir}/go-build-cache
# Enter through GOPATH to keep canonical package names and relative test fixtures.
for module in api/v3 cache/v3 client/pkg/v3 client/v3 pkg/v3 etcdctl/v3 etcdutl/v3; do
    (
        cd %{_builddir}/go/src/go.etcd.io/etcd/$module
        CGO_ENABLED=0 %{__go} test -short ./...
    )
done
(
    cd %{_builddir}/go/src/go.etcd.io/etcd/server/v3
    CGO_ENABLED=0 %{__go} test -short ./auth/... ./etcdserver/api/v3rpc/...
)

%ifarch riscv64
export ETCD_UNSUPPORTED_ARCH=riscv64
%endif
%{buildroot}%{_bindir}/etcd --version
%{buildroot}%{_bindir}/etcdctl version
%{buildroot}%{_bindir}/etcdutl version

%pre
%sysusers_create_package %{name} %{SOURCE2}
%tmpfiles_create_package %{name} %{SOURCE3}

%post
%systemd_post etcd.service

%preun
%systemd_preun etcd.service

%postun
%systemd_postun_with_restart etcd.service

%files
%doc README.md
%license LICENSE
%{_bindir}/etcd
%{_bindir}/etcdctl
%{_bindir}/etcdutl
%{_unitdir}/etcd.service
%{_sysusersdir}/etcd.conf
%{_tmpfilesdir}/etcd.conf
%attr(0750,etcd,etcd) %dir %{_localstatedir}/lib/etcd

%changelog
%autochangelog
