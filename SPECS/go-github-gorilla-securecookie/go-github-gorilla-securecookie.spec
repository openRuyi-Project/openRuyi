# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           securecookie
%define go_import_path  github.com/gorilla/securecookie

Name:           go-github-gorilla-securecookie
Version:        1.1.2
Release:        %autorelease
Summary:        Authenticated and encrypted cookie values for Go
License:        BSD-3-Clause
URL:            https://github.com/gorilla/securecookie
#!RemoteAsset:  sha256:6a95562e0bf0b29033bfe75a55a28ca547d76b5472c0865f38ba9d8eb44c2ddf
Source0:        https://github.com/gorilla/securecookie/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/gofuzz)

Provides:       go(github.com/gorilla/securecookie) = %{version}

%description
Securecookie encodes authenticated and optionally encrypted values for HTTP
cookies in Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
