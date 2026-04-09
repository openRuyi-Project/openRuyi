# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           set
%define go_import_path  github.com/xtgo/set

Name:           go-github-xtgo-set
Version:        1.0.0
Release:        %autorelease
Summary:        General, type-safe, non-allocating set-operations for any sort.Interface
License:        BSD-2-Clause
URL:            https://github.com/xtgo/set
#!RemoteAsset
Source0:        https://github.com/xtgo/set/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/xtgo/set) = %{version}

%description
Package set provides type-safe, polymorphic mathematical set operations
that operate on any sort.Interface implementation.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
