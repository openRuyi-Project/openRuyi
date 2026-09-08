# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-grpc-middleware
%define go_import_path  github.com/grpc-ecosystem/go-grpc-middleware

Name:           go-github-grpc-ecosystem-go-grpc-middleware-v2
Version:        2.3.3
Release:        %autorelease
Summary:        Middleware and Prometheus interceptors for Go gRPC
License:        Apache-2.0
URL:            https://github.com/grpc-ecosystem/go-grpc-middleware
#!RemoteAsset:  sha256:653cae72dbba078a04eb6eda0e8b330b3832a5794af28829c32a965aa26a29d0
Source0:        https://github.com/grpc-ecosystem/go-grpc-middleware/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go)
BuildRequires:  go(buf.build/go/protovalidate)
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/antlr4-go/antlr/v4)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/cel-go)
BuildRequires:  go(github.com/matttproud/golang_protobuf_extensions)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/stoewer/go-strcase)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}/providers/prometheus) = %{version}
Provides:       go(%{go_import_path}/v2) = %{version}

Requires:       go(buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go)
Requires:       go(buf.build/go/protovalidate)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package bundles the version 2 gRPC middleware module and its Prometheus
metrics provider module from the same upstream repository.

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}/v2"
cp -a ./. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/v2/"
rm -rf "%{buildroot}%{go_sys_gopath}/%{go_import_path}/v2/.bingo"
rm -rf "%{buildroot}%{go_sys_gopath}/%{go_import_path}/v2/examples"
rm -rf "%{buildroot}%{go_sys_gopath}/%{go_import_path}/v2/interceptors/logging/examples"
rm -rf "%{buildroot}%{go_sys_gopath}/%{go_import_path}/v2/providers"
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}/providers/prometheus"
cp -a providers/prometheus/. \
    "%{buildroot}%{go_sys_gopath}/%{go_import_path}/providers/prometheus/"

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
install -d "%{_builddir}/go/src/%{go_import_path}"
cp -a "%{buildroot}%{go_sys_gopath}/%{go_import_path}/." \
    "%{_builddir}/go/src/%{go_import_path}/"
for _module in v2 providers/prometheus; do
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
