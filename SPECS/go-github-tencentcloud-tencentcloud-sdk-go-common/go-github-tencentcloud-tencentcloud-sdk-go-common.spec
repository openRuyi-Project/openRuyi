# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tencentcloud-sdk-go
%define go_import_path  github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common

Name:           go-github-tencentcloud-tencentcloud-sdk-go-common
Version:        1.0.413
Release:        %autorelease
Summary:        Common client library for Tencent Cloud Go SDK
License:        Apache-2.0
URL:            https://github.com/TencentCloud/tencentcloud-sdk-go
#!RemoteAsset:  sha256:193994747810d3f4426b0c1177382c21bf1ed629dede99aee48a4826a896787b
Source0:        https://github.com/TencentCloud/tencentcloud-sdk-go/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common) = %{version}

%description
Shared authentication, request, response, and client code used by
Tencent Cloud SDK services.

%prep -a
# The upstream tag includes independently versioned service modules.
# Install only the common module at its actual Go import path.
cp -a tencentcloud/common/. .
rm -rf tencentcloud examples testing doc.go

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
