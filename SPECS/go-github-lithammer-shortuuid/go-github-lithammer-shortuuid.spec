# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           shortuuid
%define go_import_path  github.com/lithammer/shortuuid

Name:           go-github-lithammer-shortuuid
Version:        4.2.0
Release:        %autorelease
Summary:        A generator library for concise, unambiguous and URL-safe UUIDs
License:        MIT
URL:            https://github.com/lithammer/shortuuid
#!RemoteAsset
Source0:        https://github.com/lithammer/shortuuid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/uuid)

Provides:       go(github.com/lithammer/shortuuid)
Requires:       go(github.com/google/uuid)

%description
A Go library that generates concise, unambiguous, URL-safe UUIDs. Based on and compatible with the Python library shortuuid.

Often, one needs to use non-sequential IDs in places where users will see them, but the IDs must be as concise and easy to use as possible. shortuuid solves this problem by generating UUIDs using google/uuid and then translating them to base57 using lowercase and uppercase letters and digits, and removing similar-looking characters such as l, 1, I, O and 0.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
