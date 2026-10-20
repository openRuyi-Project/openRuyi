# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-spin
%define go_import_path  github.com/tj/go-spin

Name:           go-github-tj-go-spin
Version:        1.1.0
Release:        %autorelease
Summary:        Terminal spinner library for Go
License:        MIT
URL:            https://github.com/tj/go-spin
#!RemoteAsset:  sha256:4a27a6b93300897f88f55cec35f7b7fb9bc32cdf1cfd6a4e80a22981fa300c0c
Source0:        https://github.com/tj/go-spin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-spin-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/tj/go-spin) = %{version}

%description
This package provides configurable terminal spinners and animation
frames for Go applications.

%files
%license Readme.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
