# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gotest.tools
%define go_import_path  gotest.tools/v3
# gty-migrate-from-testify tests run "go mod tidy" and need module downloads;
# x/generics/property imports the non-v3 gotest.tools/x/generics/property path
# that is not provided by this v3 module in GOPATH-mode builds; poll connects
# to google.com:80, which is not reliable in the OBS build sandbox. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    gotest.tools/v3/assert/cmd/gty-migrate-from-testify
    gotest.tools/v3/poll
    gotest.tools/v3/x/generics/property
}

Name:           go-gotest-tools-v3
Version:        3.5.2
Release:        %autorelease
Summary:        Go packages for writing tests
License:        Apache-2.0
URL:            https://github.com/gotestyourself/gotest.tools
#!RemoteAsset:  sha256:9656a4df6d6e238c20c082fcad548ecf99e326a3005e52878635fe5ea56c7c81
Source0:        https://github.com/gotestyourself/gotest.tools/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(gotest.tools/v3) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(golang.org/x/tools)

%description
gotest.tools provides packages that help write Go tests.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
