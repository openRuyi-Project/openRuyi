# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jaeger-idl
%define go_import_path  github.com/jaegertracing/jaeger-idl

Name:           go-github-jaegertracing-jaeger-idl
Version:        0.11.0
Release:        %autorelease
Summary:        Shared Thrift and Protocol Buffer definitions for Jaeger
License:        Apache-2.0
URL:            https://github.com/jaegertracing/jaeger-idl
#!RemoteAsset:  sha256:f55b77c90c825824f4feddc4e0b134e138c6dc1f3b8321bef5af8a79eb73d6f6
Source0:        https://github.com/jaegertracing/jaeger-idl/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/apache/thrift)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/gogo/googleapis)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/apache/thrift)
Requires:       go(github.com/gogo/googleapis)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
Jaeger IDL provides shared Thrift and Protocol Buffer definitions and their Go
implementations for Jaeger components.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
