# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-docopt
%define go_import_path  github.com/flynn/go-docopt
%define commit_id       f6dd2ebbb31e9721c860cf1faf5c944aa73e3844
# The examples are independent programs with multiple main functions in the
# same directories, so they cannot be tested as Go packages.
%define go_test_exclude_glob %{go_import_path}/examples*

Name:           go-github-flynn-go-docopt
Version:        0+git20260817.f6dd2eb
Release:        %autorelease
Summary:        Command-line argument parser based on help messages
License:        MIT
URL:            https://github.com/flynn/go-docopt
#!RemoteAsset:  sha256:05b3811f3c8bb88fd53eb5daf66d86df63e24565a181fabc1488a50d805ba9e6
Source0:        https://github.com/flynn/go-docopt/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/docopt/docopt-go)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/docopt/docopt-go)

%description
Go-docopt parses command-line arguments from the usage and option descriptions
in an application's help message.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
