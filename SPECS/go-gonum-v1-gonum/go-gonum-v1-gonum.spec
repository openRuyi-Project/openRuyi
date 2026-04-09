# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gonum
%define go_import_path  gonum.org/v1/gonum
# TODO: these two failed on riscv64 and I have no idea why - 251
%define go_test_exclude_glob %{shrink:
    gonum.org/v1/gonum/graph/layout*
    gonum.org/v1/gonum/mathext/internal/amos*
}

Name:           go-gonum-v1-gonum
Version:        0.16.0
Release:        %autorelease
Summary:        Gonum is a set of numeric libraries for the Go programming language.
License:        BSD-3-Clause
URL:            https://github.com/gonum/gonum
#!RemoteAsset
Source0:        https://github.com/gonum/gonum/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off -short -timeout 150m

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gonum.org/v1/plot)

Provides:       go(gonum.org/v1/gonum) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(golang.org/x/tools)
Requires:       go(gonum.org/v1/plot)

%description
Gonum is a set of packages designed to make writing numerical and
scientific algorithms productive, performant, and scalable.

Gonum contains libraries for matrices and linear algebra; statistics,
probability distributions, and sampling; tools for function
differentiation, integration, and optimization; network creation and
analysis; and more.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
