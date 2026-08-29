# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           argparse
%define go_import_path  github.com/akamensky/argparse

Name:           go-github-akamensky-argparse
Version:        1.4.0
Release:        %autorelease
Summary:        Argument parser for Go
License:        MIT
URL:            https://github.com/akamensky/argparse
VCS:            git:https://github.com/akamensky/argparse
#!RemoteAsset:  sha256:755bc41205468e0fb7264bee5c0f14585ee8eeaa377e96a23655c12f65df7016
Source0:        https://github.com/akamensky/argparse/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/akamensky/argparse) = %{version}

%description
Argparse is an argument parser for Go command-line applications. It supports
positional arguments, flags, commands, validation, and generated help output.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
