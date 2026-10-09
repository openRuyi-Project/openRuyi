# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cos-go-sdk-v5
%define go_import_path  github.com/tencentyun/cos-go-sdk-v5

Name:           go-github-tencentyun-cos-go-sdk-v5
Version:        0.7.24
Release:        %autorelease
Summary:        Tencent Cloud Object Storage SDK for Go
License:        MIT
URL:            https://github.com/tencentyun/cos-go-sdk-v5
#!RemoteAsset:  sha256:39e7368c9d7b082b15e8589becd2c105d3af1d251490832ca89c4d5d64f11ae6
Source0:        https://github.com/tencentyun/cos-go-sdk-v5/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# Keep multipart upload tests on slower architectures by fixing a race in
# the upstream test server's retry counter map.
Patch2000:      2000-synchronize-multipart-test-retries.patch
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/mozillazg/go-httpheader)

Provides:       go(github.com/tencentyun/cos-go-sdk-v5) = %{version}

Requires:       go(github.com/google/go-querystring)
Requires:       go(github.com/mozillazg/go-httpheader)

%description
This library provides the Tencent Cloud Object Storage XML API client
used by Cloudmux.

%prep -a
# The examples require unpublished credentials and two dependencies unused
# by the public library. The CI-only test package also requires credentials.
rm -rf example costesting vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
