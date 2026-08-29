# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           loads
%define go_import_path  github.com/go-openapi/loads

Name:           go-github-go-openapi-loads
Version:        0.23.3
Release:        %autorelease
Summary:        OpenAPI 2.0 specification document loader
License:        Apache-2.0
URL:            https://github.com/go-openapi/loads
#!RemoteAsset:  sha256:c7c8aa0f60e043bf0fcfc20cb4b04d0233ee3bb40d12f53b00d03591316aab01
Source0:        https://github.com/go-openapi/loads/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-openapi/analysis)
BuildRequires:  go(github.com/go-openapi/spec)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/testify/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(github.com/go-openapi/loads) = %{version}

Requires:       go(github.com/go-openapi/analysis)
Requires:       go(github.com/go-openapi/spec)
Requires:       go(github.com/go-openapi/swag)

%description
Loads reads OpenAPI 2.0 documents from local or remote locations and supports
JSON, YAML, reference resolution, and restricted loading.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
