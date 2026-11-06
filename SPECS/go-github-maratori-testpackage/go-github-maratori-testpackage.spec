# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testpackage
%define go_import_path  github.com/maratori/testpackage

Name:           go-github-maratori-testpackage
Version:        1.1.2
Release:        %autorelease
Summary:        Testpackage is golang linter that makes you use a separate _test package
License:        MIT
URL:            https://github.com/maratori/testpackage
#!RemoteAsset:  sha256:77f17c32f4a60f0551986a4b8c396bc951e34f892d6e55222152ce4e07126b4a
Source0:        https://github.com/maratori/testpackage/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/maratori/testpackage) = %{version}
Provides:       go(github.com/maratori/testpackage/pkg/testpackage) = %{version}

Requires:       go(golang.org/x/tools)

%description
Testpackage is golang linter that makes you use a separate _test package.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n testpackage-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/maratori/testpackage

%changelog
%autochangelog
