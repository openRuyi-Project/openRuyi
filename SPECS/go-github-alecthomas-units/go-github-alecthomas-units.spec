# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           units
%define go_import_path  github.com/alecthomas/units
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id 0f3dac36c52b29c22285af9a6e6593035dadd74c

Name:           go-github-alecthomas-units
Version:        0+git20260108.0f3dac3
Release:        %autorelease
Summary:        Helpful unit multipliers and functions for Go
License:        MIT
URL:            https://github.com/alecthomas/units
#!RemoteAsset
Source0:        https://github.com/alecthomas/units/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/alecthomas/units) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
Units - Helpful unit multipliers and functions for Go

The goal of this package is to have functionality similar to the time
(http://golang.org/pkg/time/) package.

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
