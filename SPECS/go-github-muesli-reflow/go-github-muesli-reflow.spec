# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           reflow
%define go_import_path  github.com/muesli/reflow

Name:           go-github-muesli-reflow
Version:        0.3.0
Release:        %autorelease
Summary:        A collection of (ANSI-sequence aware) text reflow operations & algorithms
License:        MIT
URL:            https://github.com/muesli/reflow
#!RemoteAsset
Source0:        https://github.com/muesli/reflow/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mattn/go-runewidth)

Provides:       go(github.com/muesli/reflow) = %{version}

Requires:       go(github.com/mattn/go-runewidth)

%description
reflow

[Image: Latest Release]
A collection of ANSI-aware methods and io.Writers helping you to
transform blocks of text. This means you can still style your terminal
output with ANSI escape sequences without them affecting the reflow
operations & algorithms.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
