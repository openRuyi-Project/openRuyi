# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           endpoint-util
%define go_import_path  github.com/alibabacloud-go/endpoint-util

Name:           go-github-alibabacloud-go-endpoint-util
Version:        1.1.0
Release:        %autorelease
Summary:        Endpoint utilities for Alibaba Cloud Go SDKs
License:        Apache-2.0
URL:            https://github.com/alibabacloud-go/endpoint-util
#!RemoteAsset:  sha256:e95f1d79e128bc774c7cd87880400eb566dae89f036b4b52643ce97286b2c9c0
Source0:        https://github.com/alibabacloud-go/endpoint-util/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alibabacloud-go/tea)
BuildRequires:  go(github.com/yuin/goldmark)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/service) = %{version}

Requires:       go(github.com/alibabacloud-go/tea)

%description
Endpoint selection and resolution helpers for Alibaba Cloud Go SDKs.

%files
%doc README.md README-CN.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
