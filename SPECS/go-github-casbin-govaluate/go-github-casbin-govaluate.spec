# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           govaluate
%define go_import_path  github.com/casbin/govaluate

Name:           go-github-casbin-govaluate
Version:        1.10.0
Release:        %autorelease
Summary:        Expression evaluator for Go
License:        MIT
URL:            https://github.com/casbin/govaluate
#!RemoteAsset:  sha256:a726f9f69964024c399cd67f2e0b7a0ed43d861dd73455ebc0076db98d843e61
Source0:        https://github.com/casbin/govaluate/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Govaluate evaluates arbitrary C-like expressions in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
