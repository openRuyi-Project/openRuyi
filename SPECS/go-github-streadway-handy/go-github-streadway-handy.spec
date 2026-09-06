# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           handy
%define go_import_path  github.com/streadway/handy
%define commit_id       0f66f006fb2ebde51f4ce769641df75d602989e7
# These historical tests depend on tight wall-clock timing and old retry
# semantics; keep the other package tests enabled. - HNO3Miracle
%define go_test_exclude %{go_import_path}/report %{go_import_path}/retry

Name:           go-github-streadway-handy
Version:        0+git20260818.0f66f00
Release:        %autorelease
Summary:        Reusable HTTP server handlers for Go
License:        BSD-2-Clause
URL:            https://github.com/streadway/handy
#!RemoteAsset:  sha256:979424115de9e3b70ee91fc3839f77bbe54699a9e32b98be6936eea7e80a213f
Source0:        https://github.com/streadway/handy/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Handy provides reusable HTTP server handlers and filters for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
