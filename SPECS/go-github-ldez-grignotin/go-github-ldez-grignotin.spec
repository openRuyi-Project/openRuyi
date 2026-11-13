# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           grignotin
%define go_import_path  github.com/ldez/grignotin

Name:           go-github-ldez-grignotin
Version:        0.10.1
Release:        %autorelease
Summary:        A collection of small helpers around Go proxy, Go meta information, etc
License:        Apache-2.0
URL:            https://github.com/ldez/grignotin
#!RemoteAsset:  sha256:8cf14e21d8cf87c003f0eb86942afb80ac13a74f2c0c0c91f4f88ca53e01ede9
Source0:        https://github.com/ldez/grignotin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/ldez/grignotin/commit/c39f1e5d0ab40177e83d1223186796fb1583691f
Patch1000:      1000-tests-fix.patch
# Keep module queries and HTTP tests deterministic in offline GOPATH builds.
Patch2000:      2000-offline-module-and-http-tests.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/ldez/grignotin) = %{version}
Provides:       go(github.com/ldez/grignotin/goenv) = %{version}
Provides:       go(github.com/ldez/grignotin/gomod) = %{version}
Provides:       go(github.com/ldez/grignotin/goproxy) = %{version}
Provides:       go(github.com/ldez/grignotin/metago) = %{version}
Provides:       go(github.com/ldez/grignotin/version) = %{version}

Requires:       go(golang.org/x/mod)

%description
A collection of small helpers around Go proxy, Go meta information, etc.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n grignotin-%{version}

%check -p
# GOPATH builds default to legacy mux semantics; the test servers use Go 1.22
# method-aware patterns and need the current ServeMux implementation.
export GODEBUG="${GODEBUG:+$GODEBUG,}httpmuxgo121=0"

%files
%doc readme.md
%license LICENSE
%{go_sys_gopath}/github.com/ldez/grignotin

%changelog
%autochangelog
