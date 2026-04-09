# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-bexpr
%define go_import_path  github.com/hashicorp/go-bexpr

Name:           go-github-hashicorp-go-bexpr
Version:        0.1.15
Release:        %autorelease
Summary:        Generic boolean expression evaluation in Go
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-bexpr
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-bexpr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mitchellh/pointerstructure)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/hashicorp/go-bexpr) = %{version}

Requires:       go(github.com/mitchellh/pointerstructure)
Requires:       go(github.com/stretchr/testify)

%description
bexpr is a Go (golang) library to provide generic boolean expression
evaluation and filtering for Go data structures and maps. Under the
hood, bexpr uses pointerstructure
(https://github.com/mitchellh/pointerstructure), meaning that any path
within a map or structure that can be expressed via that library can be
used with bexpr. This also means that you can use the custom bexpr
dotted syntax (kept mainly for backwards compatibility) to select values
in expressions, or, by enclosing the selectors in quotes, you can use
JSON Pointer (https://tools.ietf.org/html/rfc6901) syntax to select
values in expressions.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
