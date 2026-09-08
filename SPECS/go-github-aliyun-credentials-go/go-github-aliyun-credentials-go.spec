# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           credentials-go
%define go_import_path  github.com/aliyun/credentials-go
# Integration tests require live Alibaba Cloud credentials.
%define go_test_exclude %{go_import_path}/integration

Name:           go-github-aliyun-credentials-go
Version:        1.1.2
Release:        %autorelease
Summary:        Alibaba Cloud credentials provider for Go
License:        Apache-2.0
URL:            https://github.com/aliyun/credentials-go
#!RemoteAsset:  sha256:7aa778580b22f960bcb53542a02e1e1c08c0f1d1278a8986bee357d340d859b8
Source0:        https://github.com/aliyun/credentials-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alibabacloud-go/debug)
BuildRequires:  go(github.com/alibabacloud-go/tea)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/ini.v1)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/credentials) = %{version}
Provides:       go(%{go_import_path}/credentials/request) = %{version}
Provides:       go(%{go_import_path}/credentials/response) = %{version}
Provides:       go(%{go_import_path}/credentials/utils) = %{version}

Requires:       go(github.com/alibabacloud-go/debug)
Requires:       go(github.com/alibabacloud-go/tea)
Requires:       go(gopkg.in/ini.v1)

%description
Alibaba Cloud Credentials for Go manages credential providers and credential
refreshing for Alibaba Cloud SDK clients.

%files
%doc README.md README-CN.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
