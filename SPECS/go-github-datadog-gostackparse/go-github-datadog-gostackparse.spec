# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gostackparse
%define go_import_path  github.com/DataDog/gostackparse

Name:           go-github-datadog-gostackparse
Version:        0.7.0
Release:        %autorelease
Summary:        Parse Go goroutine stack traces
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/DataDog/gostackparse
#!RemoteAsset:  sha256:24c35d411f473b9a4ad4889f3c3a13ae44285e039dd748216e20f32e9171eebc
Source0:        https://github.com/DataDog/gostackparse/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(%{go_import_path}) = %{version}

%description
Gostackparse efficiently parses textual goroutine stack traces emitted by
panic and runtime/debug.Stack into structured Go values.

%files
%doc README.md
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
