# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pdf
%define go_import_path  rsc.io/pdf
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id c47d69cf462f804ff58ca63c61a8fb2aed76587e

Name:           go-rsc-pdf
Version:        0.1.0+git20260106.c47d69c
Release:        %autorelease
Summary:        Golang library that provides a reader for the PDF format
License:        BSD-3-Clause
URL:            https://github.com/rsc/pdf
#!RemoteAsset
Source0:        https://github.com/rsc/pdf/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(rsc.io/pdf) = %{version}

%description
This package exposes the simple structure along with some wrappers to
extract basic information. If more complex information is needed, it
is possible to extract that information by interpreting the structure
exposed by this package.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
