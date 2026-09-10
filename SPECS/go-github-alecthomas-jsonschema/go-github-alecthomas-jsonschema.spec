# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonschema
%define go_import_path  github.com/alecthomas/jsonschema
%define commit_id       9eeeec9d044b28001bc1a5aaf61333d60ac33a64

Name:           go-github-alecthomas-jsonschema
Version:        0+git20260817.9eeeec9
Release:        %autorelease
Summary:        Generate JSON schemas from Go types
License:        MIT
URL:            https://github.com/alecthomas/jsonschema
#!RemoteAsset:  sha256:afa702dc38e3ce8893cfa507c27b40955eb533784c76ff671dc9ea9a4f9c2a4a
Source0:        https://github.com/alecthomas/jsonschema/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/iancoleman/orderedmap)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/iancoleman/orderedmap)

%description
Jsonschema uses reflection to generate JSON schemas from Go types. The project
is retained for consumers that have not migrated to its successor.

%files
%doc README.md
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
