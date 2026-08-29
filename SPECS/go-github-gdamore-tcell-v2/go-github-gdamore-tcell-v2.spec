# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tcell
%define go_import_path  github.com/gdamore/tcell/v2

Name:           go-github-gdamore-tcell-v2
Version:        2.13.10
Release:        %autorelease
Summary:        Cell-based terminal package for Go
License:        Apache-2.0
URL:            https://github.com/gdamore/tcell
#!RemoteAsset:  sha256:d851aaa880ae54e1b8f2067589bfe8cc2a49d3b9b6edc579447b79983a5d253d
Source0:        https://github.com/gdamore/tcell/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gdamore/encoding)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/gdamore/tcell/v2) = %{version}

Requires:       go(github.com/gdamore/encoding)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)

%description
Tcell provides a cell-based view for text terminals, with support for colors,
Unicode, keyboard input, and mouse events.

%files
%doc README* TUTORIAL*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
