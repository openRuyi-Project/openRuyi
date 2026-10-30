# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           subcommands
%define go_import_path  github.com/google/subcommands

Name:           go-github-google-subcommands
Version:        1.2.0
Release:        %autorelease
Summary:        Subcommand dispatch and flag handling for Go programs
License:        Apache-2.0
URL:            https://github.com/google/subcommands
#!RemoteAsset:  sha256:99602409506274003f52f6eb901f3a4d6aa2fc041971939dfa753ffcf0549bae
Source0:        https://github.com/google/subcommands/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Subcommands provides command registration, dispatch, help output, and flag
handling for Go programs that expose multiple subcommands.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
