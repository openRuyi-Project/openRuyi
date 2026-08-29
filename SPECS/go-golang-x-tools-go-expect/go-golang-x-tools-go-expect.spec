# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           expect
%define go_import_path  golang.org/x/tools/go/expect

Name:           go-golang-x-tools-go-expect
Version:        0.30.0
Release:        %autorelease
Summary:        Go expect marker parser from golang.org/x/tools
License:        BSD-3-Clause
URL:            https://github.com/golang/tools
#!RemoteAsset:  sha256:c1e93ac3be804264bbe3779418caa6728944472cf5bc9368365657e31c1b4a2e
Source0:        https://github.com/golang/tools/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go-rpm-macros

Provides:       go(golang.org/x/tools/go/expect) = %{version}

Requires:       go(golang.org/x/mod)

%description
This package provides the removed golang.org/x/tools/go/expect package needed
by packages that still depend on older x/tools APIs.

%prep -a
%autosetup -n tools-%{version}
# This compatibility package intentionally ships only go/expect from x/tools
# 0.30.0. Newer x/tools no longer contains this package, while some consumers
# still import it.
mkdir -p %{_builddir}/go/src/%{go_import_path}
cp -a LICENSE go/expect/. %{_builddir}/go/src/%{go_import_path}/
cd %{_builddir}
rm -rf %{name}-%{version}
cp -a %{_builddir}/go/src/%{go_import_path} %{name}-%{version}
cd %{_builddir}/go/src/%{go_import_path}

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
