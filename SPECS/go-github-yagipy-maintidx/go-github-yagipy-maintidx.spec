# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           maintidx
%define go_import_path  github.com/yagipy/maintidx

Name:           go-github-yagipy-maintidx
Version:        1.0.0
Release:        %autorelease
Summary:        Maintidx measures the maintainability index of each function
License:        MIT
URL:            https://github.com/yagipy/maintidx
#!RemoteAsset:  sha256:fa32cebe6eb5decb2162bfd8f9c2ebdccabb823154df263f7e0c6260ccffa989
Source0:        https://github.com/yagipy/maintidx/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/xerrors)

Provides:       go(github.com/yagipy/maintidx) = %{version}
Provides:       go(github.com/yagipy/maintidx/pkg/cyc) = %{version}
Provides:       go(github.com/yagipy/maintidx/pkg/halstvol) = %{version}

Requires:       go(golang.org/x/tools)

%description
Maintidx measures the maintainability index of each function.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n maintidx-%{version}

%check -p
# The analyzer fixture is a GOPATH tree; its marker would select module mode.
mv testdata/go.mod testdata/go.mod.fixture

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/yagipy/maintidx

%changelog
%autochangelog
