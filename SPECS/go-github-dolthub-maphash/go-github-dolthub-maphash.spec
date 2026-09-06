# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           maphash
%define go_import_path  github.com/dolthub/maphash

Name:           go-github-dolthub-maphash
Version:        0.1.0
Release:        %autorelease
Summary:        Runtime-backed hashing for comparable Go values
License:        Apache-2.0
URL:            https://github.com/dolthub/maphash
#!RemoteAsset:  sha256:e1cc92f97f77f7104708c382fbebd3bdf9bf1b116167ed73c532b24fb4b926b1
Source0:        https://github.com/dolthub/maphash/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

%description
Maphash exposes Go's optimized runtime hashing for values of any comparable
type, using hardware acceleration when available.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
