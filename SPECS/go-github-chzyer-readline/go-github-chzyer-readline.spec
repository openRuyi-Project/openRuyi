# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           readline
%define go_import_path  github.com/chzyer/readline

Name:           go-github-chzyer-readline
Version:        1.5.1
Release:        %autorelease
Summary:        Readline is a pure go(golang) implementation for GNU-Readline kind library
License:        MIT
URL:            https://github.com/chzyer/readline
#!RemoteAsset
Source0:        https://github.com/chzyer/readline/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/chzyer/test)

Provides:       go(github.com/chzyer/readline) = %{version}

Requires:       go(github.com/chzyer/test)

%description
The most popular multi-platform readline library for Go, featuring
powerful line editing capabilities.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
