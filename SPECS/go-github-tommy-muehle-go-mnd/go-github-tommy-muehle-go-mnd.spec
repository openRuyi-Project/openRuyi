# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-mnd
%define go_import_path  github.com/tommy-muehle/go-mnd/v2

Name:           go-github-tommy-muehle-go-mnd
Version:        2.5.1
Release:        %autorelease
Summary:        A vet analyzer to detect magic numbers
License:        MIT
URL:            https://github.com/tommy-muehle/go-mnd
#!RemoteAsset:  sha256:b13accde873df9719f2382e6f43534fecc8fada0e92677d2b6ab7707c8f96c26
Source0:        https://github.com/tommy-muehle/go-mnd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The upstream archive marks testdata as export-ignore; restore it so the
# complete analyzer test suite can run from the packaged source.
Patch2000:      2000-restore-testdata-excluded-from-release-archive.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/tommy-muehle/go-mnd/v2) = %{version}
Provides:       go(github.com/tommy-muehle/go-mnd/v2/checks) = %{version}
Provides:       go(github.com/tommy-muehle/go-mnd/v2/config) = %{version}

Requires:       go(golang.org/x/tools)

%description
A vet analyzer to detect magic numbers.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n go-mnd-%{version}
# Use packaged dependencies instead of the bundled snapshots.
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/tommy-muehle/go-mnd/v2

%changelog
%autochangelog
