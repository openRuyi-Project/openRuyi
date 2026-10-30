# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           funlen
%define go_import_path  github.com/ultraware/funlen

Name:           go-github-ultraware-funlen
Version:        0.2.0
Release:        %autorelease
Summary:        Funlen is a linter that checks for long functions
License:        MIT
URL:            https://github.com/ultraware/funlen
#!RemoteAsset:  sha256:5dd7a1d3e73702edcceee4ecff15fc1e9ee48a99c686035ff91632b3877c0cc5
Source0:        https://github.com/ultraware/funlen/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/ultraware/funlen) = %{version}

Requires:       go(golang.org/x/tools)

%description
Funlen is a linter that checks for long functions.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n funlen-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/ultraware/funlen

%changelog
%autochangelog
