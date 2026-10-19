# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kagi-openapi-golang
%define go_import_path  github.com/kagisearch/kagi-openapi-golang
%define commit_id       96575e864d628e603b5d2faf14a6a2051108ef6d

Name:           go-github-kagisearch-kagi-openapi-golang
Version:        0+git20261019.96575e8
Release:        %autorelease
Summary:        Go API client for openapi
License:        Apache-2.0
URL:            https://github.com/kagisearch/kagi-openapi-golang
#!RemoteAsset:  sha256:f3db0af267a21c7be78cc6e43befb784d5ccfd71dd4810787551ba62c74ebc76
Source0:        https://github.com/kagisearch/kagi-openapi-golang/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/kagisearch/kagi-openapi-golang) = %{version}

%description
The Kagi API provides programmatic access to data that powers our search
results & more.

%files
%doc README.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
