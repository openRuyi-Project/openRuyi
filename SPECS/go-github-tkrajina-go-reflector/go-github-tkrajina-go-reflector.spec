# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-reflector
%define go_import_path  github.com/tkrajina/go-reflector

Name:           go-github-tkrajina-go-reflector
Version:        0.5.5
Release:        %autorelease
Summary:        Convenience helpers around Go reflection
License:        Apache-2.0
URL:            https://github.com/tkrajina/go-reflector
#!RemoteAsset:  sha256:fa4e04b3db3335447fc1e8da9fc4ea7843ab780ee9bd82a0176bc9c908905eee
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch2000:      2000-call-the-renamed-Subtract-method-in-tests.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides convenience helpers for inspecting Go values with the
standard reflection API.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
