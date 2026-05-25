# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gostub
%define go_import_path  github.com/prashantv/gostub

Name:           go-github-prashantv-gostub
Version:        1.1.0
Release:        %autorelease
Summary:        Stub variables in Go tests
License:        MIT
URL:            https://github.com/prashantv/gostub
#!RemoteAsset:  sha256:ed08d1297409f9e1c7b07f437727fe0f6e73beef97700bb1d7410995761c1fc9
Source0:        https://github.com/prashantv/gostub/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/prashantv/gostub) = %{version}

%description
This package provides helpers for stubbing variables in Go tests.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
