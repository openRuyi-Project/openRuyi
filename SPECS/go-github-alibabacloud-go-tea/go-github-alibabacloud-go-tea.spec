# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tea
%define go_import_path  github.com/alibabacloud-go/tea

Name:           go-github-alibabacloud-go-tea
Version:        1.1.19
Release:        %autorelease
Summary:        Darabonba runtime library for Go
License:        Apache-2.0
URL:            https://github.com/alibabacloud-go/tea
#!RemoteAsset:  sha256:80823505a632ee0f7065889b257985d2959deb758a04afe9907f2dcd16da992b
Source0:        https://github.com/alibabacloud-go/tea/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alibabacloud-go/debug)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(golang.org/x/net)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/tea) = %{version}
Provides:       go(%{go_import_path}/utils) = %{version}

Requires:       go(github.com/alibabacloud-go/debug)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(golang.org/x/net)

%description
Tea is the Darabonba runtime library used by Alibaba Cloud Go SDKs.

%files
%doc README.md README-CN.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
