# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           slim-sprig
%define go_import_path  github.com/go-task/slim-sprig/v3
%define commit_id 38f81b619418835ccb38a10056359737311c99e3
# TestGetHostByName depends on DNS/network availability and returns nil in the
# OBS build sandbox. - HNO3Miracle
%define go_test_exclude %{go_import_path}

Name:           go-github-go-task-slim-sprig-v3
Version:        0+git20260602.38f81b6
Release:        %autorelease
Summary:        Go library for github.com/go-task/slim-sprig/v3
License:        MIT
URL:            https://github.com/go-task/slim-sprig
#!RemoteAsset:  sha256:7cf9aa43e9f1fa739a7f24288a0b336191be8249f3c3f3e0de816ab80fef021e
Source0:        https://github.com/go-task/slim-sprig/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-task/slim-sprig/v3) = %{version}

%description
This package provides the Go library github.com/go-task/slim-sprig/v3.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
