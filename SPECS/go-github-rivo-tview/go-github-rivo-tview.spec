# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tview
%define go_import_path  github.com/rivo/tview

Name:           go-github-rivo-tview
Version:        0.42.0
Release:        %autorelease
Summary:        Rich interactive widgets for terminal UIs
License:        MIT
URL:            https://github.com/rivo/tview
#!RemoteAsset:  sha256:0c7b0177e633cb83d7d6f0e6faf7ce3609603f109bf1e20dcf68f529c31c24d5
Source0:        https://github.com/rivo/tview/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gdamore/tcell/v2)
BuildRequires:  go(github.com/lucasb-eyer/go-colorful)
BuildRequires:  go(github.com/rivo/uniseg)

Provides:       go(github.com/rivo/tview) = %{version}

Requires:       go(github.com/gdamore/tcell/v2)
Requires:       go(github.com/lucasb-eyer/go-colorful)
Requires:       go(github.com/rivo/uniseg)

%description
Tview provides commonly used, customizable components for terminal-based user
interfaces, including forms, text views, tables, trees, lists, and layouts.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
