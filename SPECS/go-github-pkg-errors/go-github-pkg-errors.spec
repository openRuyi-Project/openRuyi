# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errors
%define go_import_path  github.com/pkg/errors

Name:           go-github-pkg-errors
Version:        0.9.1
Release:        %autorelease
Summary:        Simple error handling primitives
License:        BSD-2-Clause
URL:            https://github.com/pkg/errors
#!RemoteAsset
Source0:        https://github.com/pkg/errors/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://sources.debian.org/src/golang-github-pkg-errors/0.9.1-3/debian/patches/0001-Fix-FTBFS-with-golang-1.21.patch
Patch0:         2000-Fix-FTBFS-with-golang-1.21.patch

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pkg/errors) = %{version}

%description
This package provides simple error handling primitives.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
