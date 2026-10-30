# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testableexamples
%define go_import_path  github.com/maratori/testableexamples

Name:           go-github-maratori-testableexamples
Version:        1.0.1
Release:        %autorelease
Summary:        Linter checks if examples are testable (have an expected output)
License:        MIT
URL:            https://github.com/maratori/testableexamples
#!RemoteAsset:  sha256:d8473bbd41df14c9d452ebb771b459b7c5ae458a9f50d133588fa477d9ee08c3
Source0:        https://github.com/maratori/testableexamples/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/maratori/testableexamples) = %{version}
Provides:       go(github.com/maratori/testableexamples/pkg/testableexamples) = %{version}
Provides:       go(github.com/maratori/testableexamples/pkg/testableexamples/testfiles) = %{version}

Requires:       go(golang.org/x/tools)

%description
Linter checks if examples are testable (have an expected output).
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n testableexamples-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/maratori/testableexamples

%changelog
%autochangelog
