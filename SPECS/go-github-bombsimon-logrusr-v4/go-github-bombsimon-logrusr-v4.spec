# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logrusr
%define go_import_path  github.com/bombsimon/logrusr/v4

Name:           go-github-bombsimon-logrusr-v4
Version:        4.1.0
Release:        %autorelease
Summary:        Logrus backend for the logr interface
License:        MIT
URL:            https://github.com/bombsimon/logrusr
#!RemoteAsset:  sha256:f65a0182512284e7887efc1ace8a126eabf038abbf40ab8fcdf7cc99d1b0f81a
Source0:        https://github.com/bombsimon/logrusr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/sirupsen/logrus)

%description
Logrusr adapts Logrus loggers to the structured logging interfaces defined by
github.com/go-logr/logr.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
