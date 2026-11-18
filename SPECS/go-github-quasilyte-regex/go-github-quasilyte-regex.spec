# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           regex
%define go_import_path  github.com/quasilyte/regex
%define commit_id       b3f0c404a7278362659382cf50fc41506bb4160c

Name:           go-github-quasilyte-regex
Version:        0+git20261022.b3f0c40
Release:        %autorelease
Summary:        Provides regular expressions parser as well as AST definitions
License:        MIT
URL:            https://github.com/quasilyte/regex
#!RemoteAsset:  sha256:a1c50ff63b0ec9b091727724a6029b19e60adf317d90581c3affe47e0450fe3c
Source0:        https://github.com/quasilyte/regex/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/quasilyte/regex/syntax) = %{version}

%description
Provides regular expressions parser as well as AST definitions.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n regex-%{commit_id}

%install -a
# Nested modules use their declared import paths; keep repository fixtures intact.
install -d %{buildroot}%{go_sys_gopath}/github.com/quasilyte/regex/syntax
cp -a syntax/. %{buildroot}%{go_sys_gopath}/github.com/quasilyte/regex/syntax/

%check
# Stage all modules at their declared paths before testing every package.
%{go_common}
mkdir -p %{_builddir}/go/src/github.com/quasilyte/regex/syntax
cp -a syntax/. %{_builddir}/go/src/github.com/quasilyte/regex/syntax/
# The package list omits modules that only declare tool dependencies.
(
    cd %{_builddir}/go/src/github.com/quasilyte/regex/syntax
    packages=$(go list -e -f '{{if or .GoFiles .CgoFiles .TestGoFiles .XTestGoFiles}}{{.ImportPath}}{{end}}' ./...)
    if [ -n "$packages" ]; then
        go test -v $packages
    fi
)

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/quasilyte/regex

%changelog
%autochangelog
