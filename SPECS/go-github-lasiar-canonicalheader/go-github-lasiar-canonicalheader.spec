# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           canonicalheader
%define go_import_path  github.com/lasiar/canonicalheader

Name:           go-github-lasiar-canonicalheader
Version:        1.1.3
Release:        %autorelease
Summary:        Go analyzer for canonical HTTP header names
License:        MIT
URL:            https://github.com/lasiar/canonicalheader
#!RemoteAsset:  sha256:1c750a8cc426ac2e31f3e4aa731d46c0507b329acfc0d51b67fdbb784239301d
Source0:        https://github.com/lasiar/canonicalheader/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-toolsmith/astcast)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/lasiar/canonicalheader) = %{version}

Requires:       go(github.com/go-toolsmith/astcast)
Requires:       go(golang.org/x/tools)

%description
Go analyzer for canonical HTTP header names.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n canonicalheader-%{version}

%files
%doc README.md
%license LICENCE
%{go_sys_gopath}/github.com/lasiar/canonicalheader

%changelog
%autochangelog
