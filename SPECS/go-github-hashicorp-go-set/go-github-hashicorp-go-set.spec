# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-set
%define go_import_path  github.com/hashicorp/go-set

Name:           go-github-hashicorp-go-set
Version:        3.0.1
Release:        %autorelease
Summary:        The go-set package provides generic Set implementations for Go, including HashSet for types with a Hash() function and TreeSet for orderable data
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-set
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-set/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/shoenig/test)

Provides:       go(github.com/hashicorp/go-set) = %{version}

Requires:       go(github.com/shoenig/test)

%description
The go-set package includes Set for types that satisfy
the comparable constraint. Uniqueness of a set elements
is guaranteed via shallow comparison (result of == operator).

Note: if pointers or structs with pointer fields are
stored in the Set, they will be compared in the sense
of pointer addresses, not in the sense of referenced values.
Due to this fact the Set type is recommended to be used with
builtin types like string, int, or simple struct types with
no pointers. Set usage with pointers or structs with pointer
is also possible if shallow equality is acceptable.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
