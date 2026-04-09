# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           douceur
%define go_import_path  github.com/aymerick/douceur
# TODO: test dependency need too much dependency, add it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-aymerick-douceur
Version:        0.2.0
Release:        %autorelease
Summary:        A simple CSS parser and inliner in Go
License:        MIT
URL:            https://github.com/aymerick/douceur
#!RemoteAsset
Source0:        https://github.com/aymerick/douceur/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/aymerick/douceur) = %{version}

%description
A simple CSS parser and inliner in Golang.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
