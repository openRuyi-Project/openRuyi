# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-grpc-middleware
%define go_import_path  github.com/grpc-ecosystem/go-grpc-middleware/v2

Name:           go-github-grpc-ecosystem-go-grpc-middleware-v2
Version:        2.3.4
Release:        %autorelease
Summary:        Middleware and Prometheus interceptors for Go gRPC
License:        Apache-2.0
URL:            https://github.com/grpc-ecosystem/go-grpc-middleware
#!RemoteAsset:  sha256:c0b837e6062f5e7fc289b34c68f133a76760bde82b190361c2c5fe64b520f62f
Source0:        https://github.com/grpc-ecosystem/go-grpc-middleware/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go)
BuildRequires:  go(buf.build/go/protovalidate)
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/antlr4-go/antlr/v4)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-kit/log)
BuildRequires:  go(github.com/go-logfmt/logfmt)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/cel-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/matttproud/golang_protobuf_extensions)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/oklog/run)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stoewer/go-strcase)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/oauth2/google)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/examples/v2) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/interceptors/logging/examples) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/auth) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/logging) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/protovalidate) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/ratelimit) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/realip) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/recovery) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/retry) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/selector) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/timeout) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/interceptors/validator) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/metadata) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/testing/testpb) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/testing/testvalidate) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/testing/testvalidate/v1) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/v2/util/backoffutils) = %{version}

Requires:       go(buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go)
Requires:       go(buf.build/go/protovalidate)
Requires:       go(github.com/oklog/run)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/exporters/stdout/stdouttrace)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/oauth2/google)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package bundles the version 2 gRPC middleware module and its Prometheus
metrics provider module from the same upstream repository.

%install
# Install each module at its declared import path. Remove nested module
# copies from each parent before installing them at their own paths.
while read -r _source _import _children; do
    _target="%{buildroot}%{go_sys_gopath}/${_import}"
    install -d "${_target}"
    cp -aL "${_source}"/. "${_target}/"
    for _child in ${_children}; do
        rm -rf "${_target}/${_child}"
    done
done <<'GO_MODULES'
. github.com/grpc-ecosystem/go-grpc-middleware/v2 examples providers/prometheus interceptors/logging/examples
examples github.com/grpc-ecosystem/go-grpc-middleware/examples/v2
providers/prometheus github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus
interceptors/logging/examples github.com/grpc-ecosystem/go-grpc-middleware/interceptors/logging/examples
GO_MODULES

%check
%go_common
# Test the installed layout, including nested modules, without loading a
# second copy of the repository or using the system's older source package.
install -d "%{_builddir}/go/src"
cp -a "%{buildroot}%{go_sys_gopath}/." "%{_builddir}/go/src/"
_go_packages=$(go list -e -f '{{.ImportPath}}' github.com/grpc-ecosystem/go-grpc-middleware/...)
_go_packages=$(printf '%s\n' "${_go_packages}" | sort -u)
_go_tests=
set -f
for _package in ${_go_packages}; do
    _skip=0
    for _exclude in %{?go_test_exclude}; do
        if [ "${_package}" = "${_exclude}" ]; then _skip=1; fi
    done
    for _exclude in %{?go_test_exclude_glob}; do
        case "${_package}" in ${_exclude}) _skip=1 ;; esac
    done
    [ "${_skip}" -eq 1 ] || _go_tests="${_go_tests} ${_package}"
done
set +f
test -n "${_go_tests}"
go test %{go_test_flags_default}  ${_go_tests}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/grpc-ecosystem/go-grpc-middleware

%changelog
%autochangelog
