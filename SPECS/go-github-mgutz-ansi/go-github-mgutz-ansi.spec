# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ansi
%define go_import_path  github.com/mgutz/ansi
%define commit_id       d51e80ef957dba7f19388ca64afefbd5a096af30

Name:           go-github-mgutz-ansi
Version:        0+git20260719.d51e80e
Release:        %autorelease
Summary:        Go library for creating ANSI colored strings and codes
License:        MIT
URL:            https://github.com/mgutz/ansi
#!RemoteAsset:  sha256:394eb0e1f63e4e8ee099e7cf843f6fd17ab93867b283e2385cb9613b435d57c7
Source0:        %{url}/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mattn/go-colorable)

Provides:       go(github.com/mgutz/ansi) = %{version}

Requires:       go(github.com/mattn/go-colorable)

%description
This Go library creates ANSI colored strings and escape codes.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
