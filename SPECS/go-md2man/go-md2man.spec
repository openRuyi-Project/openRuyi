# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-md2man
%define go_import_path  github.com/cpuguy83/go-md2man/v2

Name:           go-md2man
Version:        2.0.7
Release:        %autorelease
Summary:        Converts markdown into roff (man pages).
License:        MIT
URL:            https://github.com/cpuguy83/go-md2man
#!RemoteAsset
Source0:        https://github.com/cpuguy83/go-md2man/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/russross/blackfriday/v2)

%description
go-md2man Converts markdown into roff (man pages).

%package     -n go-github-cpuguy83-go-md2man-v2
Summary:        Converts markdown into roff (man pages) (Source).
Provides:       go(github.com/cpuguy83/go-md2man/v2) = %{version}
Requires:       go(github.com/russross/blackfriday/v2)

%description -n go-github-cpuguy83-go-md2man-v2
go-md2man Converts markdown into roff (man pages).

This package contains the source for go-md2man version 2.

# This is for the source package
%install -a
%buildsystem_golangmodules_install

%files
%license LICENSE*
%doc README*
%{_bindir}/%{_name}

%files -n go-github-cpuguy83-go-md2man-v2
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
