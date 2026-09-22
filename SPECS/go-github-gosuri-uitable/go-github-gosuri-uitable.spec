# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           uitable
%define go_import_path  github.com/gosuri/uitable

Name:           go-github-gosuri-uitable
Version:        0.0.4
Release:        %autorelease
Summary:        Provides a decorator for formating data as a table
License:        MIT
URL:            https://github.com/gosuri/uitable
VCS:            git:https://github.com/gosuri/uitable.git
#!RemoteAsset:  sha256:7b496d0c8df70ef7ab546081174ad9994917bf4be49f0420079ecc3c66355875
Source0:        https://github.com/gosuri/uitable/archive/v0.0.4.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n uitable-0.0.4

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/mattn/go-runewidth)

Provides:       go(github.com/gosuri/uitable) = %{version}

Requires:       go(github.com/fatih/color)
Requires:       go(github.com/mattn/go-runewidth)

%description
This package provides the github.com/gosuri/uitable Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
