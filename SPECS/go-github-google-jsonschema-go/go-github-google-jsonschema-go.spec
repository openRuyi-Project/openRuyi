# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonschema-go
%define go_import_path  github.com/google/jsonschema-go

Name:           go-github-google-jsonschema-go
Version:        0.4.3
Release:        %autorelease
Summary:        JSON Schema implementation for Go
License:        MIT
URL:            https://github.com/google/jsonschema-go
VCS:            git:https://github.com/google/jsonschema-go.git
#!RemoteAsset:  sha256:de9198fe0050ea4306c0a362fabc69be46373290160d416d2ce5627f460ea4e5
Source0:        https://github.com/google/jsonschema-go/archive/refs/tags/v%{version}.tar.gz#/jsonschema-go-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n jsonschema-go-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
# go-cmp is used only by the test suite.
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(github.com/google/jsonschema-go) = %{version}

%description
Jsonschema-go provides JSON Schema types, resolution, validation, and related
utilities for Go programs.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
