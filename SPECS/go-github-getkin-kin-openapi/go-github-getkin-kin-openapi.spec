# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kin-openapi
%define go_import_path  github.com/getkin/kin-openapi

Name:           go-github-getkin-kin-openapi
Version:        0.138.0
Release:        %autorelease
Summary:        OpenAPI 3.0 and 3.1 (and Swagger v2) implementation for Go (parsing, converting, validation, and more)
License:        MIT
URL:            https://github.com/getkin/kin-openapi
#!RemoteAsset:  sha256:d50ea27d6e644012011135f15b8876b1db561dde4721a7ab28c8e0010633fc11
Source0:        https://github.com/getkin/kin-openapi/archive/refs/tags/v0.138.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n kin-openapi-0.138.0
# These tests fetch external schemas or archives from github.com,
# raw.githubusercontent.com, schemas.sentex.io, and json-schema.org. OBS
# builders do not have network access during %check.
BuildOption(check):  -skip 'TestV2ApisGuruOpenapiDirectory|TestV3ApisGuruOpenapiDirectory|TestExtraSiblingsInRemoteRef|TestIssue495WithDraft04|TestIssue423'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/gorilla/mux)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/mohae/deepcopy)
BuildRequires:  go(github.com/oasdiff/yaml)
BuildRequires:  go(github.com/oasdiff/yaml3)
BuildRequires:  go(github.com/perimeterx/marshmallow)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/santhosh-tekuri/jsonschema/v6)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(github.com/woodsbury/decimal128)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/getkin/kin-openapi) = %{version}
Provides:       go(github.com/getkin/kin-openapi/openapi2) = %{version}
Provides:       go(github.com/getkin/kin-openapi/openapi2conv) = %{version}
Provides:       go(github.com/getkin/kin-openapi/openapi3) = %{version}
Provides:       go(github.com/getkin/kin-openapi/openapi3conv) = %{version}
Provides:       go(github.com/getkin/kin-openapi/openapi3filter) = %{version}
Provides:       go(github.com/getkin/kin-openapi/openapi3gen) = %{version}
Provides:       go(github.com/getkin/kin-openapi/openapi3gen/internal/subpkg) = %{version}
Provides:       go(github.com/getkin/kin-openapi/routers) = %{version}
Provides:       go(github.com/getkin/kin-openapi/routers/gorillamux) = %{version}
Provides:       go(github.com/getkin/kin-openapi/routers/legacy) = %{version}
Provides:       go(github.com/getkin/kin-openapi/routers/legacy/pathpattern) = %{version}

Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/gorilla/mux)
Requires:       go(github.com/josharian/intern)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/mohae/deepcopy)
Requires:       go(github.com/oasdiff/yaml)
Requires:       go(github.com/oasdiff/yaml3)
Requires:       go(github.com/perimeterx/marshmallow)
Requires:       go(github.com/santhosh-tekuri/jsonschema/v6)
Requires:       go(github.com/woodsbury/decimal128)
Requires:       go(golang.org/x/text)
Requires:       go(gopkg.in/yaml.v3)


%description
[Image: CI] (https://github.com/getkin/kin-
openapi/workflows/go/badge.svg) (https://github.com/getkin/kin-
openapi/actions) [Image: Go Report Card]
(https://goreportcard.com/badge/github.com/getkin/kin-openapi)
(https://goreportcard.com/report/github.com/getkin/kin-openapi) [Image:
GoDoc] (https://godoc.org/github.com/getkin/kin-openapi?status.svg)
(https://godoc.org/github.com/getkin/kin-openapi) [Image: Join Gitter
Chat Channel -] (https://badges.gitter.im/getkin/kin.svg)
(https://gitter.
im/getkin/kin?utm_source=badge&utm_medium=badge&utm_campaign=pr-
badge&utm_content=badge)

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
