# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tea-utils
%define go_import_path  github.com/alibabacloud-go/tea-utils

Name:           go-github-alibabacloud-go-tea-utils
Version:        1.4.5
Release:        %autorelease
Summary:        Darabonba utility library for Go
License:        Apache-2.0
URL:            https://github.com/alibabacloud-go/tea-utils
#!RemoteAsset:  sha256:a324d0a20f0a18f069af3671e120f30b1870f0df67c000d7e89683c76121fb98
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
Common utility functions for Alibaba Cloud Darabonba Go SDKs.

%files
%doc README.md README-CN.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
