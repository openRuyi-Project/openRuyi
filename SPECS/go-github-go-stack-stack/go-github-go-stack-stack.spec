# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stack
%define go_import_path  github.com/go-stack/stack

Name:           go-github-go-stack-stack
Version:        1.8.0
Release:        %autorelease
Summary:        Call stack capture and formatting for Go
License:        MIT
URL:            https://github.com/go-stack/stack
#!RemoteAsset:  sha256:3b8987e137d76f4f35db1e8005ec7fb766b68eed8cac0ca0b795ac43cd72b319
Source0:        https://github.com/go-stack/stack/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-stack/stack) = %{version}

%description
Call stack capture and formatting for Go.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
