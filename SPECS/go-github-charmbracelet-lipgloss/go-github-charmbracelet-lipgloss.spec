# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lipgloss
%define go_import_path  github.com/charmbracelet/lipgloss
# TODO: test has circular dependency, add it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-charmbracelet-lipgloss
Version:        1.1.0
Release:        %autorelease
Summary:        Style definitions for nice terminal layouts
License:        MIT
URL:            https://github.com/charmbracelet/lipgloss
#!RemoteAsset
Source0:        https://github.com/charmbracelet/lipgloss/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aymanbagabas/go-udiff)
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/charmbracelet/x)
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/muesli/termenv)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/creack/pty)

Provides:       go(github.com/charmbracelet/lipgloss) = %{version}

Requires:       go(github.com/aymanbagabas/go-udiff)
Requires:       go(github.com/charmbracelet/x)
Requires:       go(github.com/clipperhouse/displaywidth)
Requires:       go(github.com/muesli/termenv)
Requires:       go(github.com/rivo/uniseg)

%description
Lip Gloss

Style definitions for nice terminal layouts. Built with TUIs in mind.

Lip Gloss takes an expressive, declarative approach to terminal
rendering. Users familiar with CSS will feel at home with Lip Gloss.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
