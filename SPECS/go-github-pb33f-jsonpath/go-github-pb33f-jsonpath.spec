# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonpath
%define go_import_path  github.com/pb33f/jsonpath

Name:           go-github-pb33f-jsonpath
Version:        0.8.2
Release:        %autorelease
Summary:        This is a full implementation of RFC 9535 & JSON Path Plus
License:        Apache-2.0
URL:            https://github.com/pb33f/jsonpath
#!RemoteAsset:  sha256:0fbf47e08ada6ce5e9b1b155a85fcae429c64b8dbeb6326fe915793a50813b5b
Source0:        https://github.com/pb33f/jsonpath/archive/refs/tags/v0.8.2.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n jsonpath-0.8.2
# Upstream release tarball does not include jsonpath-compliance-test-suite/cts.json,
# so this test fails before exercising package code.
BuildOption(check):  -skip TestJSONPathComplianceTestSuite

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/pmezard/go-difflib/difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/stretchr/testify/require)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/pb33f/jsonpath) = %{version}
Provides:       go(github.com/pb33f/jsonpath/pkg/jsonpath) = %{version}
Provides:       go(github.com/pb33f/jsonpath/pkg/jsonpath/config) = %{version}
Provides:       go(github.com/pb33f/jsonpath/pkg/jsonpath/token) = %{version}
Provides:       go(github.com/pb33f/jsonpath/pkg/overlay) = %{version}

Requires:       go(go.yaml.in/yaml/v4)


%description
pb33f jsonpath

[Image: Go Doc] (https://img.shields.io/badge/godoc-reference-
blue.svg?style=for-the-badge)
(https://pkg.go.dev/github.com/pb33f/jsonpath?tab=doc)

A full implementation of RFC 9535 JSONPath
(https://datatracker.ietf.org/doc/rfc9535/) with **JSONPath Plus**
extensions for enhanced querying capabilities.

This library was forked from speakeasy-api/jsonpath

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
