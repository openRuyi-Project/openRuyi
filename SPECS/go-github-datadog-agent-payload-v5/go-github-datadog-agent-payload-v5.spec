# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           agent-payload
%define go_import_path  github.com/DataDog/agent-payload/v5

Name:           go-github-datadog-agent-payload-v5
Version:        5.0.209
Release:        %autorelease
Summary:        Datadog Agent payload definitions and generated bindings
License:        BSD-3-Clause
URL:            https://github.com/DataDog/agent-payload
#!RemoteAsset:  sha256:51eccbb260c698334df9f29ddc4ff9ccf1dbbceac835a757017bca3068d9f46d
Source0:        https://github.com/DataDog/agent-payload/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/DataDog/mmh3)
BuildRequires:  go(github.com/DataDog/zstd)
BuildRequires:  go(github.com/chrusty/protoc-gen-jsonschema)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/DataDog/mmh3)
Requires:       go(github.com/DataDog/zstd)
Requires:       go(github.com/chrusty/protoc-gen-jsonschema)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/yaml.v3)

%description
Agent-payload contains protocol-buffer definitions and generated Go bindings
used for communication between the Datadog Agent and Datadog backends.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
