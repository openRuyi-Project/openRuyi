# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           filepath
%define go_import_path  github.com/minio/filepath

Name:           go-github-minio-filepath
Version:        1.0.0
Release:        %autorelease
Summary:        Flat-key sorted filepath.Walk for Go
License:        BSD-3-Clause
URL:            https://github.com/minio/filepath
#!RemoteAsset:  sha256:aaf9252ffde11accab6dedabe7628dfa605df166e9839c11b9b05cb2740e6d7a
Source0:        https://github.com/minio/filepath/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/minio/filepath) = %{version}

%description
filepath reimplements Go's filepath.Walk with flat-key lexical
sorting. There is no LICENSE file; the Go files are BSD-3-Clause.

%files
%doc README.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
