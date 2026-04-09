# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           overflow
%define go_import_path  github.com/JohnCGriffin/overflow
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id 46fa312c352cdb9517817d04f2067d49f418e332

Name:           go-github-johncgriffin-overflow
Version:        0+git20260108.46fa312
Release:        %autorelease
Summary:        Check for int/int64/int32 arithmetic overflow in Golang
License:        MIT
URL:            https://github.com/JohnCGriffin/overflow
#!RemoteAsset
Source0:        https://github.com/JohnCGriffin/overflow/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/JohnCGriffin/overflow) = %{version}

%description
This package provides check for int/int8/int16/int64/int32 integer
overflow in Golang arithmetic.

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
