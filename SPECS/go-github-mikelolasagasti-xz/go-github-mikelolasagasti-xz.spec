# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xz
%define go_import_path  github.com/mikelolasagasti/xz

Name:           go-github-mikelolasagasti-xz
Version:        1.0.1
Release:        %autorelease
Summary:        Implements XZ decompression natively in Go
License:        0BSD
URL:            https://github.com/mikelolasagasti/xz
#!RemoteAsset:  sha256:b38f06ee75f1dceac0af6a1e9fba81f8d66ed345996870964a8f5db8dae07d9b
Source0:        https://github.com/mikelolasagasti/xz/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mikelolasagasti/xz) = %{version}

%description
Package xz implements XZ decompression natively in Go.

Documentation at (https://pkg.go.dev/github.com/mikelolasagasti/xz).

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
