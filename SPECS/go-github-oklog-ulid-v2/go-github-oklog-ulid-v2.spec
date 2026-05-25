# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ulid
%define go_import_path  github.com/oklog/ulid/v2

Name:           go-github-oklog-ulid-v2
Version:        2.1.1
Release:        %autorelease
Summary:        Universally Unique Lexicographically Sortable Identifier (ULID) in Go
License:        Apache-2.0
URL:            https://github.com/oklog/ulid
#!RemoteAsset:  sha256:0f9bc214b2da681b839a1c0aea827613ed818d3e19234065fc1f15c4cd569185
Source0:        https://github.com/oklog/ulid/archive/refs/tags/v2.1.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n ulid-2.1.1

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pborman/getopt)
BuildRequires:  go(github.com/pborman/getopt/v2)

Provides:       go(github.com/oklog/ulid/v2) = %{version}

Requires:       go(github.com/pborman/getopt)
Requires:       go(github.com/pborman/getopt/v2)


%description
Universally Unique Lexicographically Sortable Identifier

[Image: Project status]
(https://img.shields.io/github/release/oklog/ulid.svg?style=flat-square)
(https://github.com/oklog/ulid/releases/latest) [Image: Build Status]
(https://github.com/oklog/ulid/actions/workflows/test.yml/badge.svg)
[Image: Go Report Card]
(https://goreportcard.com/badge/oklog/ulid?cache=0)
(https://goreportcard.com/report/oklog/ulid) [Image: Coverage Status]
(https://coveralls.io/repos/github/oklog/ulid/badge.
svg?branch=master&cache=0)

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
