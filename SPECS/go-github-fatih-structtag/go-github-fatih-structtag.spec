# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           structtag
%define go_import_path  github.com/fatih/structtag

Name:           go-github-fatih-structtag
Version:        1.2.0
Release:        %autorelease
Summary:        Parse and modify Go struct tags
License:        BSD-3-Clause
URL:            https://github.com/fatih/structtag
#!RemoteAsset:  sha256:f39a7edcb38f70f8b12f8b4f18b386d508c6a5b7f6fbddcee52d299b795fdaab
Source0:        https://github.com/fatih/structtag/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/fatih/structtag) = %{version}

%description
Structtag parses, edits, and formats Go struct field tags.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
