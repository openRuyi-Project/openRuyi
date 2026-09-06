# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-resiliency
%define go_import_path  github.com/eapache/go-resiliency

Name:           go-github-eapache-go-resiliency
Version:        1.7.0
Release:        %autorelease
Summary:        Resiliency patterns for Go
License:        MIT
URL:            https://github.com/eapache/go-resiliency
#!RemoteAsset:  sha256:9f84d71fae41cdcd2acedb9fe17ebe7659e1b2cf734be6b2d7135a0aab8f2649
Source0:        https://github.com/eapache/go-resiliency/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides retry, breaker, and timeout resiliency patterns for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
