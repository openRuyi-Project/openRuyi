# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gcfg
%define go_import_path  github.com/go-git/gcfg

Name:           go-github-go-git-gcfg
Version:        2.0.2
Release:        %autorelease
Summary:        go-gcfg/gcfg fork for usage in src-d/go-git
License:        BSD-3-Clause
URL:            https://github.com/go-git/gcfg
#!RemoteAsset
Source0:        https://github.com/go-git/gcfg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-git/gcfg) = %{version}

%description
Gcfg reads INI-style configuration files into Go structs;
supports user-defined types and subsections.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
