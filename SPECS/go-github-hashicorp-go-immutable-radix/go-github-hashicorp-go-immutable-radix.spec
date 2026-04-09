# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-immutable-radix
%define go_import_path  github.com/hashicorp/go-immutable-radix

Name:           go-github-hashicorp-go-immutable-radix
Version:        2.1.0
Release:        %autorelease
Summary:        An immutable radix tree implementation in Golang
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-immutable-radix
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-immutable-radix/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/hashicorp/go-uuid)
BuildRequires:  go(github.com/hashicorp/golang-lru)
BuildRequires:  go(golang.org/x/exp)

Provides:       go(github.com/hashicorp/go-immutable-radix) = %{version}

Requires:       go(github.com/hashicorp/go-uuid)
Requires:       go(github.com/hashicorp/golang-lru)
Requires:       go(golang.org/x/exp)

%description
Provides the iradix package that implements an immutable radix tree
(http://en.wikipedia.org/wiki/Radix_tree). The package only provides a
single Tree implementation, optimized for sparse nodes.

As a radix tree, it provides the following:

 * O(k) operations. In many cases, this can be faster than a hash table
   since
   the hash function is an O(k) operation, and hash tables have very poor
   cache locality.
 * Minimum / Maximum value lookups
 * Ordered iteration

A tree supports using a transaction to batch multiple updates (insert,
delete) in a more efficient manner than performing each operation one at
a time.

For a mutable variant, see go-radix (https://github.com/armon/go-radix).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
