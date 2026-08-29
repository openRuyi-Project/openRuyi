# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-git-fixtures
%define go_import_path  github.com/go-git/go-git-fixtures/v4
%define commit_id 55a94097c399cd93043103aa276a733b91537b0b

Name:           go-github-go-git-go-git-fixtures-v4
Version:        4.3.1+git20260616.55a9409
Release:        %autorelease
Summary:        Git repository fixtures for go-git tests
License:        Apache-2.0
URL:            https://github.com/go-git/go-git-fixtures
#!RemoteAsset:  sha256:bd5d051b87d7a9858c6a7bc575fba718a0d69dcdad1380310c6bf05eccc9fa17
Source0:        https://github.com/go-git/go-git-fixtures/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# go-billy 5.9 rejects absolute temp paths for filesystems rooted at "".
# - HNO3Miracle
Patch2000:      2000-use-filesystem-relative-temp-dir.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-git/go-billy/v5)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/go-git/go-git-fixtures/v4) = %{version}

Requires:       go(github.com/go-git/go-billy/v5)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/kr/text)
Requires:       go(golang.org/x/sys)
Requires:       go(gopkg.in/check.v1)

%description
go-git-fixtures provides Git repository fixture data used by the go-git test
suite and packages that test against go-git repositories.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
