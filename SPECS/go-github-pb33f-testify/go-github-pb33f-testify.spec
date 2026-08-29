# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testify
%define go_import_path  github.com/pb33f/testify

Name:           go-github-pb33f-testify
Version:        0.1.0
Release:        %autorelease
Summary:        Testing assertions and mock helpers for Go
License:        MIT
URL:            https://github.com/pb33f/testify
#!RemoteAsset:  sha256:166809d26adffa2cdb2ab2a211d88c524e957bf81d3aa3e6894b837725eb296f
Source0:        https://github.com/pb33f/testify/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use explicit string formats where Go vet rejects dynamic format strings.
# https://github.com/pb33f/testify/pull/3
Patch2000:      2000-tests-fix-non-constant-format-strings.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(go.yaml.in/yaml/v4)

Provides:       go(github.com/pb33f/testify) = %{version}

Requires:       go(github.com/stretchr/objx)
Requires:       go(go.yaml.in/yaml/v4)

%description
This package provides assertions, mocks, suites, and HTTP test helpers for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
