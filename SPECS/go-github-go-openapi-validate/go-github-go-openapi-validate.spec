# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           validate
%define go_import_path  github.com/go-openapi/validate

Name:           go-github-go-openapi-validate
Version:        0.25.2
Release:        %autorelease
Summary:        OpenAPI 2.0 and JSON Schema validation toolkit
License:        Apache-2.0
URL:            https://github.com/go-openapi/validate
#!RemoteAsset:  sha256:af3d105d584acc9c2516b385c59c30b306677d391cde3e97d65a8613fde39c29
Source0:        https://github.com/go-openapi/validate/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Start the local JSON Schema fixture server before parallel clients run.
# https://github.com/go-openapi/validate/pull/273
Patch1000:      1000-tests-wait-for-the-local-fixture-server.patch
# Keep documentation examples deterministic in offline build environments.
# https://github.com/go-openapi/validate/pull/273
Patch1001:      1001-use-bundled-petstore-example-fixture.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-openapi/analysis)
BuildRequires:  go(github.com/go-openapi/errors)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/loads)
BuildRequires:  go(github.com/go-openapi/spec)
BuildRequires:  go(github.com/go-openapi/strfmt)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/testify/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(github.com/go-openapi/validate) = %{version}

Requires:       go(github.com/go-openapi/analysis)
Requires:       go(github.com/go-openapi/errors)
Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/go-openapi/loads)
Requires:       go(github.com/go-openapi/spec)
Requires:       go(github.com/go-openapi/strfmt)
Requires:       go(github.com/go-openapi/swag)

%description
Validate checks OpenAPI 2.0 documents and JSON Schema Draft 4 values, formats,
arrays, objects, and parameters.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
