# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           generic-list-go
%define go_import_path  github.com/bahlo/generic-list-go

Name:           go-github-bahlo-generic-list-go
Version:        0.2.0
Release:        %autorelease
Summary:        Go container/list but with generics.
License:        BSD-3-Clause
URL:            https://github.com/bahlo/generic-list-go
#!RemoteAsset
Source0:        https://github.com/bahlo/generic-list-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/bahlo/generic-list-go) = %{version}

%description
Go container/list but with generics.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
