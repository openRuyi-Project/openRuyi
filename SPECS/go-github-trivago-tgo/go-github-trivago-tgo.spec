# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tgo
%define go_import_path  github.com/trivago/tgo

Name:           go-github-trivago-tgo
Version:        1.0.7
Release:        %autorelease
Summary:        Utility packages for Go applications
License:        Apache-2.0
URL:            https://github.com/trivago/tgo
#!RemoteAsset:  sha256:02d48e81089d0bd30d53be5c6acb0f97d7249e0e53bb79e2cf05d147c6dda020
Source0:        https://github.com/trivago/tgo/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Tgo provides reusable containers, formatting, logging, synchronization, and
testing helpers for Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
