# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           libopenapi
%define go_import_path  github.com/pb33f/libopenapi

Name:           go-github-pb33f-libopenapi
Version:        0.38.7
Release:        %autorelease
Summary:        OpenAPI document model and tooling for Go
License:        MIT
URL:            https://github.com/pb33f/libopenapi
#!RemoteAsset:  sha256:3593cfae3e33ef344773055681a673d10f41bb1ea170f0993b23a9989607a9dc
Source0:        https://github.com/pb33f/libopenapi/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Preserve unit tests while requiring explicit opt-in for remote fixtures.
# https://github.com/pb33f/libopenapi/pull/609
Patch2000:      2000-tests-require-opt-in-for-remote-fixtures.patch
# Generator tests place temporary programs in an isolated GOPATH when the
# package build disables module mode, keeping all dependencies offline.
# https://github.com/pb33f/libopenapi/pull/610
Patch2001:      2001-generator-support-temporary-modules-in-GOPATH-builds.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/lucasjones/reggen)
BuildRequires:  go(github.com/pb33f/jsonpath)
BuildRequires:  go(github.com/pb33f/ordered-map/v2)
BuildRequires:  go(github.com/pb33f/testify)
BuildRequires:  go(go.yaml.in/yaml/v4)
BuildRequires:  go(golang.org/x/sync)

Provides:       go(github.com/pb33f/libopenapi) = %{version}

Requires:       go(github.com/lucasjones/reggen)
Requires:       go(github.com/pb33f/jsonpath)
Requires:       go(github.com/pb33f/ordered-map/v2)
Requires:       go(go.yaml.in/yaml/v4)
Requires:       go(golang.org/x/sync)

%description
Libopenapi reads, manipulates, compares, bundles, validates, generates, and
renders OpenAPI 2.0, 3.x, Overlay, and Arazzo documents.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
