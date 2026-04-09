# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assert
%define go_import_path  github.com/alecthomas/assert

Name:           go-github-alecthomas-assert
Version:        2.11.0
Release:        %autorelease
Summary:        A simple assertion library using Go generics
License:        MIT
URL:            https://github.com/alecthomas/assert
#!RemoteAsset
Source0:        https://github.com/alecthomas/assert/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/repr)
BuildRequires:  go(github.com/hexops/gotextdiff)

Provides:       go(github.com/alecthomas/assert) = %{version}

Requires:       go(github.com/alecthomas/repr)
Requires:       go(github.com/hexops/gotextdiff)

%description
A simple assertion library using Go generics

This library is inspired by testify/require, but with a significantly
reduced API surface based on empirical use of that package.

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
