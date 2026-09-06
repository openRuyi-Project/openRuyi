# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           debug
%define go_import_path  github.com/alibabacloud-go/debug

Name:           go-github-alibabacloud-go-debug
Version:        1.0.1
Release:        %autorelease
Summary:        Debug helpers for Alibaba Cloud Go SDKs
License:        Apache-2.0
URL:            https://github.com/alibabacloud-go/debug
#!RemoteAsset:  sha256:25531ff5dd790db1dcaa004eef78e53c894fcdc161b1493049051e4be6701027
Source0:        https://github.com/alibabacloud-go/debug/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/debug) = %{version}

%description
Debug support used by Alibaba Cloud Go SDKs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
