# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mxj
%define go_import_path  github.com/clbanning/mxj
# The examples directory contains multiple standalone main packages.
%define go_test_exclude %{go_import_path}/examples

Name:           go-github-clbanning-mxj
Version:        1.8.4
Release:        %autorelease
Summary:        XML and JSON map utilities for Go
License:        (BSD-3-Clause OR MIT)
URL:            https://github.com/clbanning/mxj
#!RemoteAsset:  sha256:335fa9d17855c8540eca83fd8ecacc5979570fe15be04f7c1154f0b71f2c39c7
Source0:        https://github.com/clbanning/mxj/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects legacy example names, while the tests themselves remain
# valid and are still executed.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/x2j-wrapper) = %{version}

%description
mxj encodes and decodes XML and JSON values as Go maps and supports querying
and modifying values by key path.

%files
%doc readme.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
