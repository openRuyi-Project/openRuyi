# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           renameio
%define go_import_path  github.com/google/renameio

Name:           go-github-google-renameio
Version:        1.0.1
Release:        %autorelease
Summary:        Go package for atomically replacing files
License:        Apache-2.0
URL:            https://github.com/google/renameio
#!RemoteAsset:  sha256:940b6a2f036652a375679afb880f8bb90ade33118e5fdceb3a9ac03e0a5d86b5
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/renameio) = %{version}

%description
The renameio Go package provides a way to atomically create or replace a file
or symbolic link.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
