# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           datadog-api-client-go
%define go_import_path  github.com/DataDog/datadog-api-client-go/v2
# Generated example directories contain multiple standalone main programs.
%define go_test_exclude_glob %{go_import_path}/examples*

Name:           go-github-datadog-datadog-api-client-go-v2
Version:        2.64.0
Release:        %autorelease
Summary:        Datadog API client for Go
License:        Apache-2.0
URL:            https://github.com/DataDog/datadog-api-client-go
#!RemoteAsset:  sha256:248c06fd286a5bd0cc9410492eb38a8fc9972e4fd6cd092ed9c56d9ad99d92ff
Source0:        https://github.com/DataDog/datadog-api-client-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/DataDog/datadog-go)
BuildRequires:  go(github.com/DataDog/dd-sdk-go-testing)
BuildRequires:  go(github.com/DataDog/sketches-go)
BuildRequires:  go(github.com/DataDog/zstd)
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/cucumber/gherkin-go/v13)
BuildRequires:  go(github.com/cucumber/messages-go/v12)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-bdd/gobdd)
BuildRequires:  go(github.com/goccy/go-json)
BuildRequires:  go(github.com/gofrs/uuid)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/mock)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/h2non/parth)
BuildRequires:  go(github.com/jonboulle/clockwork)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/opentracing/opentracing-go)
BuildRequires:  go(github.com/philhofer/fwd)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tinylib/msgp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(google.golang.org/appengine)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/DataDog/dd-trace-go.v1)
BuildRequires:  go(gopkg.in/dnaeon/go-vcr.v3)
BuildRequires:  go(gopkg.in/h2non/gock.v1)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(gotest.tools)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/DataDog/zstd)
Requires:       go(github.com/goccy/go-json)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/uuid)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(google.golang.org/appengine)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the generated Go clients and shared types for Datadog
API v1 and v2 endpoints.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
