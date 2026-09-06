# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           readline
%define go_import_path  github.com/ergochat/readline

Name:           go-github-ergochat-readline
Version:        0.1.3
Release:        %autorelease
Summary:        Apure Go implementation of functionality comparable to GNU Readline
License:        MIT
URL:            https://github.com/ergochat/readline
#!RemoteAsset:  sha256:842a97fff7b2c025fd0c1c89f8a1355a42b94a714be90e6caf618ce9e9db84e1
Source0:        https://github.com/ergochat/readline/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/ergochat/readline) = %{version}

Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)

%description
This is a pure Go implementation of functionality comparable to GNU
Readline, i.e. line editing and command history for simple TUI programs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
