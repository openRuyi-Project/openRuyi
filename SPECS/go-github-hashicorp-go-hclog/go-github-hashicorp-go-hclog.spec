# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-hclog
%define go_import_path  github.com/hashicorp/go-hclog

Name:           go-github-hashicorp-go-hclog
Version:        1.6.3
Release:        %autorelease
Summary:        A common logging package for HashiCorp tools
License:        MIT
URL:            https://github.com/hashicorp/go-hclog
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-hclog/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/hashicorp/go-hclog) = %{version}

Requires:       go(github.com/fatih/color)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/stretchr/testify)

%description
go-hclog is a package for Go that provides a simple key/value logging
interface for use in development and production environments.

It provides logging levels that provide decreased output based upon the
desired amount of output, unlike the standard library log package.

It provides Printf style logging of values via hclog.Fmt().

It provides a human readable output mode for use in development as well
as JSON output mode for production.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
