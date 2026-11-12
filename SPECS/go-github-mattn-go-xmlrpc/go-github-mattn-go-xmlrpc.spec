# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-xmlrpc
%define go_import_path  github.com/mattn/go-xmlrpc

Name:           go-github-mattn-go-xmlrpc
Version:        0.0.3
Release:        %autorelease
Summary:        Go XML-RPC client library
License:        MIT
URL:            https://github.com/mattn/go-xmlrpc
#!RemoteAsset:  sha256:4b1eef421a5f79cc0e6c8e7939de3c5fc1f0d8b27ede560c4d89e580e22e2564
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mattn/go-xmlrpc) = %{version}

%description
Go client library for encoding and decoding XML-RPC calls.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
