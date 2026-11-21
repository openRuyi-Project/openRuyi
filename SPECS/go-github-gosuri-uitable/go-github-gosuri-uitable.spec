# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           uitable
%define go_import_path  github.com/gosuri/uitable

Name:           go-github-gosuri-uitable
Version:        0.0.4
Release:        %autorelease
Summary:        Format tabular data for terminal output in Go
License:        MIT
URL:            https://github.com/gosuri/uitable
#!RemoteAsset:  sha256:7b496d0c8df70ef7ab546081174ad9994917bf4be49f0420079ecc3c66355875
Source0:        https://github.com/gosuri/uitable/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/mattn/go-runewidth)

Provides:       go(github.com/gosuri/uitable) = %{version}

Requires:       go(github.com/fatih/color)
Requires:       go(github.com/mattn/go-runewidth)

%description
Format tabular data for terminal output in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
