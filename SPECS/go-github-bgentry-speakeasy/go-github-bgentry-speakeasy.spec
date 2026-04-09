# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           speakeasy
%define go_import_path  github.com/bgentry/speakeasy

Name:           go-github-bgentry-speakeasy
Version:        0.2.0
Release:        %autorelease
Summary:        cross-platform Golang helpers for reading password input without cgo
License:        MIT AND Apache-2.0
URL:            https://github.com/bgentry/speakeasy
#!RemoteAsset
Source0:        https://github.com/bgentry/speakeasy/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bgentry/speakeasy) = %{version}

%description
This package provides cross-platform Go (#golang) helpers for taking
user
input from the terminal while not echoing the input back (similar to
getpasswd). The package uses syscalls to avoid any dependence on cgo,
and is therefore compatible with cross-compiling.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
