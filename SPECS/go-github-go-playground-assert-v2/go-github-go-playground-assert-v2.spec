# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assert
%define go_import_path  github.com/go-playground/assert/v2

Name:           go-github-go-playground-assert-v2
Version:        2.2.0
Release:        %autorelease
Summary:        Basic Assertion Library used along side native go testing, with building blocks for custom assertions
License:        MIT
URL:            https://github.com/go-playground/assert
#!RemoteAsset
Source0:        https://github.com/go-playground/assert/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-playground/assert/v2) = %{version}

%description
Package assert is a Basic Assertion library used along side native go
testing

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
