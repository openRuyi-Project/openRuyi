# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-windows-terminal-sequences
%define go_import_path  github.com/konsorten/go-windows-terminal-sequences

Name:           go-github-konsorten-go-windows-terminal-sequences
Version:        1.0.3
Release:        %autorelease
Summary:        Enable Windows terminal color support in Go
License:        MIT
URL:            https://github.com/konsorten/go-windows-terminal-sequences
#!RemoteAsset:  sha256:0fe1169bb05476f0a3270866cdd9b39b7986a1dce556f6508046ac5f0c5ad8f3
Source0:        https://github.com/konsorten/go-windows-terminal-sequences/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This library enables virtual terminal processing for color and control
sequences on supported Windows consoles.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
