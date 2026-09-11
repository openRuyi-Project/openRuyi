# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stripansi
%define go_import_path  github.com/acarl005/stripansi
%define commit_id       5a71ef0e047df0427e87a79f27009029921f1f9b

Name:           go-github-acarl005-stripansi
Version:        0+git20260907.5a71ef0
Release:        %autorelease
Summary:        Strip ANSI escape codes from strings
License:        MIT
URL:            https://github.com/acarl005/stripansi
#!RemoteAsset:  sha256:7a01171901e8c9d2ec423d45c08af32be0f47ba8dc61e5c22ff7b8b5c2f6eb08
Source0:        https://github.com/acarl005/stripansi/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/acarl005/stripansi) = %{version}

%description
stripansi removes ANSI escape codes from strings. It is used by the
mpb progress-bar library.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
