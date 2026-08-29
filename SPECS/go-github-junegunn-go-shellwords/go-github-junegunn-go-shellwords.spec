# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-shellwords
%define go_import_path  github.com/junegunn/go-shellwords
%define commit_id       2aa3b3277741a6ad31883f223d770221a85e9dd0

Name:           go-github-junegunn-go-shellwords
Version:        0+git20250127.2aa3b32
Release:        %autorelease
Summary:        Parse command lines into shell words
License:        MIT
URL:            https://github.com/junegunn/go-shellwords
#!RemoteAsset:  sha256:5b7a6c2c25b305b83cf55309358833708fbd4555c0c1a47a0a5c20030abd0fba
Source0:        https://github.com/junegunn/go-shellwords/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/junegunn/go-shellwords) = %{version}

%description
Package go-shellwords parses command lines into shell-style words and optional
environment assignments.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
