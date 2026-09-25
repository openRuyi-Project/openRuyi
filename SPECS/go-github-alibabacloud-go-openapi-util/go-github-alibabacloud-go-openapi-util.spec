# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           openapi-util
%define go_import_path  github.com/alibabacloud-go/openapi-util

Name:           go-github-alibabacloud-go-openapi-util
Version:        0.1.0
Release:        %autorelease
Summary:        OpenAPI utilities for Alibaba Cloud Go SDKs
License:        Apache-2.0
URL:            https://github.com/alibabacloud-go/openapi-util
#!RemoteAsset:  sha256:2a8418a0d9201477ba7df5763bd16513caa2c1cf94645398becb96cafc030c38
Source0:        https://github.com/alibabacloud-go/openapi-util/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alibabacloud-go/tea)
BuildRequires:  go(github.com/alibabacloud-go/tea-utils)
BuildRequires:  go(github.com/tjfoc/gmsm)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/service) = %{version}

Requires:       go(github.com/alibabacloud-go/tea)
Requires:       go(github.com/alibabacloud-go/tea-utils)
Requires:       go(github.com/tjfoc/gmsm)

%description
Utilities for handling Alibaba Cloud OpenAPI requests and responses.

%files
%doc README.md README-CN.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
