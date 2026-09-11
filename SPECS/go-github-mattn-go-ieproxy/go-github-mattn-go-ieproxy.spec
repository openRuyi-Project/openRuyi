# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ieproxy
%define go_import_path  github.com/mattn/go-ieproxy

Name:           go-github-mattn-go-ieproxy
Version:        0.0.12
Release:        %autorelease
Summary:        Retrieve system proxy parameters from Go
License:        MIT
URL:            https://github.com/mattn/go-ieproxy
#!RemoteAsset:  sha256:fb4d07d0161b47716296e395de4998640357769484fc18367e3e4538a6331c80
Source0:        https://github.com/mattn/go-ieproxy/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/mattn/go-ieproxy) = %{version}

Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)

%description
go-ieproxy retrieves the system HTTP proxy configuration. On Windows
it reads Internet Explorer proxy settings.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
