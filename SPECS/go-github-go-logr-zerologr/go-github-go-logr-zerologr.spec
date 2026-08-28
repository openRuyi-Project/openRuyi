# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zerologr
%define go_import_path  github.com/go-logr/zerologr

Name:           go-github-go-logr-zerologr
Version:        1.2.3
Release:        %autorelease
Summary:        Zerolog backend for the logr interface
License:        Apache-2.0
URL:            https://github.com/go-logr/zerologr
#!RemoteAsset:  sha256:cbddc2b7ee386c14b5f9e3289065b4e35f33c0b3563d4b1dbfe88c783d52a625
Source0:        https://github.com/go-logr/zerologr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/rs/zerolog)

%description
Zerologr adapts Zerolog loggers to the structured logging interfaces defined
by github.com/go-logr/logr.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
