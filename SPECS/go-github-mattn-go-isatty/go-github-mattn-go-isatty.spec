# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-isatty
%define go_import_path  github.com/mattn/go-isatty

Name:           go-github-mattn-go-isatty
Version:        0.0.20
Release:        %autorelease
Summary:        isatty for golang
License:        MIT
URL:            https://github.com/mattn/go-isatty
#!RemoteAsset
Source0:        https://github.com/mattn/go-isatty/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/mattn/go-isatty) = %{version}

Requires:       go(golang.org/x/sys)

%description
Golang library to implementation isatty interface

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
