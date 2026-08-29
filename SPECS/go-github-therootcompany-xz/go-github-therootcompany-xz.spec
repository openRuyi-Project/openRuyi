# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xz
%define go_import_path  github.com/therootcompany/xz

Name:           go-github-therootcompany-xz
Version:        1.0.1
Release:        %autorelease
Summary:        XZ decompression implemented natively in Go
License:        CC0-1.0
URL:            https://github.com/therootcompany/xz
#!RemoteAsset:  sha256:4ab011bbeca0f93cf40e40fd7a90f9d75c820dc630041016b47c4741541ab1b6
Source0:        https://github.com/therootcompany/xz/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/therootcompany/xz) = %{version}

%description
Package xz implements XZ decompression natively in Go.

%files
%doc AUTHORS README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
