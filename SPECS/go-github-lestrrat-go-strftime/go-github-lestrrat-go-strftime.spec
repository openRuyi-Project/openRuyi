# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           strftime
%define go_import_path  github.com/lestrrat-go/strftime

Name:           go-github-lestrrat-go-strftime
Version:        1.2.0
Release:        %autorelease
Summary:        Fast strftime implementation for Go
License:        MIT
URL:            https://github.com/lestrrat-go/strftime
#!RemoteAsset:  sha256:d45a47d0d92580fffd63f5b145035e91cfb94a5df1cb5af965be701b4927002c
Source0:        https://github.com/lestrrat-go/strftime/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fastly/go-utils)
BuildRequires:  go(github.com/jehiah/go-strftime)
BuildRequires:  go(github.com/lestrrat-go/envload)
BuildRequires:  go(github.com/ncruces/go-strftime)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tebeka/strftime)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

%description
Strftime provides a fast and reusable implementation of strftime-style time
formatting for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
