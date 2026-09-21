# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-pointer
%define go_import_path  github.com/mattn/go-pointer

Name:           go-github-mattn-go-pointer
Version:        0.0.1
Release:        %autorelease
Summary:        Utility for safely passing Go values through C code
License:        MIT
URL:            https://github.com/mattn/go-pointer
#!RemoteAsset:  sha256:5630a863fa1c2516ea3d2eeab94274768463018778486dddebfcb0fa32ea50fb
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides a small registry for safely passing Go values through
C code when using cgo.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
