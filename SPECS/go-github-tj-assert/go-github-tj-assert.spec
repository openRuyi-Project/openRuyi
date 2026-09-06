# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assert
%define go_import_path  github.com/tj/assert

Name:           go-github-tj-assert
Version:        0.0.3
Release:        %autorelease
Summary:        Immediate-failure assertions for Go tests
License:        MIT
URL:            https://github.com/tj/assert
#!RemoteAsset:  sha256:1596d9e6f2ba75f1b5e4b9b8f4a86ac4834723f1abaff4a717ba8c6896387f05
Source0:        https://github.com/tj/assert/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
Assert provides the same assertions as testify's assert package while stopping
test execution immediately when an assertion fails.

%files
%doc Readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
