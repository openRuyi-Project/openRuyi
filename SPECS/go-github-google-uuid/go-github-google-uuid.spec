# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           uuid
%define go_import_path  github.com/google/uuid

Name:           go-github-google-uuid
Version:        1.6.0
Release:        %autorelease
Summary:        Go package for UUIDs based on RFC 4122 and DCE 1.1: Authentication and Security Services.
License:        BSD-3-Clause
URL:            https://github.com/google/uuid
#!RemoteAsset
Source0:        https://github.com/google/uuid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/uuid) = %{version}

%description
The uuid package generates and inspects UUIDs based on RFC 9562
(https://datatracker.ietf.org/doc/html/rfc9562) and DCE 1.1:
Authentication and Security Services.

This package is based on the github.com/pborman/uuid package (previously
named code.google.com/p/go-uuid).  It differs from these earlier
packages
in that a UUID is a 16 byte array rather than a byte slice.  One loss
due to this change is the ability to represent an invalid UUID (vs a NIL
UUID).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
