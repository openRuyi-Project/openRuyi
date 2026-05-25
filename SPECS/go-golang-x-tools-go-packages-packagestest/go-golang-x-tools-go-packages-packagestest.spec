# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tools
%define go_import_path  golang.org/x/tools
# Test only the compatibility package. The old x/tools tree contains many
# unrelated packages whose tests are not needed for this removed API shim. - HNO3Miracle
%define go_test_include %{go_import_path}/go/packages/packagestest

Name:           go-golang-x-tools-go-packages-packagestest
Version:        0.30.0
Release:        %autorelease
Summary:        Compatibility package for golang.org/x/tools/go/packages/packagestest
License:        BSD-3-Clause
URL:            https://github.com/golang/tools
#!RemoteAsset:  sha256:c1e93ac3be804264bbe3779418caa6728944472cf5bc9368365657e31c1b4a2e
Source0:        https://github.com/golang/tools/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/expect)
BuildRequires:  go-rpm-macros

Provides:       go(golang.org/x/tools/go/packages/packagestest) = %{version}

Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/tools/go/expect)

%description
This compatibility package provides the removed
golang.org/x/tools/go/packages/packagestest package for consumers that still
use older x/tools test APIs.

%install
# Build and test from the x/tools root so Go internal package visibility works,
# but install only the removed packagestest subtree to avoid conflicting with
# the main go-golang-x-tools package.
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}/go/packages
cp -a go/packages/packagestest %{buildroot}%{go_sys_gopath}/%{go_import_path}/go/packages/

%check
# The compatibility subtree imports golang.org/x/tools/internal packages. Put
# the full old x/tools source under one GOPATH root for %check, but keep the
# installed payload limited to go/packages/packagestest.
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
mkdir -p %{_builddir}/go/src/golang.org/x
rm -rf %{_builddir}/go/src/%{go_import_path}
cp -a . %{_builddir}/go/src/%{go_import_path}
cd %{_builddir}/go/src/%{go_import_path}
go test -v %{go_test_include}

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}/go/packages/packagestest

%changelog
%autochangelog
