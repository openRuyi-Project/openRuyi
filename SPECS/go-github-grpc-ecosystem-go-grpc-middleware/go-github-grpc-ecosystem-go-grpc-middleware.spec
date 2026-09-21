# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-grpc-middleware
%define go_import_path  github.com/grpc-ecosystem/go-grpc-middleware

Name:           go-github-grpc-ecosystem-go-grpc-middleware
Version:        1.4.0
Release:        %autorelease
Summary:        gRPC middleware for Go
License:        Apache-2.0
URL:            https://github.com/grpc-ecosystem/go-grpc-middleware
#!RemoteAsset:  sha256:3f99f997771775ea72edd4bd44f48bfc5c869b3f4f4107c8a45aa4635ce98ac1
Source0:        https://github.com/grpc-ecosystem/go-grpc-middleware/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-kit/log)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/opentracing/opentracing-go)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)

Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/logging/zap) = %{version}
Provides:       go(github.com/grpc-ecosystem/go-grpc-middleware/tags) = %{version}

Requires:       go(github.com/go-kit/log)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/opentracing/opentracing-go)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)

%description
go-grpc-middleware provides reusable server and client middleware for gRPC
applications.

%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}
# The two upstream testproto generators share the historical protobuf name.
# Keep the complete test suite and use protobuf's documented compatibility mode.
export GOLANG_PROTOBUF_REGISTRATION_CONFLICT=warn
# Go 1.26 vet rejects upstream's historical non-constant logging formats.
go test -v -vet=off ./...

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
