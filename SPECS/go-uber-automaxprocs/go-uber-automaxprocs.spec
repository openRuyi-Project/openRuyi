# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           automaxprocs
%define go_import_path  go.uber.org/automaxprocs

Name:           go-uber-automaxprocs
Version:        1.6.0
Release:        %autorelease
Summary:        Automatic GOMAXPROCS tuning for Go
License:        Apache-2.0
URL:            https://github.com/uber-go/automaxprocs
#!RemoteAsset:  sha256:fb750295e270f668502fb139ff626bf5209033c7893b29521238cd04502e55cf
Source0:        https://github.com/uber-go/automaxprocs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/prashantv/gostub)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(go.uber.org/automaxprocs) = %{version}

%description
Automaxprocs automatically sets GOMAXPROCS to match the Linux CPU quota
available to a Go process.

%files
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
