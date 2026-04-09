# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-internal
%define go_import_path  github.com/rogpeppe/go-internal

Name:           go-github-rogpeppe-go-internal
Version:        1.14.1
Release:        %autorelease
Summary:        Selected Go-internal packages factored out from the standard library
License:        BSD-3-Clause
URL:            https://github.com/rogpeppe/go-internal
#!RemoteAsset
Source0:        https://github.com/rogpeppe/go-internal/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# https://salsa.debian.org/go-team/packages/golang-github-rogpeppe-go-internal/-/blob/0f60076977a5f66c5f557820c009eb0b3d647b01/debian/0001-Allow-TestSimple-cover-to-PASS.patch
Source1:        2000-Allow-TestSimple-cover-to-PASS.patch
# Otherwise the TestScripts/env_var_with_go test will fail - 251
Source2:        2001-Allow-empty-default-GOPROXY.patch
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/rogpeppe/go-internal) = %{version}

Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/sys)

%description
This repository factors out an opinionated selection of internal
packages and functionality from the Go standard library. Currently this
consists mostly of packages and testing code from within the Go tool
implementation.

# We need to override the %check section to apply patches
%check
export GO111MODULE=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
%__mkdir -p %{_builddir}/go/src/%{go_import_path}
%__cp -a . %{_builddir}/go/src/%{go_import_path}
pushd %{_builddir}/go/src/%{go_import_path}
# Apply patch here
%__patch -N -p6 -i %{SOURCE1}
%__patch -N -p1 -i %{SOURCE2}
# Then test
go test -vet=off -v ./...
popd

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
