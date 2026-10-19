# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pointer
%define go_import_path  github.com/AlekSi/pointer

Name:           go-github-aleksi-pointer
Version:        1.2.0
Release:        %autorelease
Summary:        Helpers for converting Go values and pointers
License:        MIT
URL:            https://github.com/AlekSi/pointer
#!RemoteAsset:  sha256:903cd9d0805d1cd2f462fcd8b51ab20b76d5455953a2a31babe206ff9f3a11bb
Source0:        https://github.com/AlekSi/pointer/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Pointer provides conversion helpers between pointers and values for Go
built-in types and arbitrary types through generics.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
