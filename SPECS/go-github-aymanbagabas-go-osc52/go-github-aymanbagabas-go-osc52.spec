# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-osc52
%define go_import_path  github.com/aymanbagabas/go-osc52

Name:           go-github-aymanbagabas-go-osc52
Version:        2.0.1
Release:        %autorelease
Summary:        Golang terminal ANSI OSC52 wrapper. Copy text to clipboard from anywhere.
License:        MIT
URL:            https://github.com/aymanbagabas/go-osc52
#!RemoteAsset
Source0:        https://github.com/aymanbagabas/go-osc52/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/aymanbagabas/go-osc52) = %{version}

%description
A Go library to work with the ANSI OSC52 (https://invisible-
island.net/xterm/ctlseqs/ctlseqs.html#h3-Operating-System-Commands)
terminal sequence.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
