# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go
%define go_import_path  github.com/json-iterator/go
# So tired, can't stand more flaky tests - 251
%define go_test_exclude %{shrink:
    github.com/json-iterator/go/type_tests
    github.com/json-iterator/go/benchmarks
}

Name:           go-github-json-iterator-go
Version:        1.1.12
Release:        %autorelease
Summary:        A high-performance 100% compatible drop-in replacement of "encoding/json"
License:        MIT
URL:            https://github.com/json-iterator/go
#!RemoteAsset
Source0:        https://github.com/json-iterator/go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://sources.debian.org/src/golang-github-json-iterator-go/1.1.12-2/debian/patches/0001-Skip-test-for-encoding-b-and-f.patch
Patch0:         2000-Skip-test-for-encoding-b-and-f.patch

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/google/gofuzz)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/json-iterator/go) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/google/gofuzz)
Requires:       go(github.com/modern-go/concurrent)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(github.com/stretchr/testify)

%description
This package provides a high-performance 100% compatible drop-in
replacement of "encoding/json"

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
