# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logrus
%define go_import_path  github.com/sirupsen/logrus

Name:           go-github-sirupsen-logrus
Version:        1.10.2
Release:        %autorelease
Summary:        Structured logger for Go
License:        MIT
URL:            https://github.com/sirupsen/logrus
#!RemoteAsset:  sha256:8a36bd142efe532be2e293fae0c3b2555c9522df3f2f0aa9bf9db83f5d86383f
Source0:        https://github.com/sirupsen/logrus/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/sirupsen/logrus) = %{version}

Requires:       go(golang.org/x/sys)

%description
logrus provides structured logging for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
