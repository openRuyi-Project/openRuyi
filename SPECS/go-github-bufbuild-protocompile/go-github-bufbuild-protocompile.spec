# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protocompile
%define go_import_path  github.com/bufbuild/protocompile

Name:           go-github-bufbuild-protocompile
Version:        0.14.1
Release:        %autorelease
Summary:        A parsing/linking engine for protobuf; the guts for a pure Go replacement of protoc.
License:        Apache-2.0
URL:            https://github.com/bufbuild/protocompile
#!RemoteAsset:  sha256:321593b96692d8a821a205d75340c69cf187dfbd59ba146ed50957a3dfe214ef
Source0:        https://github.com/bufbuild/protocompile/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n protocompile-0.14.1
# internal/tools is only used by upstream generate/lint targets, and
# internal/benchmarks depends on the predecessor parser for comparisons.
# linker tests require upstream's generated ../.tmp/cache/protoc/27.0/bin/protoc
# from `make protoc`; the remaining packages still run their normal Go tests.
%define go_test_exclude_glob %{shrink:
    github.com/bufbuild/protocompile/internal/tools
    github.com/bufbuild/protocompile/internal/benchmarks
    github.com/bufbuild/protocompile/linker
    github.com/bufbuild/protocompile/parser
}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sync/errgroup)
BuildRequires:  go(golang.org/x/sync/semaphore)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(google.golang.org/protobuf/encoding/prototext)
BuildRequires:  go(google.golang.org/protobuf/proto)
BuildRequires:  go(google.golang.org/protobuf/reflect/protodesc)
BuildRequires:  go(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  go(google.golang.org/protobuf/reflect/protoregistry)
BuildRequires:  go(google.golang.org/protobuf/testing/protocmp)
BuildRequires:  go(google.golang.org/protobuf/types/descriptorpb)
BuildRequires:  go(google.golang.org/protobuf/types/dynamicpb)
BuildRequires:  go(google.golang.org/protobuf/types/gofeaturespb)
BuildRequires:  go(google.golang.org/protobuf/types/known/anypb)
BuildRequires:  go(google.golang.org/protobuf/types/known/apipb)
BuildRequires:  go(google.golang.org/protobuf/types/known/durationpb)
BuildRequires:  go(google.golang.org/protobuf/types/known/emptypb)
BuildRequires:  go(google.golang.org/protobuf/types/known/fieldmaskpb)
BuildRequires:  go(google.golang.org/protobuf/types/known/sourcecontextpb)
BuildRequires:  go(google.golang.org/protobuf/types/known/structpb)
BuildRequires:  go(google.golang.org/protobuf/types/known/timestamppb)
BuildRequires:  go(google.golang.org/protobuf/types/known/typepb)
BuildRequires:  go(google.golang.org/protobuf/types/known/wrapperspb)
BuildRequires:  go(google.golang.org/protobuf/types/pluginpb)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/bufbuild/protocompile) = %{version}
Provides:       go(github.com/bufbuild/protocompile/ast) = %{version}
Provides:       go(github.com/bufbuild/protocompile/internal) = %{version}
Provides:       go(github.com/bufbuild/protocompile/internal/benchmarks) = %{version}
Provides:       go(github.com/bufbuild/protocompile/internal/editions) = %{version}
Provides:       go(github.com/bufbuild/protocompile/internal/featuresext) = %{version}
Provides:       go(github.com/bufbuild/protocompile/internal/messageset) = %{version}
Provides:       go(github.com/bufbuild/protocompile/internal/protoc) = %{version}
Provides:       go(github.com/bufbuild/protocompile/internal/prototest) = %{version}
Provides:       go(github.com/bufbuild/protocompile/linker) = %{version}
Provides:       go(github.com/bufbuild/protocompile/options) = %{version}
Provides:       go(github.com/bufbuild/protocompile/parser) = %{version}
Provides:       go(github.com/bufbuild/protocompile/parser/fastscan) = %{version}
Provides:       go(github.com/bufbuild/protocompile/protoutil) = %{version}
Provides:       go(github.com/bufbuild/protocompile/reporter) = %{version}
Provides:       go(github.com/bufbuild/protocompile/sourceinfo) = %{version}
Provides:       go(github.com/bufbuild/protocompile/walk) = %{version}
Provides:       go(github.com/bufbuild/protocompile/wellknownimports) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-cmp/cmp)
Requires:       go(github.com/google/go-cmp/cmp/cmpopts)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/stretchr/testify/require)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sync/semaphore)
Requires:       go(google.golang.org/protobuf)
Requires:       go(google.golang.org/protobuf/encoding/prototext)
Requires:       go(google.golang.org/protobuf/proto)
Requires:       go(google.golang.org/protobuf/reflect/protodesc)
Requires:       go(google.golang.org/protobuf/reflect/protoreflect)
Requires:       go(google.golang.org/protobuf/reflect/protoregistry)
Requires:       go(google.golang.org/protobuf/testing/protocmp)
Requires:       go(google.golang.org/protobuf/types/descriptorpb)
Requires:       go(google.golang.org/protobuf/types/dynamicpb)
Requires:       go(google.golang.org/protobuf/types/gofeaturespb)
Requires:       go(google.golang.org/protobuf/types/known/anypb)
Requires:       go(google.golang.org/protobuf/types/known/apipb)
Requires:       go(google.golang.org/protobuf/types/known/durationpb)
Requires:       go(google.golang.org/protobuf/types/known/emptypb)
Requires:       go(google.golang.org/protobuf/types/known/fieldmaskpb)
Requires:       go(google.golang.org/protobuf/types/known/sourcecontextpb)
Requires:       go(google.golang.org/protobuf/types/known/structpb)
Requires:       go(google.golang.org/protobuf/types/known/timestamppb)
Requires:       go(google.golang.org/protobuf/types/known/typepb)
Requires:       go(google.golang.org/protobuf/types/known/wrapperspb)
Requires:       go(google.golang.org/protobuf/types/pluginpb)
Requires:       go(gopkg.in/yaml.v3)


%description
[Image: The Buf logo] (/.github/buf-logo.svg)

Protocompile

[Image: Build]
(https://github.com/bufbuild/protocompile/actions/workflows/ci.
yaml/badge.svg?branch=main)
(https://github.com/bufbuild/protocompile/actions/workflows/ci.yaml)
[Image: Report Card]
(https://goreportcard.com/badge/github.com/bufbuild/protocompile)
(https://goreportcard.com/report/github.com/bufbuild/protocompile)

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
