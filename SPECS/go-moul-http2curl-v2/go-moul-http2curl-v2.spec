# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           http2curl
%define go_import_path  moul.io/http2curl/v2

Name:           go-moul-http2curl-v2
Version:        2.3.0
Release:        %autorelease
Summary:        Convert Go HTTP requests to curl commands
License:        Apache-2.0 OR MIT
URL:            https://github.com/moul/http2curl
#!RemoteAsset:  sha256:ed6fd573dd1908d81cea464747d75a66bb4464f92dbf0ccc1a91491ca2edd31c
Source0:        https://github.com/moul/http2curl/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(moul.io/http2curl/v2) = %{version}

%description
http2curl converts Go HTTP requests into equivalent curl commands,
including request bodies and headers.

%files
%doc README.md
%license COPYRIGHT LICENSE-APACHE
%license LICENSE-MIT
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
