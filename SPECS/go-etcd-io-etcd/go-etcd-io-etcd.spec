# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           etcd
%define go_import_path  go.etcd.io/etcd

Name:           go-etcd-io-etcd
Version:        3.7.1
Release:        %autorelease
Summary:        Go API and client modules for etcd
License:        Apache-2.0
URL:            https://github.com/etcd-io/etcd
#!RemoteAsset:  sha256:95352a96ffb1d92df77b5bce2bb239046fa94cd99dc839ff7eecfdc983416637
Source0:        https://github.com/etcd-io/etcd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/coreos/go-semver)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware/v2)
BuildRequires:  go(github.com/grpc-ecosystem/grpc-gateway/v2)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(%{go_import_path}/api/v3) = %{version}
Provides:       go(%{go_import_path}/client/pkg/v3) = %{version}
Provides:       go(%{go_import_path}/client/v3) = %{version}
Provides:       go(%{go_import_path}/pkg/v3) = %{version}

Requires:       go(github.com/coreos/go-semver)
Requires:       go(github.com/coreos/go-systemd/v22)
Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus)
Requires:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2)
Requires:       go(github.com/grpc-ecosystem/grpc-gateway/v2)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(sigs.k8s.io/yaml)

%description
This package bundles the etcd API, shared client utilities, and version 3 Go
client modules from the etcd repository.

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}/api/v3"
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}/client/pkg/v3"
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}/client/v3"
cp -aL api/. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/api/v3/"
cp -aL client/pkg/. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/client/pkg/v3/"
cp -aL client/v3/. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/client/v3/"

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
install -d "%{_builddir}/go/src/%{go_import_path}/api/v3"
install -d "%{_builddir}/go/src/%{go_import_path}/client/pkg/v3"
install -d "%{_builddir}/go/src/%{go_import_path}/client/v3"
install -d "%{_builddir}/go/src/%{go_import_path}/tests"
cp -aL api/. "%{_builddir}/go/src/%{go_import_path}/api/v3/"
cp -aL client/pkg/. "%{_builddir}/go/src/%{go_import_path}/client/pkg/v3/"
cp -aL client/v3/. "%{_builddir}/go/src/%{go_import_path}/client/v3/"
cp -aL tests/fixtures "%{_builddir}/go/src/%{go_import_path}/tests/"
for _module in api/v3 client/pkg/v3 client/v3; do
    pushd "%{_builddir}/go/src/%{go_import_path}/${_module}"
    go test -v $(go list -e -f '{{.ImportPath}}' ./...)
    popd
done

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
