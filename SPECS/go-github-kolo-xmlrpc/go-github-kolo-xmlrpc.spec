# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xmlrpc
%define go_import_path  github.com/kolo/xmlrpc
%define commit_id a4b6fa1dd06bbefa509944742c219846044ed934

Name:           go-github-kolo-xmlrpc
Version:        0+git20220921.a4b6fa1
Release:        %autorelease
Summary:        Implementation of XMLRPC protocol in Go language.
License:        MIT
URL:            https://github.com/kolo/xmlrpc
#!RemoteAsset:  sha256:0458acac47655e593b31f87f529a670050b96c2e23d8a83484496e58b307672c
Source0:        https://github.com/kolo/xmlrpc/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n xmlrpc-a4b6fa1dd06bbefa509944742c219846044ed934

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/text/encoding/charmap)
BuildRequires:  go(golang.org/x/text/transform)

Provides:       go(github.com/kolo/xmlrpc) = %{version}


%description
[Image: GoDoc] (https://godoc.org/github.com/kolo/xmlrpc?status.svg)
(https://godoc.org/github.com/kolo/xmlrpc)

Overview

xmlrpc is an implementation of client side part of XMLRPC protocol in Go
language.

Status

This project is in minimal maintenance mode with no further development.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
