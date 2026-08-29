# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ovh
%define go_import_path  github.com/ovh/go-ovh

Name:           go-github-ovh-go-ovh
Version:        1.9.0
Release:        %autorelease
Summary:        Go client for OVHcloud APIs
License:        BSD-3-Clause
URL:            https://github.com/ovh/go-ovh
#!RemoteAsset:  sha256:146b1fa7e9c88d199c7113356ea2dca9aa7b78e4a1f07529da3565f3ff0712a5
Source0:        https://github.com/ovh/go-ovh/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Accept stable OAuth2 status-code context across dependency versions.
# https://github.com/ovh/go-ovh/pull/97
Patch2000:      2000-tolerate-oauth2-status-text-changes.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/jarcoal/httpmock)
BuildRequires:  go(github.com/maxatome/go-testdeep)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(gopkg.in/ini.v1)

Provides:       go(github.com/ovh/go-ovh) = %{version}

Requires:       go(golang.org/x/oauth2)
Requires:       go(gopkg.in/ini.v1)

%description
This package provides a lightweight Go client for OVHcloud APIs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
