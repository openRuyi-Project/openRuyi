# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-control-plane
%define go_import_path  github.com/envoyproxy/go-control-plane

Name:           go-github-envoyproxy-go-control-plane
Version:        0.14.0
Release:        %autorelease
Summary:        Envoy control plane library for Go
License:        Apache-2.0
URL:            https://github.com/envoyproxy/go-control-plane
#!RemoteAsset:  sha256:f5973fcd5e93ff7e061ea4f0f21248a0df537f4cf87040ca94993a83f150ed25
Source0:        https://github.com/envoyproxy/go-control-plane/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 vet rejects status.Errorf with a non-constant format string.
Patch0:         2000-fix-non-constant-status-errorf.patch

BuildOption(prep):  -n go-control-plane-0.14.0
# The upstream repository contains nested Go modules. The root module uses local
# replace directives for them, so testing sibling modules here would create a
# bootstrap cycle with the separately packaged envoy/ratelimit modules.
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/contrib*
    %{go_import_path}/envoy*
    %{go_import_path}/examples*
    %{go_import_path}/internal/tools*
    %{go_import_path}/ratelimit*
    %{go_import_path}/xdsmatcher*
}

BuildRequires:  go
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/planetscale/vtprotobuf)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prometheus/client_model/go)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/proto/otlp/common/v1)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/envoyproxy/go-control-plane) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/internal/example) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/cache/types) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/cache/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/client/sotw/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/conversion) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/integration) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/log) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/resource/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/server/config) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/server/delta/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/server/rest/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/server/sotw/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/server/stream/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/server/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/test) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/test/resource/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/test/v3) = %{version}
Provides:       go(github.com/envoyproxy/go-control-plane/pkg/wellknown) = %{version}

Requires:       go(cel.dev/expr)
Requires:       go(github.com/cncf/xds/go)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/planetscale/vtprotobuf)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/prometheus/client_model/go)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.opentelemetry.io/proto/otlp/common/v1)
Requires:       go(go.uber.org/goleak)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/check.v1)
Requires:       go(gopkg.in/yaml.v3)

%description
This package provides Envoy control plane library for Go.

# The upstream repository vendors envoy and ratelimit as nested Go modules.
# They are packaged separately, so the root package must not own their source
# trees or provide their import paths.
%install -a
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/envoy \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/ratelimit

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
