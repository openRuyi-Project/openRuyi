# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           alibabacloud-gateway-spi
%define go_import_path  github.com/alibabacloud-go/alibabacloud-gateway-spi

Name:           go-github-alibabacloud-go-alibabacloud-gateway-spi
Version:        0.0.4
Release:        %autorelease
Summary:        Alibaba Cloud gateway service provider interface
License:        Apache-2.0
URL:            https://github.com/alibabacloud-go/alibabacloud-gateway-spi
#!RemoteAsset:  sha256:1320386e8474c843425d946c43b38ed3b3c1f9215b9d5cfefacd82384faa8b2d
Source0:        https://github.com/alibabacloud-go/alibabacloud-gateway-spi/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aliyun/credentials-go)
BuildRequires:  go(github.com/alibabacloud-go/tea)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/client) = %{version}

Requires:       go(github.com/aliyun/credentials-go)
Requires:       go(github.com/alibabacloud-go/tea)

%description
This package defines the Alibaba Cloud gateway service provider interface.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
