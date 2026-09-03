# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           puddle
%define go_import_path  github.com/jackc/puddle/v2

Name:           go-github-jackc-puddle-v2
Version:        2.2.2
Release:        %autorelease
Summary:        Generic resource pool for Go
License:        MIT
URL:            https://github.com/jackc/puddle
#!RemoteAsset:  sha256:15615ff760c55a7024d362fccbbf75646e20235472ab24c8ef94792876f196eb
Source0:        https://github.com/jackc/puddle/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/sync)

%description
Puddle implements a generic, concurrency-safe resource pool with acquisition,
idle cleanup, lifetime limits, and statistics.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
