# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dig
%define go_import_path  go.uber.org/dig

Name:           go-uber-dig
Version:        1.19.0
Release:        %autorelease
Summary:        Reflection-based dependency injection toolkit for Go
License:        MIT
URL:            https://github.com/uber-go/dig
#!RemoteAsset:  sha256:9ca333ca78dcf8aeb87a8a3fb118a505b56d86f00f0f3fbbef96d31e691dec56
Source0:        https://github.com/uber-go/dig/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
Dig is a reflection-based dependency injection toolkit for constructing and
resolving Go object graphs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
