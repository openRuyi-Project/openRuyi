# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tea-utils
%define go_import_path  github.com/alibabacloud-go/tea-utils/v2

Name:           go-github-alibabacloud-go-tea-utils-v2
Version:        2.0.1
Release:        %autorelease
Summary:        Version 2 Darabonba utility library for Go
License:        Apache-2.0
URL:            https://github.com/alibabacloud-go/tea-utils
#!RemoteAsset:  sha256:e93750623a9a07accba64b51adb1e33bef37778b74eaa84864178ebb910f6903
Source0:        https://github.com/alibabacloud-go/tea-utils/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alibabacloud-go/tea)
BuildRequires:  go(golang.org/x/net)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/service) = %{version}

Requires:       go(github.com/alibabacloud-go/tea)

%description
Version 2 of the common utility functions for Alibaba Cloud Go SDKs.

%files
%doc README.md README-CN.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
