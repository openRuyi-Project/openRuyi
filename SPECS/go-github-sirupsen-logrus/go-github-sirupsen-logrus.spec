# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logrus
%define go_import_path  github.com/sirupsen/logrus

Name:           go-github-sirupsen-logrus
Version:        1.9.4
Release:        %autorelease
Summary:        Structured logger for Go
License:        MIT
URL:            https://github.com/sirupsen/logrus
#!RemoteAsset:  sha256:9609d276c670be5fccf9c6489d1036476b5e7afc49fd33cc4f5973dcc803366a
Source0:        https://github.com/sirupsen/logrus/archive/refs/tags/v1.9.4.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n logrus-1.9.4

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/sirupsen/logrus) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/sys)
Requires:       go(gopkg.in/yaml.v3)

%description
This package provides Structured logger for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
