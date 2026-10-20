# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-aws-auth
%define go_import_path  github.com/smartystreets/go-aws-auth
%global commit_id       0c1422d1fdb9fef5a1ad5b2e13ac663467eb767e

Name:           go-github-smartystreets-go-aws-auth
Version:        0+git20261020.0c1422d
Release:        %autorelease
Summary:        AWS HTTP request signing library for Go
License:        MIT
URL:            https://github.com/smartystreets/go-aws-auth
#!RemoteAsset:  sha256:5a014b4cbb3fbe11075d813462eee433b2ca6a175227088245d19387f11b94e8
Source0:        https://github.com/smartystreets/go-aws-auth/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Automatic signing selects SigV4, while four upstream tests still expect V2/V3.
Patch2000:      2000-align-signing-tests-with-service-map.patch

BuildOption(prep):  -n go-aws-auth-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/smartystreets/assertions)
BuildRequires:  go(github.com/smartystreets/gunit)

Provides:       go(github.com/smartystreets/go-aws-auth) = %{version}

%description
Go-AWS-Auth signs HTTP requests using AWS Signature Versions 2, 3, and 4.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
