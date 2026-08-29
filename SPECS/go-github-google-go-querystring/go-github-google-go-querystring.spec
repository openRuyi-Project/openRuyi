# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-querystring
%define go_import_path  github.com/google/go-querystring

Name:           go-github-google-go-querystring
Version:        1.2.0
Release:        %autorelease
Summary:        URL query string encoder for Go structs
License:        BSD-3-Clause
URL:            https://github.com/google/go-querystring
#!RemoteAsset:  sha256:d28780f21377085732bc2925ee1192a29f3e4c3fab82316a714a6e14fa52e42a
Source0:        https://github.com/google/go-querystring/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(github.com/google/go-querystring) = %{version}

%description
go-querystring encodes Go structs into URL query parameters.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
