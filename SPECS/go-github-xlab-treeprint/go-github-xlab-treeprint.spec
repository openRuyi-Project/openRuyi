# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           treeprint
%define go_import_path  github.com/xlab/treeprint

Name:           go-github-xlab-treeprint
Version:        1.2.0
Release:        %autorelease
Summary:        ASCII tree rendering library for Go
License:        MIT
URL:            https://github.com/xlab/treeprint
#!RemoteAsset:  sha256:74fa67d893ffbd2a48814c55f1ff7b6b0587f52b2234e683ff30d07b71ed89be
Source0:        https://github.com/xlab/treeprint/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/xlab/treeprint) = %{version}

%description
Treeprint renders Go data structures as predictable, Unicode-friendly ASCII
trees.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
