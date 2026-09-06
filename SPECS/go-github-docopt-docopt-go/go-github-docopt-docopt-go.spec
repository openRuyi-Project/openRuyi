# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           docopt-go
%define go_import_path  github.com/docopt/docopt-go

Name:           go-github-docopt-docopt-go
Version:        0.6.2
Release:        %autorelease
Summary:        Command-line argument parser based on help messages
License:        MIT
URL:            https://github.com/docopt/docopt-go
#!RemoteAsset:  sha256:bfd2816c9b1830eff84fc97fdad8fbf88ed56b6fccfe29d40c85c55e676edea9
Source0:        https://github.com/docopt/docopt-go/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Docopt-go parses command-line arguments from the usage and option descriptions
in an application's help message.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
