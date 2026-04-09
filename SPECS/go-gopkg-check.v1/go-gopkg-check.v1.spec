# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           check.v1
%define go_import_path  gopkg.in/check.v1
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id 10cb98267c6cb43ea9cd6793f29ff4089c306974

Name:           go-gopkg-check.v1
Version:        0+git20260106.10cb982
Release:        %autorelease
Summary:        Rich testing for the Go language
License:        BSD-2-Clause
URL:            https://github.com/go-check/check
#!RemoteAsset
Source0:        https://github.com/go-check/check/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/kr/pretty)

Provides:       go(gopkg.in/check.v1) = %{version}

Requires:       go(github.com/kr/pretty)

%description
This Go language provides an internal testing library, named testing, which is
relatively slim due to the fact that the standard library correctness by
itself is verified using it. The check package, on the other hand, expects the
standard library from Go to be working correctly, and builds on it to offer a
richer testing framework for libraries and applications to use.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
