# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dedent
%define go_import_path  github.com/lithammer/dedent

Name:           go-github-lithammer-dedent
Version:        1.1.0
Release:        %autorelease
Summary:        Removes common leading whitespace from multiline strings
License:        MIT
URL:            https://github.com/lithammer/dedent
#!RemoteAsset:  sha256:aee382778063c582f69f4b8dd7f0e8bcb5ff827c61447108944aa2024954de16
Source0:        https://github.com/lithammer/dedent/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/lithammer/dedent) = %{version}

%description
Dedent removes common leading whitespace from multiline strings while
preserving their relative indentation.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
