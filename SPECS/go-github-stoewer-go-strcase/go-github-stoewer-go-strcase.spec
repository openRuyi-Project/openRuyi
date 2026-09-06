# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-strcase
%define go_import_path  github.com/stoewer/go-strcase

Name:           go-github-stoewer-go-strcase
Version:        1.3.1
Release:        %autorelease
Summary:        String case conversion library for Go
License:        MIT
URL:            https://github.com/stoewer/go-strcase
#!RemoteAsset:  sha256:b9a70676f82b27a6b4de8e5eeae77dbd2e68afb3d9610b88be56fb68cadb612a
Source0:        https://github.com/stoewer/go-strcase/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/stoewer/go-strcase) = %{version}

%description
Go-strcase converts strings between camel case, snake case, kebab case, and
other naming formats.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
