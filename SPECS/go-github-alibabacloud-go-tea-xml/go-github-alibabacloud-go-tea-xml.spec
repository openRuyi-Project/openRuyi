# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tea-xml
%define go_import_path  github.com/alibabacloud-go/tea-xml

Name:           go-github-alibabacloud-go-tea-xml
Version:        1.1.2
Release:        %autorelease
Summary:        XML utilities for Alibaba Cloud Go SDKs
License:        Apache-2.0
URL:            https://github.com/alibabacloud-go/tea-xml
#!RemoteAsset:  sha256:58df737167221e313e350f396c7e20ad3b437cec63442730807a29f1f80efa20
Source0:        https://github.com/alibabacloud-go/tea-xml/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alibabacloud-go/tea)
BuildRequires:  go(github.com/clbanning/mxj/v2)
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
Requires:       go(github.com/clbanning/mxj/v2)

%description
XML encoding and decoding helpers for Alibaba Cloud Go SDKs.

%files
%doc README.md README-CN.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
