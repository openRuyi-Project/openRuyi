# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xpath
%define go_import_path  github.com/antchfx/xpath

Name:           go-github-antchfx-xpath
Version:        1.3.8
Release:        %autorelease
Summary:        XPath expression implementation for Go
License:        MIT
URL:            https://github.com/antchfx/xpath
#!RemoteAsset:  sha256:fa32cbc5c987688c5d9db1dd5842adf45cd2b2867b824ddc70d9cc5aa2b50159
Source0:        https://codeload.github.com/antchfx/xpath/tar.gz/refs/tags/v%{version}#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package evaluates XPath expressions against XML, HTML, and other tree
structured documents.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
