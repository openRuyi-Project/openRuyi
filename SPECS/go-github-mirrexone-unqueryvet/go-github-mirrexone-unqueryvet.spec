# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           unqueryvet
%define go_import_path  github.com/MirrexOne/unqueryvet

Name:           go-github-mirrexone-unqueryvet
Version:        1.5.4
Release:        %autorelease
Summary:        Provides a Go static analysis tool that detects SELECT * usage
License:        MIT
URL:            https://github.com/MirrexOne/unqueryvet
#!RemoteAsset:  sha256:87216d4b0d1d5efbcd94b830109f629ffb68738cb4b911fa7b855b3dd32ec283
Source0:        https://github.com/MirrexOne/unqueryvet/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aymanbagabas/go-osc52/v2)
BuildRequires:  go(github.com/charmbracelet/bubbles)
BuildRequires:  go(github.com/charmbracelet/bubbletea)
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/charmbracelet/x/ansi)
BuildRequires:  go(github.com/charmbracelet/x/cellbuf)
BuildRequires:  go(github.com/charmbracelet/x/term)
BuildRequires:  go(github.com/erikgeiser/coninput)
BuildRequires:  go(github.com/expr-lang/expr)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-localereader)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/muesli/ansi)
BuildRequires:  go(github.com/muesli/cancelreader)
BuildRequires:  go(github.com/muesli/termenv)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/MirrexOne/unqueryvet) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/internal/analyzer) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/internal/analyzer/sqlbuilders) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/internal/cli) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/internal/configloader) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/internal/dsl) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/internal/lsp) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/internal/lsp/protocol) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/internal/messages) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/internal/runner) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/internal/tui) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/internal/version) = %{version}
Provides:       go(github.com/MirrexOne/unqueryvet/pkg/config) = %{version}

Requires:       go(github.com/charmbracelet/bubbles)
Requires:       go(github.com/charmbracelet/bubbletea)
Requires:       go(github.com/charmbracelet/lipgloss)
Requires:       go(github.com/expr-lang/expr)
Requires:       go(golang.org/x/tools)
Requires:       go(gopkg.in/yaml.v3)

%description
Provides a Go static analysis tool that detects SELECT * usage.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n unqueryvet-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/MirrexOne/unqueryvet

%changelog
%autochangelog
