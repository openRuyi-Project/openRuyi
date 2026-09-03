# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           git-todo-parser
%define go_import_path  github.com/stefanhaller/git-todo-parser
%define commit_id       c50528f08304a21c90bfea55a7b3532317f3a33f

Name:           go-github-stefanhaller-git-todo-parser
Version:        0+git20260621.c50528f
Release:        %autorelease
Summary:        Small parser for git todo files
License:        MIT
URL:            https://github.com/stefanhaller/git-todo-parser
#!RemoteAsset:  sha256:d6bd80b3ff71f541a23c36b745917caf13cd7aacb8a97fe24075f8f22924ef00
Source0:        https://github.com/stefanhaller/git-todo-parser/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/stefanhaller/git-todo-parser) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
git-todo-parser parses and serializes git rebase todo (instruction) files.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
