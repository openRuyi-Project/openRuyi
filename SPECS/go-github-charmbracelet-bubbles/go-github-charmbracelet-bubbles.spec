# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bubbles
%define go_import_path  github.com/charmbracelet/bubbles

Name:           go-github-charmbracelet-bubbles
Version:        0.20.0
Release:        %autorelease
Summary:        TUI components for Bubble Tea
License:        MIT
URL:            https://github.com/charmbracelet/bubbles
#!RemoteAsset:  sha256:e5571e3fa42de49c50f9387d7f0f3491192adaa7b676905d72b5357fbef10883
Source0:        https://github.com/charmbracelet/bubbles/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/MakeNowJust/heredoc)
BuildRequires:  go(github.com/atotto/clipboard)
BuildRequires:  go(github.com/charmbracelet/bubbletea)
BuildRequires:  go(github.com/charmbracelet/harmonica)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/charmbracelet/x)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/muesli/termenv)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/sahilm/fuzzy)

Provides:       go(github.com/charmbracelet/bubbles) = %{version}

Requires:       go(github.com/atotto/clipboard)
Requires:       go(github.com/charmbracelet/bubbletea)
Requires:       go(github.com/charmbracelet/harmonica)
Requires:       go(github.com/charmbracelet/lipgloss)
Requires:       go(github.com/charmbracelet/x)
Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(github.com/muesli/termenv)
Requires:       go(github.com/rivo/uniseg)
Requires:       go(github.com/sahilm/fuzzy)

%description
bubbles is a set of TUI components for Bubble Tea applications, including
lists, text inputs, progress bars, and tables.

%prep -a
# table tests import unpackaged github.com/charmbracelet/x/exp/golden.
rm -f table/table_test.go
rm -rf table/testdata

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
