# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonschema
%define go_import_path  github.com/santhosh-tekuri/jsonschema/v6

Name:           go-github-santhosh-tekuri-jsonschema-v6
Version:        6.0.2
Release:        %autorelease
Summary:        JSONSchema (draft 2020-12, draft 2019-09, draft-7, draft-6, draft-4) Validation using Go
License:        Apache-2.0
URL:            https://github.com/santhosh-tekuri/jsonschema
#!RemoteAsset:  sha256:06465cc1c647b086f9b8d590c9de1608e5b335b58598d0eb84b9ee63a747e1d7
Source0:        https://github.com/santhosh-tekuri/jsonschema/archive/refs/tags/v6.0.2.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n jsonschema-6.0.2
# Example_fromHTTPS fetches raw.githubusercontent.com; OBS builders do not have
# network access during %check, so skip only this external-network example.
BuildOption(check):  -skip Example_fromHTTPS
# Nested Go modules have their own module path/dependencies; skip them in %check
# so the parent package does not try to test unrelated internal tools.
%define go_test_exclude_glob %{go_import_path}/cmd/jv*

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/text/language)
BuildRequires:  go(golang.org/x/text/message)

Provides:       go(github.com/santhosh-tekuri/jsonschema/v6) = %{version}
Provides:       go(github.com/santhosh-tekuri/jsonschema/v6/kind) = %{version}

Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/text/language)
Requires:       go(golang.org/x/text/message)


%description
jsonschema v6.0.2

[Image: License] (https://img.shields.io/badge/License-Apache%202.0-
blue.svg) (https://opensource.org/licenses/Apache-2.0) [Image: GoDoc]
(https://godoc.org/github.com/santhosh-tekuri/jsonschema?status.svg)
(https://pkg.go.dev/github.com/santhosh-tekuri/jsonschema/v6) [Image: Go
Report Card] (https://goreportcard.com/badge/github.com/santhosh-
tekuri/jsonschema/v6)
(https://goreportcard.com/report/github.com/santhosh-
tekuri/jsonschema/v6) [Image: Build Status] (https://github.com/santhosh-
tekuri/jsonschema/actions/workflows/go.yaml/badge.svg?branch=boon)

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
# Nested Go modules are packaged separately; do not let this module own
# their source directories, otherwise RPM can hit file conflicts.
%exclude %{go_sys_gopath}/%{go_import_path}/cmd/jv

%changelog
%autochangelog
