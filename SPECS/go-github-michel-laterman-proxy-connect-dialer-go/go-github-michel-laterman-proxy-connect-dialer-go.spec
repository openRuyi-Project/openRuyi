# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           proxy-connect-dialer-go
%define go_import_path  github.com/michel-laterman/proxy-connect-dialer-go

Name:           go-github-michel-laterman-proxy-connect-dialer-go
Version:        0.1.0
Release:        %autorelease
Summary:        HTTP CONNECT proxy dialer for Go
License:        Apache-2.0
URL:            https://github.com/michel-laterman/proxy-connect-dialer-go
#!RemoteAsset:  sha256:d2d6672bf0aa5db4b03ce124967f8bea5623dbc67225426a4b6e62a04c0c5bd6
Source0:        https://github.com/michel-laterman/proxy-connect-dialer-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides a Go dialer that connects through HTTP CONNECT proxies.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
