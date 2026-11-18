# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gocognit
%define go_import_path  github.com/uudashr/gocognit

Name:           go-github-uudashr-gocognit
Version:        1.3.0
Release:        %autorelease
Summary:        Go analyzer for cognitive complexity
License:        MIT
URL:            https://github.com/uudashr/gocognit
#!RemoteAsset:  sha256:75dcae900e7d3f09fb6989bb771b8a3a155a2850d011fa4e54c6004d45fd3405
Source0:        https://github.com/uudashr/gocognit/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/uudashr/gocognit) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for cognitive complexity.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n gocognit-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/uudashr/gocognit

%changelog
%autochangelog
