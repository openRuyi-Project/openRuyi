# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logging
%define go_import_path  github.com/pion/logging

Name:           go-github-pion-logging
Version:        0.2.2
Release:        %autorelease
Summary:        The Pion logging library
License:        MIT
URL:            https://github.com/pion/logging
#!RemoteAsset:  sha256:9e06f3dbf6f4fcf0e61e3a6406cac898fe3df86cb906bc9d73c7c4b466f0a9d6
Source0:        https://github.com/pion/logging/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pion/logging) = %{version}

%description
The Pion logging library

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
