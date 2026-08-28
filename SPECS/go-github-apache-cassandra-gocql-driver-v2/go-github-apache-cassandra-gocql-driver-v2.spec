# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cassandra-gocql-driver
%define go_import_path  github.com/apache/cassandra-gocql-driver/v2

Name:           go-github-apache-cassandra-gocql-driver-v2
Version:        2.1.2
Release:        %autorelease
Summary:        Cassandra driver for Go
License:        Apache-2.0
URL:            https://github.com/apache/cassandra-gocql-driver
#!RemoteAsset:  sha256:c5d832da5f786cf9b82fc2b0e2b7998fd8aa62bde5e44bfde64b0fe6aca6d339
Source0:        https://github.com/apache/cassandra-gocql-driver/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bitly/go-hostpool)
BuildRequires:  go(github.com/bmizerany/assert)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/hailocab/go-hostpool)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/golang/snappy)
Requires:       go(github.com/hailocab/go-hostpool)
Requires:       go(github.com/pierrec/lz4/v4)
Requires:       go(github.com/rs/zerolog)
Requires:       go(go.uber.org/zap)
Requires:       go(gopkg.in/inf.v0)

%description
The Apache Cassandra GoCQL driver implements the Cassandra wire protocol and
provides cluster discovery, connection pooling, queries, and batch operations.

%files
%doc README.md
%license LICENSE NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
