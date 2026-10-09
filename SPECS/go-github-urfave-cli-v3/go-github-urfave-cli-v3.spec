# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cli
%define go_import_path  github.com/urfave/cli/v3
# The docs package imports cli-altsrc, which itself requires this module.
%define go_test_exclude  %{go_import_path}/docs

Name:           go-github-urfave-cli-v3
Version:        3.13.0
Release:        %autorelease
Summary:        Command-line application framework for Go
License:        MIT
URL:            https://github.com/urfave/cli
#!RemoteAsset:  sha256:6359e879782eb330304e5cdc65550802839a9adc4499cedb37c4254c8d0cc5b7
Source0:        https://github.com/urfave/cli/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Current Go vet rejects non-constant format strings in command tests; keep
# running the tests with vet disabled.
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
