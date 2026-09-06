# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cli
%define go_import_path  github.com/urfave/cli/v3
# The docs package imports cli-altsrc, which itself requires this module.
%define go_test_exclude %{go_import_path}/docs

Name:           go-github-urfave-cli-v3
Version:        3.11.0
Release:        %autorelease
Summary:        Command-line application framework for Go
License:        MIT
URL:            https://github.com/urfave/cli
#!RemoteAsset:  sha256:95351a5fdf8da5ed550521712134abc64dccce81d4f9249eb4ac509504c1ce1a
Source0:        https://github.com/urfave/cli/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

%description
Urfave CLI is a minimal framework for building and organizing command-line
applications in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
