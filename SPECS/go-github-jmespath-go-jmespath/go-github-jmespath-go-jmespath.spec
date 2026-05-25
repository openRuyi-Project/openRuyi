# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-jmespath
%define go_import_path  github.com/jmespath/go-jmespath
# The bundled internal/testify copy is a test helper. Its own assert/suite
# self-tests fail under newer Go vet and intentional panic subtests, while the
# jmespath package tests are still run.
%define go_test_exclude_glob %{shrink:
    github.com/jmespath/go-jmespath/internal/testify/assert*
    github.com/jmespath/go-jmespath/internal/testify/suite
}

Name:           go-github-jmespath-go-jmespath
Version:        0.4.0
Release:        %autorelease
Summary:        JMESPath implementation for Go
License:        Apache-2.0
URL:            https://github.com/jmespath/go-jmespath
#!RemoteAsset:  sha256:aa86d00b6836345eee196c13df2df084a18e0b1159935de9289f2ef6a7fe375d
Source0:        https://github.com/jmespath/go-jmespath/archive/refs/tags/v0.4.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-jmespath-0.4.0

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/jmespath/go-jmespath) = %{version}
Provides:       go(github.com/jmespath/go-jmespath/internal/testify) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/objx)
Requires:       go(gopkg.in/yaml.v2)

%description
This package provides JMESPath implementation for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
