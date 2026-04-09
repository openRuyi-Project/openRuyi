# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tensor
%define go_import_path  github.com/pdevine/tensor
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id a7dc8b61c822528f973a5e4e7b272055c6fdb43e

%define _name           goautoneg
%define go_import_path  github.com/munnerz/goautoneg

Name:           go-github-munnerz-goautoneg
Version:        0+git20260108.a7dc8b6
Release:        %autorelease
Summary:        HTTP Content-Type Autonegotiation.
License:        BSD-3-Clause
URL:            https://github.com/munnerz/goautoneg
#!RemoteAsset
Source0:        https://github.com/munnerz/goautoneg/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/munnerz/goautoneg) = %{version}

%description
HTTP Content-Type Autonegotiation.

The functions in this package implement the behaviour specified in
http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
