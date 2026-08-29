# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           reggen
%define go_import_path  github.com/lucasjones/reggen
%define commit_id       37ba4fa293bb40d3e1d805ba3545bfaab688d669

Name:           go-github-lucasjones-reggen
Version:        0+git20260721.37ba4fa
Release:        %autorelease
Summary:        Generates text based on regular expression definitions
License:        MIT
URL:            https://github.com/lucasjones/reggen
#!RemoteAsset:  sha256:359199a089c35a71aa97983d863280a2b4c39f62474c7e8df63320b92c8d0c4d
Source0:        https://github.com/lucasjones/reggen/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/lucasjones/reggen) = %{version}

%description
Reggen generates strings that match regular expression definitions.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
