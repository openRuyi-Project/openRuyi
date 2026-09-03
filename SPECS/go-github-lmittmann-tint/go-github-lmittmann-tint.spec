# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tint
%define go_import_path  github.com/lmittmann/tint

Name:           go-github-lmittmann-tint
Version:        1.2.0
Release:        %autorelease
Summary:        Colorized slog handler for Go
License:        MIT
URL:            https://github.com/lmittmann/tint
#!RemoteAsset:  sha256:26282e6a46c1b3d0c34d86da92b4544c4ce59b8c0280bcdb4629e2de5eeba2d4
Source0:        https://github.com/lmittmann/tint/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Tint provides a zero-dependency slog handler that writes human-readable,
colorized structured logs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
