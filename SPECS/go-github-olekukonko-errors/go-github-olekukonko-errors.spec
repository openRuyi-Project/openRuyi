# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           errors
%define go_import_path  github.com/olekukonko/errors

Name:           go-github-olekukonko-errors
Version:        1.1.0
Release:        %autorelease
Summary:        A production-grade error handling library for Go
License:        MIT
URL:            https://github.com/olekukonko/errors
#!RemoteAsset
Source0:        https://github.com/olekukonko/errors/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/olekukonko/errors) = %{version}

%description
A production-grade error handling library for Go, offering zero-cost
abstractions, stack traces, multi-error support, retries, and advanced
monitoring through two complementary packages: errors (core) and errmgr
(management).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
