# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           text
%define go_import_path  github.com/kr/text

Name:           go-github-kr-text
Version:        0.2.0
Release:        %autorelease
Summary:        Miscellaneous functions for formatting text
License:        MIT
URL:            https://github.com/kr/text
#!RemoteAsset
Source0:        https://github.com/kr/text/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/creack/pty)

Provides:       go(github.com/kr/text) = %{version}

Requires:       go(github.com/creack/pty)

%description
This is a Go package for manipulating paragraphs of text.

%files
%license License
%doc Readme
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
