# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           analysis
%define go_import_path  github.com/go-openapi/analysis

Name:           go-github-go-openapi-analysis
Version:        0.25.0
Release:        %autorelease
Summary:        OpenAPI 2.0 specification analysis toolkit
License:        Apache-2.0
URL:            https://github.com/go-openapi/analysis
#!RemoteAsset:  sha256:d510d6b98d916668e6deebfa9f61afe284384240603fc0bae7044eae19c979e2
Source0:        https://github.com/go-openapi/analysis/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The patched test fetches a remote CloudEvents fixture unless explicitly enabled.
# https://github.com/go-openapi/analysis/pull/222
Patch2000:      2000-tests-require-opt-in-for-remote-fixture.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/spec)
BuildRequires:  go(github.com/go-openapi/strfmt)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/testify/v2)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/go-openapi/analysis) = %{version}

Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/go-openapi/spec)
Requires:       go(github.com/go-openapi/strfmt)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(golang.org/x/text)

%description
Analysis provides tools to inspect, flatten, merge, compare, and repair
OpenAPI 2.0 specification documents.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
