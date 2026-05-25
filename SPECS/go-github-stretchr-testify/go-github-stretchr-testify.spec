# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testify
%define go_import_path  github.com/stretchr/testify

Name:           go-github-stretchr-testify
Version:        1.11.0
Release:        %autorelease
Summary:        A toolkit with common assertions and mocks that plays nicely with the standard library
License:        MIT
URL:            https://github.com/stretchr/testify
#!RemoteAsset:  sha256:b7f2847b9ed10a6e40f7353f3f2a138cc8d54aed3f661cb9c8a1ced7d21a448f
Source0:        https://github.com/stretchr/testify/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://sources.debian.org/src/golang-testify/1.10.0-1/debian/patches/do-not-use-race.patch
Patch0:         2000-do-not-use-race.patch

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(github.com/stretchr/testify) = %{version}
Provides:       go(github.com/stretchr/testify/assert) = %{version}
Provides:       go(github.com/stretchr/testify/http) = %{version}
Provides:       go(github.com/stretchr/testify/mock) = %{version}
Provides:       go(github.com/stretchr/testify/require) = %{version}
Provides:       go(github.com/stretchr/testify/suite) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/objx)
Requires:       go(go.yaml.in/yaml/v3)

%description
Testify provide many tools for testifying that your code will behave
as you intend.

Features include:

 * Easy assertions
 * Mocking
 * Testing suite interfaces and functions

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
