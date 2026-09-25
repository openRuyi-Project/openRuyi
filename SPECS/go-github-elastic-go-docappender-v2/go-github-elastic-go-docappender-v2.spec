# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-docappender
%define go_import_path  github.com/elastic/go-docappender/v2

Name:           go-github-elastic-go-docappender-v2
Version:        2.14.1
Release:        %autorelease
Summary:        Append-only bulk document indexing library for Elasticsearch
License:        Apache-2.0
URL:            https://github.com/elastic/go-docappender
#!RemoteAsset:  sha256:db081accfe61086bf29e620b4b7289bcb5cc33e64c4f72c5d498a4ab889684e9
Source0:        https://github.com/elastic/go-docappender/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/elastic/elastic-transport-go/v8)
BuildRequires:  go(github.com/elastic/go-elasticsearch/v7)
BuildRequires:  go(github.com/elastic/go-elasticsearch/v8)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.elastic.co/fastjson)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/elastic/elastic-transport-go/v8)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.elastic.co/fastjson)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/sync)

%description
Go-docappender provides an asynchronous Go API for append-only bulk document
indexing into Elasticsearch.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
