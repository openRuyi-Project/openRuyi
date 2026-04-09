# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           btree
%define go_import_path  github.com/google/btree

Name:           go-github-google-btree
Version:        1.1.3
Release:        %autorelease
Summary:        BTree provides a simple, ordered, in-memory data structure for Go programs.
License:        Apache-2.0
URL:            https://github.com/google/btree
#!RemoteAsset
Source0:        https://github.com/google/btree/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/btree) = %{version}

%description
BTree implementation for Go

This package provides an in-memory B-Tree implementation for Go, useful
as an ordered, mutable data structure.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
