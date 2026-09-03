# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           glamour
%define go_import_path  github.com/charmbracelet/glamour
%define commit_id       549f544650e38ad6f4ed21cf79e3749d7c08a7f5

Name:           go-github-charmbracelet-glamour
Version:        0+git20260723.549f544
Release:        %autorelease
Summary:        Stylesheet-based Markdown rendering for terminals
License:        MIT
URL:            https://github.com/charmbracelet/glamour
#!RemoteAsset:  sha256:3b12143f0e3994a633fa602e4521b116e4c55f61509f0463d78cb91e34b87eeb
Source0:        https://github.com/charmbracelet/glamour/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/chroma/v2)
BuildRequires:  go(github.com/aymanbagabas/go-osc52/v2)
BuildRequires:  go(github.com/aymanbagabas/go-udiff)
BuildRequires:  go(github.com/aymerick/douceur)
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/charmbracelet/x/ansi)
BuildRequires:  go(github.com/charmbracelet/x/cellbuf)
BuildRequires:  go(github.com/charmbracelet/x/term)
BuildRequires:  go(github.com/dlclark/regexp2)
BuildRequires:  go(github.com/gorilla/css)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/microcosm-cc/bluemonday)
BuildRequires:  go(github.com/muesli/reflow)
BuildRequires:  go(github.com/muesli/termenv)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(github.com/yuin/goldmark)
BuildRequires:  go(github.com/yuin/goldmark-emoji)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/charmbracelet/glamour) = %{version}

Requires:       go(github.com/alecthomas/chroma/v2)
Requires:       go(github.com/aymanbagabas/go-osc52/v2)
Requires:       go(github.com/aymanbagabas/go-udiff)
Requires:       go(github.com/aymerick/douceur)
Requires:       go(github.com/charmbracelet/colorprofile)
Requires:       go(github.com/charmbracelet/lipgloss)
Requires:       go(github.com/charmbracelet/x/ansi)
Requires:       go(github.com/charmbracelet/x/cellbuf)
Requires:       go(github.com/charmbracelet/x/term)
Requires:       go(github.com/dlclark/regexp2)
Requires:       go(github.com/gorilla/css)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(github.com/microcosm-cc/bluemonday)
Requires:       go(github.com/muesli/reflow)
Requires:       go(github.com/muesli/termenv)
Requires:       go(github.com/rivo/uniseg)
Requires:       go(github.com/xo/terminfo)
Requires:       go(github.com/yuin/goldmark)
Requires:       go(github.com/yuin/goldmark-emoji)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)

%description
glamour renders Markdown to ANSI-styled terminal output using built-in or
customizable stylesheets.

# Golden-output tests use the unshipped charmbracelet/x/exp/golden helper;
# retain the remaining parser, renderer and style tests.
%prep -a
rm -f glamour_test.go ansi/renderer_test.go

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
