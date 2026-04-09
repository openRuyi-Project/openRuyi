# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsondiff
%define go_import_path  github.com/nsf/jsondiff
%define commit_id 8e8d90c4c0ac88dc08c7336bc394e4a37f7ababd

Name:           go-github-nsf-jsondiff
Version:        0+git20260207.8e8d90c
Release:        %autorelease
Summary:        JsonDiff library
License:        MIT
URL:            https://github.com/nsf/jsondiff
#!RemoteAsset
Source0:        https://github.com/nsf/jsondiff/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/nsf/jsondiff) = %{version}

%description
The main purpose of the library is integration into tests which use json
and providing human-readable output of test results.

The lib can compare two json items and return a detailed report of the
comparison.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
