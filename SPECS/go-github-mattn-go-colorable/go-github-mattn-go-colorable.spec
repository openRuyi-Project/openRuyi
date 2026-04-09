# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-colorable
%define go_import_path  github.com/mattn/go-colorable

Name:           go-github-mattn-go-colorable
Version:        0.1.14
Release:        %autorelease
Summary:        Colorable writer for windows
License:        MIT
URL:            https://github.com/mattn/go-colorable
#!RemoteAsset
Source0:        https://github.com/mattn/go-colorable/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mattn/go-isatty)

Provides:       go(github.com/mattn/go-colorable) = %{version}

Requires:       go(github.com/mattn/go-isatty)

%description
Colorable writer for windows.

For example, most of logger packages doesn't show colors on windows. (I
know we can do it with ansicon. But I don't want.) This package is
possible to handle escape sequence for ansi color on windows.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
