# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           diff
%define go_import_path  github.com/andreyvit/diff
%define commit_id       c7f18ee00883bfd3b00e0a2bf7607827e0148ad4

Name:           go-github-andreyvit-diff
Version:        0+git20260823.c7f18ee
Release:        %autorelease
Summary:        Quick and easy string diffing functions for Go
License:        MIT
URL:            https://github.com/andreyvit/diff
#!RemoteAsset:  sha256:9128e34ca1a5446d76ecc6aa409a7b4d47f21e9ddf544810921687db143b78ad
Source0:        https://github.com/andreyvit/diff/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/sergi/go-diff)

Provides:       go(github.com/andreyvit/diff) = %{version}

Requires:       go(github.com/sergi/go-diff)

%description
diff provides quick and easy string diffing functions
for Go based on github.com/sergi/go-diff.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
