# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           scram
%define go_import_path  github.com/xdg-go/scram

Name:           go-github-xdg-go-scram
Version:        1.1.2
Release:        %autorelease
Summary:        SCRAM authentication for Go
License:        Apache-2.0
URL:            https://github.com/xdg-go/scram
#!RemoteAsset:  sha256:66e8e73966d87b7266957dbe421313b335c455907a36b0115ea81bdf7d1c9d19
Source0:        https://github.com/xdg-go/scram/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/xdg-go/pbkdf2)
BuildRequires:  go(github.com/xdg-go/stringprep)

Provides:       go(github.com/xdg-go/scram) = %{version}

Requires:       go(github.com/xdg-go/pbkdf2)
Requires:       go(github.com/xdg-go/stringprep)

%description
SCRAM implements client and server authentication using salted challenge
responses as specified by RFC 5802, including SHA-1 and SHA-256 variants.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
