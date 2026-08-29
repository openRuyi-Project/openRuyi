# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-archvariant
%define go_import_path  github.com/tonistiigi/go-archvariant

Name:           go-github-tonistiigi-go-archvariant
Version:        1.0.0
Release:        %autorelease
Summary:        Detect the supported amd64 microarchitecture variant
License:        MIT
URL:            https://github.com/tonistiigi/go-archvariant
#!RemoteAsset:  sha256:fb75a03315e6049b381437404597ee84987f7fe9fa1637878ce2af99cb888a66
Source0:        https://github.com/tonistiigi/go-archvariant/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/tonistiigi/go-archvariant) = %{version}

%description
go-archvariant detects the highest amd64 microarchitecture level (v1-v4) supported by the running CPU.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
