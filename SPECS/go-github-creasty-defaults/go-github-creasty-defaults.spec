# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           defaults
%define go_import_path  github.com/creasty/defaults

Name:           go-github-creasty-defaults
Version:        1.11.0
Release:        %autorelease
Summary:        Initialize Go structs with default values
License:        MIT
URL:            https://github.com/creasty/defaults
#!RemoteAsset:  sha256:97bbc6b7d85506d0ba6824518297a5f21e36185b8ff50e17691aa59f39d414f1
Source0:        https://github.com/creasty/defaults/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Defaults initializes struct fields from default-value tags and supports
nested values, custom setters, and unmarshaling interfaces.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
