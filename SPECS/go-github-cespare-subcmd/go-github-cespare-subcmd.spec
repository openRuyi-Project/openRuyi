# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           subcmd
%define go_import_path  github.com/cespare/subcmd

Name:           go-github-cespare-subcmd
Version:        1.1.0
Release:        %autorelease
Summary:        Git-style subcommand handling for Go programs
License:        MIT
URL:            https://github.com/cespare/subcmd
#!RemoteAsset:  sha256:b5e2de80e725a8a4cd0c21ecba959010e69fd16055cae9ff51d6dc8cba361c8d
Source0:        https://github.com/cespare/subcmd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Subcmd extends Go's flag package with git-style subcommand dispatch,
argument parsing, and help output. The complete source repository includes
an example command-line program.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
