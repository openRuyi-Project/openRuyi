# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           etcd
%define go_import_path  go.etcd.io/etcd/v3
%define git_sha         fc04cf702b0a46c2fd85547a2be05705b100a496

Name:           etcd
Version:        3.6.14
Release:        %autorelease
Summary:        Distributed reliable key-value store
License:        Apache-2.0
URL:            https://github.com/etcd-io/etcd
#!RemoteAsset:  sha256:a7ac1ed4192c6e53e4716df3e08bc75e4f929fcb186a9d9e5b0aaf11c96b067a
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        etcd.service
Source2:        etcd.sysusers
Source3:        etcd.tmpfiles

BuildRequires:  go >= 1.25
BuildRequires:  go-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  go(github.com/VividCortex/ewma)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/bgentry/speakeasy)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cheggaaa/pb/v3)
BuildRequires:  go(github.com/coreos/go-semver)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/btree)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware/v2)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/jonboulle/clockwork)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/olekukonko/tablewriter)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/soheilhy/cmux)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/tmc/grpc-websocket-proxy)
BuildRequires:  go(github.com/xiang90/probing)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(go.etcd.io/raft/v3) = 3.6.0
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.opentelemetry.io/proto/otlp)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  go(sigs.k8s.io/json)
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
