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
Source0:        https://github.com/oklog/ulid/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pborman/getopt/v2)

Provides:       go(github.com/oklog/ulid/v2) = %{version}

Requires:       go(github.com/pborman/getopt/v2)

%description
Universally Unique Lexicographically Sortable Identifier

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
