# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testcerts
%define go_import_path  github.com/madflojo/testcerts

Name:           go-github-madflojo-testcerts
Version:        1.5.0
Release:        %autorelease
Summary:        Test certificate generator for Go
License:        MIT
URL:            https://github.com/madflojo/testcerts
#!RemoteAsset:  sha256:9eac2e6826b6e5bac4e20b20dad04b8f6dd9214a3104b7535f4c05846138971b
Source0:        https://github.com/madflojo/testcerts/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides Go helpers for generating test certificates.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
