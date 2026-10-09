# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-assert
%define go_import_path  github.com/huandu/go-assert

Name:           go-github-huandu-go-assert
Version:        1.1.6
Release:        %autorelease
Summary:        Assertions with source context for Go tests
License:        MIT
URL:            https://github.com/huandu/go-assert
VCS:            git:https://github.com/huandu/go-assert.git
#!RemoteAsset:  sha256:32677b94294e794cf9ef63e247a96602cbdbc8a443f7591179df88216c28ef03
Source0:        https://github.com/huandu/go-assert/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/davecgh/go-spew)

%description
This library provides assertions for Go tests and includes the source
expression and formatted values in assertion failure messages.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
