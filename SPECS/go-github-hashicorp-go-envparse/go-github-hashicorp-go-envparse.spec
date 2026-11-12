# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-envparse
%define go_import_path  github.com/hashicorp/go-envparse

Name:           go-github-hashicorp-go-envparse
Version:        0.1.0
Release:        %autorelease
Summary:        Go parser for environment variable files
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-envparse
#!RemoteAsset:  sha256:43145bea3ebce840db30293679f592665d3b10184b2ccf425f71e425b6b928e5
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/go-envparse) = %{version}

%description
Go library for parsing environment variable files and values.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
