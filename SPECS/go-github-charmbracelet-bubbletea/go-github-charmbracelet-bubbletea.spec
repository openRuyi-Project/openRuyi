# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bubbletea
%define go_import_path  github.com/charmbracelet/bubbletea
# TODO: Test need too much dependency, add it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-charmbracelet-bubbletea
Version:        1.3.10
Release:        %autorelease
Summary:        A powerful little TUI framework 🏗
License:        MIT
URL:            https://github.com/charmbracelet/bubbletea
#!RemoteAsset
Source0:        https://github.com/charmbracelet/bubbletea/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/charmbracelet/x)
BuildRequires:  go(github.com/muesli/ansi)
BuildRequires:  go(github.com/muesli/cancelreader)

Provides:       go(github.com/charmbracelet/bubbletea) = %{version}

Requires:       go(github.com/charmbracelet/lipgloss)
Requires:       go(github.com/charmbracelet/x)
Requires:       go(github.com/muesli/ansi)
Requires:       go(github.com/muesli/cancelreader)

%description
The fun, functional and stateful way to build terminal apps. A Go
framework based on The Elm Architecture (https://guide.elm-
lang.org/architecture/). Bubble Tea is well-suited for simple and
complex
terminal applications, either inline, full-window, or a mix of both.

Bubble Tea is in use in production and includes a number of features and
performance optimizations we’ve added along the way. Among those is a
framerate-based renderer, mouse support, focus reporting and more.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
