# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ldap
%define go_import_path  github.com/go-ldap/ldap
# TODO: Test need too much dependencies, add it later - Julian
%define go_test_exclude_glob %{shrink:
    github.com/go-ldap/ldap/v3
    github.com/go-ldap/ldap/v3/gssapi
}

Name:           go-github-go-ldap-ldap
Version:        3.4.12
Release:        %autorelease
Summary:        Basic LDAP v3 functionality for the GO programming language.
License:        MIT
URL:            https://github.com/go-ldap/ldap
#!RemoteAsset
Source0:        https://github.com/go-ldap/ldap/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-ldap/ldap) = %{version}

%description
Basic LDAP v3 functionality for the GO programming language.

The library implements the following specifications:

 * (https://datatracker.ietf.org/doc/html/rfc4511) for basic operations
 * (https://datatracker.ietf.org/doc/html/rfc3062) for password modify
   operation
 * (https://datatracker.ietf.org/doc/html/rfc4514) for distinguished
   names parsing
 * (https://datatracker.ietf.org/doc/html/rfc4533) for Content
   Synchronization Operation
 * (https://datatracker.ietf.org/doc/html/draft-armijo-ldap-treedelete-
   02) for Tree Delete Control
 * (https://datatracker.ietf.org/doc/html/rfc2891) for Server Side
   Sorting of Search Results
 * (https://datatracker.ietf.org/doc/html/rfc4532) for WhoAmI requests

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
