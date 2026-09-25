# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sts-20150401
%define go_import_path  github.com/alibabacloud-go/sts-20150401/v2

Name:           go-github-alibabacloud-go-sts-20150401-v2
Version:        2.0.1
Release:        %autorelease
Summary:        Alibaba Cloud Security Token Service SDK
License:        Apache-2.0
URL:            https://github.com/alibabacloud-go/sts-20150401
#!RemoteAsset:  sha256:c2ecf286b5c57cc7eb405f4541c53573cf8d87984fbec8f2b20c0640059eb309
Source0:        https://github.com/alibabacloud-go/sts-20150401/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alibabacloud-go/darabonba-openapi/v2)
BuildRequires:  go(github.com/alibabacloud-go/endpoint-util)
BuildRequires:  go(github.com/alibabacloud-go/openapi-util)
BuildRequires:  go(github.com/alibabacloud-go/tea)
BuildRequires:  go(github.com/alibabacloud-go/tea-utils/v2)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/client) = %{version}

Requires:       go(github.com/alibabacloud-go/darabonba-openapi/v2)
Requires:       go(github.com/alibabacloud-go/endpoint-util)
Requires:       go(github.com/alibabacloud-go/openapi-util)
Requires:       go(github.com/alibabacloud-go/tea)
Requires:       go(github.com/alibabacloud-go/tea-utils/v2)

%description
Go SDK for Alibaba Cloud Security Token Service.

%files
%doc README.md README-CN.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
