# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           schema
%define go_import_path  github.com/gorilla/schema

Name:           go-github-gorilla-schema
Version:        1.4.1
Release:        %autorelease
Summary:        Package gorilla/schema converts structs to and from form values
License:        BSD-3-Clause
URL:            https://github.com/gorilla/schema
#!RemoteAsset:  sha256:5ba1ae2586add03cbbe9ca0f4669c37fd257b196f6e3d2f41dc98cc99efb802b
Source0:        https://github.com/gorilla/schema/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gorilla/schema) = %{version}

%description
Package gorilla/schema converts structs to and from form values.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
