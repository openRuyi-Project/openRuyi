# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           treemap
%define go_import_path  github.com/igrmk/treemap/v2
%define commit_id c69857c24f535143274e79c5a97b79be605d4cea

Name:           go-github-igrmk-treemap-v2
Version:        0+git20220322.c69857c
Release:        %autorelease
Summary:        Generic sorted map for Go with red-black tree under the hood
License:        Unlicense
URL:            https://github.com/igrmk/treemap
#!RemoteAsset:  sha256:c56f59ffe220d35566edd4217779d952140866ea3c60d6c566a5cbe0d3c751ac
Source0:        https://github.com/igrmk/treemap/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}
# The repository keeps the v2 Go module in the v2/ subdirectory; checking only
# that module avoids testing the repository root, which intentionally has no Go files.
%define go_test_include github.com/igrmk/treemap/v2

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/exp/constraints)

Provides:       go(github.com/igrmk/treemap/v2) = %{version}
Provides:       go(github.com/igrmk/treemap/v2/example) = %{version}

Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/exp/constraints)


%description
TreeMap v2

[Image: PkgGoDev] (https://pkg.go.dev/badge/github.com/igrmk/treemap/v2)
(https://pkg.go.dev/github.com/igrmk/treemap/v2) [Image: Unlicense]
(https://img.shields.io/badge/license-Unlicense-brightgreen.svg)
(http://unlicense.org/) [Image: Build Status] (https://api.travis-
ci.com/igrmk/treemap.svg?branch=master) (https://app.travis-
ci.com/github/igrmk/treemap) [Image: Coverage Status]
(https://coveralls.io/repos/igrmk/treemap/badge.svg?branch=master)
(https://coveralls.io/github/igrmk/treemap) [Image: GoReportCard]
(https://goreportcard.com/badge/github.com/igrmk/treemap/v2)

%files
%license LICENSE
%{go_sys_gopath}/github.com/igrmk/treemap

%changelog
%autochangelog
