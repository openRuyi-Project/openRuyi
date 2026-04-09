# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           filepathx
%define go_import_path  github.com/klauspost/filepathx
# Test example has not update yet after forked, ignore it
%define go_test_exclude_glob github.com/klauspost/filepathx/example/find

Name:           go-github-klauspost-filepathx
Version:        1.1.1
Release:        %autorelease
Summary:        Add double-star support to path/filepath
License:        MIT
URL:            https://github.com/klauspost/filepathx
#!RemoteAsset
Source0:        https://github.com/klauspost/filepathx/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/klauspost/filepathx) = %{version}

%description
A small filepath extension library that supports double star globbling.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
