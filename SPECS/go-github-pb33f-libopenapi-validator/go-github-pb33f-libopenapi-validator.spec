# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           libopenapi-validator
%define go_import_path  github.com/pb33f/libopenapi-validator

Name:           go-github-pb33f-libopenapi-validator
Version:        0.14.0
Release:        %autorelease
Summary:        OpenAPI validation library for Go
License:        MIT
URL:            https://github.com/pb33f/libopenapi-validator
#!RemoteAsset:  sha256:3c18537872bb2a996e992d2ae46dc855203b774009f1100d15a3e95b275cbab9
Source0:        https://github.com/pb33f/libopenapi-validator/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep schema-loading tests offline by directing them to their mock servers.
# https://github.com/pb33f/libopenapi-validator/pull/311
Patch2000:      2000-tests-use-mock-servers-for-schema-loading.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/basgys/goxml2json)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/goccy/go-yaml)
BuildRequires:  go(github.com/pb33f/jsonpath)
BuildRequires:  go(github.com/pb33f/libopenapi)
BuildRequires:  go(github.com/pb33f/testify)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/pb33f/libopenapi-validator) = %{version}

Requires:       go(github.com/basgys/goxml2json)
Requires:       go(github.com/dlclark/regexp2)
Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/goccy/go-yaml)
Requires:       go(github.com/pb33f/jsonpath)
Requires:       go(github.com/pb33f/libopenapi)
Requires:       go(github.com/santhosh-tekuri/jsonschema/v6)
Requires:       go(go.yaml.in/yaml/v4)
Requires:       go(golang.org/x/text)

%description
Libopenapi-validator validates OpenAPI 3.x documents, HTTP requests and
responses, parameters, and JSON Schema content.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
