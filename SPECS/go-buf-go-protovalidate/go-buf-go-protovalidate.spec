# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           protovalidate
%define go_import_path  buf.build/go/protovalidate
# Root test mocks target the older CEL Program interface without ConcurrentEval.
%define go_test_exclude %{go_import_path}

Name:           go-buf-go-protovalidate
Version:        0.12.0
Release:        %autorelease
Summary:        Semantic validation library for protocol buffers
License:        Apache-2.0
URL:            https://github.com/bufbuild/protovalidate-go
#!RemoteAsset:  sha256:4688d211e7e866bdd7f9566e9d3bb43d99574c4d44bc74e8af636da08809def0
Source0:        https://github.com/bufbuild/protovalidate-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go)
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(github.com/antlr4-go/antlr/v4)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/google/cel-go)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stoewer/go-strcase)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go)
Requires:       go(github.com/google/cel-go)
Requires:       go(google.golang.org/protobuf)

%description
Protovalidate provides semantic validation for protocol buffer messages using
standard annotations and custom Common Expression Language rules.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
