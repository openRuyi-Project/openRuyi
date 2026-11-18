# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           structtags
%define go_import_path  github.com/ldez/structtags

Name:           go-github-ldez-structtags
Version:        0.6.1
Release:        %autorelease
Summary:        Structtags provides several ways of parsing struct tags
License:        GPL-3.0-only AND BSD-3-Clause
URL:            https://github.com/ldez/structtags
#!RemoteAsset:  sha256:2b443d1894123285b4d35823a846032dc0b0d0e06e40e892ae4e51dbe1358101
Source0:        https://github.com/ldez/structtags/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# The parser includes BSD-licensed code from the Go standard library.
#!RemoteAsset:  sha256:911f8f5782931320f5b8d1160a76365b83aea6447ee6c04fa6d5591467db9dad
Source1:        https://raw.githubusercontent.com/golang/go/go1.26.3/LICENSE#/LICENSE.golang
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fatih/structtag)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/ldez/structtags) = %{version}
Provides:       go(github.com/ldez/structtags/parser) = %{version}
Provides:       go(github.com/ldez/structtags/variant/fatih) = %{version}
Provides:       go(github.com/ldez/structtags/variant/maps/multikeys) = %{version}
Provides:       go(github.com/ldez/structtags/variant/maps/raw) = %{version}
Provides:       go(github.com/ldez/structtags/variant/maps/values) = %{version}
Provides:       go(github.com/ldez/structtags/variant/slices/raw) = %{version}
Provides:       go(github.com/ldez/structtags/variant/slices/values) = %{version}
Provides:       go(github.com/ldez/structtags/variant/structured) = %{version}

Requires:       go(github.com/fatih/structtag)

%description
Structtags provides several ways of parsing struct tags.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n structtags-%{version}
cp -p %{SOURCE1} LICENSE.golang

%files
%doc readme.md
%license LICENSE LICENSE.golang
%{go_sys_gopath}/github.com/ldez/structtags

%changelog
%autochangelog
