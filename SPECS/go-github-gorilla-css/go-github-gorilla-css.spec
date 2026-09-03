# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           css
%define go_import_path  github.com/gorilla/css

Name:           go-github-gorilla-css
Version:        1.0.1
Release:        %autorelease
Summary:        CSS3 tokenizer for Go
License:        BSD-3-Clause
URL:            https://github.com/gorilla/css
#!RemoteAsset:  sha256:c56d3dd69a9922440c3a79246ff3b3fe8114128eac94605e3efcd9c465c57e4a
Source0:        https://github.com/gorilla/css/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gorilla/css) = %{version}

%description
gorilla/css provides a standards-oriented CSS3 tokenizer implemented in Go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
