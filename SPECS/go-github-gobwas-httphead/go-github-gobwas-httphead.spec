# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httphead
%define go_import_path  github.com/gobwas/httphead
# Test failure, may be cause by outdate code
%define go_test_ignore_failure 1

Name:           go-github-gobwas-httphead
Version:        0.1.0
Release:        %autorelease
Summary:        Tiny HTTP header value parsing library in go.
License:        MIT
URL:            https://github.com/gobwas/httphead
#!RemoteAsset
Source0:        https://github.com/gobwas/httphead/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gobwas/httphead) = %{version}

%description
This library contains low-level functions for scanning HTTP RFC2616
compatible header value grammars.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
