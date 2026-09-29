# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assertions
%define go_import_path  github.com/smartystreets/assertions

Name:           go-github-smartystreets-assertions
Version:        1.2.0
Release:        %autorelease
Summary:        Assertions for Go tests
License:        MIT AND Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/smartystreets/assertions
#!RemoteAsset:  sha256:b1b6becbca1d6375d426461d95c7daf5532770e4747b4ee600627d97aae10f87
Source0:        https://github.com/smartystreets/assertions/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Legacy test code fails current go vet checks.
BuildOption(check):  -vet=off

# The mixed-type map rendering expectation depends on runtime type-pointer order.
BuildOption(check):  -skip '^TestMapSortRendering$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata

Provides:       go(github.com/smartystreets/assertions) = %{version}

%description
Assertions for Go tests.

%prep -a
# Keep bundled license texts under distinct names.
mkdir licenses
cp internal/go-render/LICENSE licenses/go-render-LICENSE
cp internal/oglematchers/LICENSE licenses/oglematchers-LICENSE
cp internal/go-diff/LICENSE licenses/go-diff-LICENSE
cp internal/go-diff/APACHE-LICENSE-2.0 licenses/go-diff-APACHE-LICENSE-2.0

%files
%doc README.md
%license LICENSE.md
%license licenses
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
