# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           log
%define go_import_path  github.com/charmbracelet/log

Name:           go-github-charmbracelet-log
Version:        0.4.2
Release:        %autorelease
Summary:        A minimal, colorful Go logging library 🪵
License:        MIT
URL:            https://github.com/charmbracelet/log
#!RemoteAsset
Source0:        https://github.com/charmbracelet/log/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/go-logfmt/logfmt)
BuildRequires:  go(github.com/muesli/termenv)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/mattn/go-runewidth)

Provides:       go(github.com/charmbracelet/log) = %{version}

Requires:       go(github.com/charmbracelet/lipgloss)
Requires:       go(github.com/go-logfmt/logfmt)
Requires:       go(github.com/muesli/termenv)
Requires:       go(github.com/stretchr/testify)

%description
A minimal and colorful Go logging library. 🪵

It provides a leveled structured human readable logger with a small API.
Unlike standard log (https://pkg.go.dev/log), the Charm logger provides
customizable colorful human readable logging with batteries included.

 * Uses Lip Gloss (https://github.com/charmbracelet/lipgloss) to style
   and colorize the output.
 * Colorful, human readable format.
 * Ability to customize the time stamp format.
 * Skips caller frames and marks function as helpers.
 * Leveled logging.
 * Text, JSON, and Logfmt formatters.
 * Store and retrieve logger in and from context.
 * Slog handler.
 * Standard log adapter.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
