# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gcfg
%define go_import_path  github.com/go-git/gcfg/v2

Name:           go-github-go-git-gcfg-v2
Version:        2.0.2
Release:        %autorelease
Summary:        go-gcfg/gcfg fork for usage in src-d/go-git
License:        BSD-3-Clause
URL:            https://github.com/go-git/gcfg
#!RemoteAsset:  sha256:2d8f25f12e4bec0349cdc5265bca20803adde83edb6fe31690e52506914fe5e3
Source0:        https://github.com/go-git/gcfg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-git/gcfg/v2) = %{version}

%description
Gcfg reads INI-style configuration files into Go structs;
supports user-defined types and subsections.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
