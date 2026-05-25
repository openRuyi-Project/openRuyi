# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonschema
%define go_import_path  github.com/santhosh-tekuri/jsonschema/v5
# The upstream release tarball does not include the JSON-Schema-Test-Suite
# submodule/testdata needed by root package tests. Nested Go modules have their
# own module path/dependencies; skip them in %check so the parent package does
# not try to test unrelated internal tools.
# - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}
    %{go_import_path}/cmd/jv*
}

Name:           go-github-santhosh-tekuri-jsonschema-v5
Version:        5.3.1
Release:        %autorelease
Summary:        JSON Schema compiler and validator for Go
License:        Apache-2.0
URL:            https://github.com/santhosh-tekuri/jsonschema
#!RemoteAsset:  sha256:9f79a056386f4cfbd616252032020ed4cfe0fd9445af9954b3d7ab8a76fe5b44
Source0:        https://github.com/santhosh-tekuri/jsonschema/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/santhosh-tekuri/jsonschema/v5) = %{version}

%description
Package jsonschema compiles and validates JSON Schema documents for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let this module own
# their source directories, otherwise RPM can hit file conflicts.
%exclude %{go_sys_gopath}/%{go_import_path}/cmd/jv

%changelog
%autochangelog
