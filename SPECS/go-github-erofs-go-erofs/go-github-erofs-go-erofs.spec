# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-erofs
%define go_import_path  github.com/erofs/go-erofs

Name:           go-github-erofs-go-erofs
Version:        0.3.1
Release:        %autorelease
Summary:        Go implementation of the EROFS filesystem
License:        Apache-2.0
URL:            https://github.com/erofs/go-erofs
#!RemoteAsset:  sha256:dff791c2e56b04b3c8b371c83df9af580be04983c4d6523f0dffb200726e5d49
Source0:        https://github.com/erofs/go-erofs/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/erofs/go-erofs) = %{version}

%description
go-erofs provides a pure Go implementation of the EROFS filesystem format.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
