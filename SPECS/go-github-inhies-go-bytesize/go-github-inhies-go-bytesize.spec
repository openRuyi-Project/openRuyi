# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-bytesize
%define go_import_path  github.com/inhies/go-bytesize
%define commit_id       4913239db9cf578e44f49d7b813734678ef94f51

Name:           go-github-inhies-go-bytesize
Version:        0+git20261019.4913239
Release:        %autorelease
Summary:        Parse and format byte sizes in Go
License:        BSD-3-Clause
URL:            https://github.com/inhies/go-bytesize
#!RemoteAsset:  sha256:7ef9789428346a76a6a312966dbdaac73d7babb2bba6d9c8db9f999babbb4982
Source0:        https://github.com/inhies/go-bytesize/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
ByteSize represents byte quantities and supports parsing, arithmetic, and
human-readable formatting with decimal and binary units.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
