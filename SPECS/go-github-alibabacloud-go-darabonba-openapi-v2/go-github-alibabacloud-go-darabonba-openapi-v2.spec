# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           darabonba-openapi
%define go_import_path  github.com/alibabacloud-go/darabonba-openapi/v2

Name:           go-github-alibabacloud-go-darabonba-openapi-v2
Version:        2.0.4
Release:        %autorelease
Summary:        Darabonba OpenAPI runtime for Go
License:        Apache-2.0
URL:            https://github.com/alibabacloud-go/darabonba-openapi
#!RemoteAsset:  sha256:b2c4bd24f883fff8b9cc13135e8cc3605641250bb8eabfb0b3c513c41f80f186
Source0:        https://github.com/alibabacloud-go/darabonba-openapi/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alibabacloud-go/alibabacloud-gateway-spi)
BuildRequires:  go(github.com/alibabacloud-go/openapi-util)
BuildRequires:  go(github.com/alibabacloud-go/tea)
BuildRequires:  go(github.com/alibabacloud-go/tea-utils/v2)
BuildRequires:  go(github.com/alibabacloud-go/tea-xml)
BuildRequires:  go(github.com/aliyun/credentials-go)
BuildRequires:  go(github.com/clbanning/mxj/v2)
BuildRequires:  go(github.com/niemeyer/pretty)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/client) = %{version}

Requires:       go(github.com/alibabacloud-go/alibabacloud-gateway-spi)
Requires:       go(github.com/alibabacloud-go/openapi-util)
Requires:       go(github.com/alibabacloud-go/tea)
Requires:       go(github.com/alibabacloud-go/tea-utils/v2)
Requires:       go(github.com/alibabacloud-go/tea-xml)
Requires:       go(github.com/aliyun/credentials-go)

%description
Darabonba OpenAPI provides the common runtime used by Alibaba Cloud Go SDKs.

%files
%doc README.md README-CN.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
