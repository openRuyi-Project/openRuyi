# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           modver
%define go_import_path  github.com/tenntenn/modver

Name:           go-github-tenntenn-modver
Version:        1.0.1
Release:        %autorelease
Summary:        Query and filter Go module versions
License:        MIT
URL:            https://github.com/tenntenn/modver
#!RemoteAsset:  sha256:fcae89fadc81b6c61439d24810394b6f2830d9038b37c5e629db781e7ef10051
Source0:        https://github.com/tenntenn/modver/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.15
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/hashicorp/go-version)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/hashicorp/go-version)

%description
Query available Go module versions and filter them by version constraints
or minor releases. This package contains the complete upstream repository
sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
