# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           log
%define go_import_path  github.com/go-kit/log

Name:           go-github-go-kit-log
Version:        0.2.1
Release:        %autorelease
Summary:        Structured logging library for Go
License:        MIT
URL:            https://github.com/go-kit/log
#!RemoteAsset:  sha256:b37718967f9cbdb3eea4aa2fa9420b7d329b6bab7f9b85f970db197257226152
Source0:        https://github.com/go-kit/log/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-logfmt/logfmt)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/go-logfmt/logfmt)

%description
Package log provides structured logging interfaces and implementations for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
