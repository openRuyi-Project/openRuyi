# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           x
%define go_import_path  github.com/charmbracelet/x
%define commit_id       d6a276319c45fce7a423ea796c0fd3e48ec828f8
# TODO: test has circular dependency, add it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-charmbracelet-x
Version:        0+git20260204.d6a2763
Release:        %autorelease
Summary:        Charm experimental packages
License:        MIT
URL:            https://github.com/charmbracelet/x
#!RemoteAsset:  sha256:f791fd740305561ca8798817e0f190c8bc10916d6e09779b97b11b1125264b62
Source0:        https://github.com/charmbracelet/x/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/charmbracelet/x) = %{version}
# Dedicated submodule packages were removed as duplicates of this monorepo
# package. Export providers for the source versions included at this commit.
Provides:       go(github.com/charmbracelet/x/ansi) = 0.11.6
Provides:       go(github.com/charmbracelet/x/cellbuf) = 0.0.15
Provides:       go(github.com/charmbracelet/x/term) = 0.2.2

Requires:       go(github.com/bits-and-blooms/bitset)
Requires:       go(github.com/clipperhouse/displaywidth)
Requires:       go(github.com/clipperhouse/uax29/v2)
Requires:       go(github.com/charmbracelet/colorprofile)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(github.com/rivo/uniseg)
Requires:       go(golang.org/x/sys)

%description
This repository contains experimental packages with no promises of
backwards compatibility. Once they mature here, they might be moved into
other repositories.

Currently the following packages are available:

 * ansi (/ansi): ANSI escape sequence parser and definitions • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/ansi)
 * cellbuf (/cellbuf): Cell-based terminal display parser • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/cellbuf)
 * charmtone (/exp/charmtone): Charm color palette utilities • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/exp/charmtone)
 * colors (/colors): Color utilities • Docs (https://pkg.go.dev/github.
   com/charmbracelet/x/colors)
 * conpty (/conpty): Windows Console Pseudo-terminal library • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/conpty)
 * editor (/editor): open files in text editors • Docs (https://pkg.go.
   dev/github.com/charmbracelet/x/editor)
 * errors (/errors): errors.Join in older Go versions • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/errors)
 * etag (/etag): HTTP ETag generation utilities • Docs (https://pkg.go.
   dev/github.com/charmbracelet/x/etag)
 * gitignore (/gitignore): Gitignore pattern matching • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/gitignore)
 * golden (/exp/golden): verify golden file equality • Docs (https://pkg.
   go.dev/github.com/charmbracelet/x/exp/golden)
 * higherorder (/exp/higherorder): generic higher order functions • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/exp/higherorder)
 * input (/input): terminal event input handler and driver • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/input)
 * json (/json): JSON parsing using generics • Docs (https://pkg.go.
   dev/github.com/charmbracelet/x/json)
 * maps (/exp/maps): generic maps utilities • Docs (https://pkg.go.
   dev/github.com/charmbracelet/x/exp/maps)
 * mosaic (/mosaic): Image to terminal rendering • Docs (https://pkg.go.
   dev/github.com/charmbracelet/x/mosaic)
 * open (/exp/open): open a file/URL using open, xdg-open, etc • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/exp/open)
 * ordered (/exp/ordered): generic min, max, and clamp functions for
   ordered types • Docs (https://pkg.go.dev/github.
   com/charmbracelet/x/exp/ordered)
 * pony (/pony): Declarative terminal UI markup language • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/pony)
 * powernap (/powernap): LSP client utilities • Docs (https://pkg.go.
   dev/github.com/charmbracelet/x/powernap)
 * slice (/exp/slice): generic slice utilities • Docs (https://pkg.go.
   dev/github.com/charmbracelet/x/exp/slice)
 * sshkey (/sshkey): open and parse SSH keys, asks for passphrases when
   needed • Docs (https://pkg.go.dev/github.com/charmbracelet/x/sshkey)
 * strings (/exp/strings): utilities for working with strings • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/exp/strings)
 * teatest (/exp/teatest): a library for testing Bubble Tea
   (https://github.com/charmbracelet/bubbletea) programs • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/exp/teatest)
 * term (/term): terminal utilities and helpers • Docs (https://pkg.go.
   dev/github.com/charmbracelet/x/term)
 * termios (/termios): Termios unified API and library • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/termios)
 * toner (/exp/toner): Color toning utilities • Docs (https://pkg.go.
   dev/github.com/charmbracelet/x/exp/toner)
 * vcr (/vcr): HTTP recording and playback for testing • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/vcr)
 * vt (/vt): Virtual terminal emulator • Docs (https://pkg.go.dev/github.
   com/charmbracelet/x/vt)
 * wcwidth (/wcwidth): Wide character width calculation • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/wcwidth)
 * windows (/windows): Windows API used at Charmbracelet • Docs
   (https://pkg.go.dev/github.com/charmbracelet/x/windows)
 * xpty (/xpty): cross-platform PTY interface • Docs (https://pkg.go.
   dev/github.com/charmbracelet/x/xpty)

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
