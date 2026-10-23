# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gofumpt
%define go_import_path  mvdan.cc/gofumpt

Name:           go-mvdan-gofumpt
Version:        0.12.0
Release:        %autorelease
Summary:        Stricter Go source formatter
License:        BSD-3-Clause
URL:            https://github.com/mvdan/gofumpt
#!RemoteAsset:  sha256:b6d5d14692cad23996da4329bf24d30324af30125dd5261e6d9b0c5bc8b20b28
Source0:        https://github.com/mvdan/gofumpt/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# OBS Go test binaries report no module metadata for this package.
Patch2000:      2000-adjust-diagnose-golden-for-buildinfo.patch

BuildOption(prep):  -n gofumpt-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-quicktest/qt)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(mvdan.cc/gofumpt) = %{version}
Provides:       go(mvdan.cc/gofumpt/format) = %{version}
Provides:       go(mvdan.cc/gofumpt/internal/govendor/diff) = %{version}
Provides:       go(mvdan.cc/gofumpt/internal/govendor/go/doc/comment) = %{version}
Provides:       go(mvdan.cc/gofumpt/internal/govendor/go/format) = %{version}
Provides:       go(mvdan.cc/gofumpt/internal/govendor/go/printer) = %{version}
Provides:       go(mvdan.cc/gofumpt/internal/version) = %{version}

Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/tools)

%description
Stricter Go source formatter.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE LICENSE.google
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
