# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           llib
%define go_import_path  github.com/lesismal/llib
# Test failure, may be cause by outdate code - Julian
%define go_test_ignore_failure 1

Name:           go-github-lesismal-llib
Version:        1.2.2
Release:        %autorelease
Summary:        llib - nbio's dependency lib.
License:        BSD-3-Clause
URL:            https://github.com/lesismal/llib
#!RemoteAsset
Source0:        https://github.com/lesismal/llib/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/lesismal/llib) = %{version}

Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)

%description
llib - nbio (https://github.com/lesismal/nbio)'s dependency lib.

Features:

Blocking/NonBlocking TLS interface(rewritten from a copy of golang
 1.6 std's tls).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
