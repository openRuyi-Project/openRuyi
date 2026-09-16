# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ulid
%define go_import_path  github.com/oklog/ulid

Name:           go-github-oklog-ulid
Version:        1.3.1
Release:        %autorelease
Summary:        Universally Unique Lexicographically Sortable Identifier for Go
License:        Apache-2.0
URL:            https://github.com/oklog/ulid
#!RemoteAsset:  sha256:499a6ee77ca473a44ad9f11425a8f87f6c02ff1221b11f24d13bee13ce632640
Source0:        https://github.com/oklog/ulid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/oklog/ulid) = %{version}

%description
ulid implements Universally Unique Lexicographically Sortable
Identifiers. cmd/ulid needs unpackaged pborman/getopt.

%prep -a
# cmd/ulid is a CLI that needs unpackaged github.com/pborman/getopt/v2.
rm -rf cmd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
