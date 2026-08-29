# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonschema
%define go_import_path  github.com/invopop/jsonschema

Name:           go-github-invopop-jsonschema
Version:        0.14.0
Release:        %autorelease
Summary:        Generate JSON Schemas from Go types
License:        MIT
URL:            https://github.com/invopop/jsonschema
#!RemoteAsset:  sha256:8b2d7d5fbdfcefe30d368bd7ae081570fc358980a8807d8fffe18cdd6e2a742f
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pb33f/ordered-map/v2)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/invopop/jsonschema) = %{version}

Requires:       go(github.com/pb33f/ordered-map/v2)
Requires:       go(github.com/stretchr/testify)

%description
This package can be used to generate JSON Schemas from Go types through reflection.

 * Supports arbitrarily complex types, including interface{}, maps, slices, etc.
 * Supports json-schema features such as minLength, maxLength, pattern, format, etc.
 * Supports simple string and numeric enums.
 * Supports custom property fields via the jsonschema_extras struct tag.

%files
%doc README*
%license COPYING*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
