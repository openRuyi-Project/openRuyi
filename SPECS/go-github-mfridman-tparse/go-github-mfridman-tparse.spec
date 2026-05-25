# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tparse
%define go_import_path  github.com/mfridman/tparse

Name:           go-github-mfridman-tparse
Version:        0.18.0
Release:        %autorelease
Summary:        Go test output parser
License:        MIT
URL:            https://github.com/mfridman/tparse
#!RemoteAsset:  sha256:11e779379e6605202aa1751b2de3e36179ad63c38c478748e8c4e4693845c1b5
Source0:        https://github.com/mfridman/tparse/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aymanbagabas/go-osc52/v2)
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/charmbracelet/x/ansi)
BuildRequires:  go(github.com/charmbracelet/x/cellbuf)
BuildRequires:  go(github.com/charmbracelet/x/term)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/muesli/termenv)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/mfridman/tparse) = %{version}

Requires:       go(github.com/charmbracelet/lipgloss)
Requires:       go(github.com/muesli/termenv)
Requires:       go(golang.org/x/term)

%description
tparse parses and summarizes Go test output.

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
