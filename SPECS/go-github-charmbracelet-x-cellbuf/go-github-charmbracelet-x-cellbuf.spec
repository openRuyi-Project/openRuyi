# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cellbuf
%define go_import_path  github.com/charmbracelet/x/cellbuf
# The import path is a Go module below the repository root;
# keep %check scopedto this module so GOPATH-mode tests
# do not scan sibling modules from the archive. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-github-charmbracelet-x-cellbuf
Version:        0.0.15
Release:        %autorelease
Summary:        Terminal cell buffer helpers for Go
License:        MIT
URL:            https://github.com/charmbracelet/x
#!RemoteAsset:  sha256:be0b120ce2c9da343aaa2e8810596228ab442444aeb8a3f14f32e56c5b2732b3
Source0:        https://github.com/charmbracelet/x/archive/refs/tags/cellbuf/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/charmbracelet/colorprofile)
BuildRequires:  go(github.com/charmbracelet/x/ansi)
BuildRequires:  go(github.com/charmbracelet/x/term)
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/clipperhouse/stringish)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/rivo/uniseg)
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/charmbracelet/x/cellbuf) = %{version}

Requires:       go(github.com/charmbracelet/colorprofile)
Requires:       go(github.com/charmbracelet/x/ansi)
Requires:       go(github.com/charmbracelet/x/term)
Requires:       go(github.com/clipperhouse/displaywidth)
Requires:       go(github.com/clipperhouse/stringish)
Requires:       go(github.com/clipperhouse/uax29/v2)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(github.com/rivo/uniseg)
Requires:       go(github.com/xo/terminfo)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/sys)

%description
This package provides Terminal cell buffer helpers for Go.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
