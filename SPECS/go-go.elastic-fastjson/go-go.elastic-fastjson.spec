# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fastjson
%define go_import_path  go.elastic.co/fastjson

Name:           go-go.elastic-fastjson
Version:        1.5.1
Release:        %autorelease
Summary:        Fast JSON encoder and code generator for Go
License:        Apache-2.0 AND MIT
URL:            https://github.com/elastic/go-fastjson
#!RemoteAsset:  sha256:932b5327252f092ffe36a639115971e4a2e2067686b6d6aecaea2f2ae94935ec
Source0:        https://github.com/elastic/go-fastjson/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.27 formats the Marshaler type in encoding/json errors as a pointer.
Patch0:         2000-tolerate-go1.27-json-error-type.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/tools)

%description
Fastjson provides a fast JSON encoding library and a generator for producing
marshalling methods for exported Go types.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
