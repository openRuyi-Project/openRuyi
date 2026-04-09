# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fastuuid
%define go_import_path  github.com/rogpeppe/fastuuid

Name:           go-github-rogpeppe-fastuuid
Version:        1.2.0
Release:        %autorelease
Summary:        Fast generation of 192-bit UUIDs
License:        BSD-3-Clause
URL:            https://github.com/rogpeppe/fastuuid
#!RemoteAsset
Source0:        https://github.com/rogpeppe/fastuuid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/rogpeppe/fastuuid) = %{version}

%description
Package fastuuid provides fast UUID generation of 192 bit universally
unique identifiers.

It also provides simple support for 128-bit RFC-4122 V4 UUID strings.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
