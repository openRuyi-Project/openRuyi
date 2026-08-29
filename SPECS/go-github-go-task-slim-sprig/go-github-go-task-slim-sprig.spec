# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           slim-sprig
%define go_import_path  github.com/go-task/slim-sprig
# TestGetHostByName depends on DNS/network availability and returns nil in the
# OBS build sandbox. - HNO3Miracle
%define go_test_exclude %{go_import_path}

Name:           go-github-go-task-slim-sprig
Version:        3.0.0
Release:        %autorelease
Summary:        Useful template functions for Go templates
License:        MIT
URL:            https://github.com/go-task/slim-sprig
#!RemoteAsset:  sha256:673b1acc819c60899e78b00f20da2b8270a0e370c01d3def9cda0a86167881fb
Source0:        https://github.com/go-task/slim-sprig/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/go-task/slim-sprig) = %{version}

%description
Slim-Sprig is a lightweight fork of Sprig with template functions for Go.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
