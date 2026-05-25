# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ansi
%define go_import_path  github.com/charmbracelet/x/ansi
# go2spec resolves this import path to the repository root; package the selected Go submodule instead.
# The import path is a Go module below the repository root; keep %check scoped
# to this module so GOPATH-mode tests do not scan sibling modules from the archive. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-github-charmbracelet-x-ansi
Version:        0.11.7
Release:        %autorelease
Summary:        ANSI terminal helpers for Go
License:        MIT
URL:            https://github.com/charmbracelet/x
#!RemoteAsset:  sha256:0cbdf91967be1db68b9cd800b5194c43d3750de60e3725a04da78d2a2242c39c
Source0:        https://github.com/charmbracelet/x/archive/refs/tags/ansi/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bits-and-blooms/bitset)
BuildRequires:  go(github.com/clipperhouse/displaywidth)
BuildRequires:  go(github.com/clipperhouse/uax29/v2)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-runewidth)

Provides:       go(github.com/charmbracelet/x/ansi) = %{version}

Requires:       go(github.com/bits-and-blooms/bitset)
Requires:       go(github.com/clipperhouse/displaywidth)
Requires:       go(github.com/clipperhouse/uax29/v2)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/mattn/go-runewidth)

%description
This package provides ANSI terminal helpers for Go.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
