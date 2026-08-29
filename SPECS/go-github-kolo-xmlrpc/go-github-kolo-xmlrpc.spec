# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xmlrpc
%define go_import_path  github.com/kolo/xmlrpc
%define commit_id a4b6fa1dd06bbefa509944742c219846044ed934

Name:           go-github-kolo-xmlrpc
Version:        0+git20260607.a4b6fa1
Release:        %autorelease
Summary:        XML-RPC client implementation for Go
License:        MIT
URL:            https://github.com/kolo/xmlrpc
#!RemoteAsset:  sha256:0458acac47655e593b31f87f529a670050b96c2e23d8a83484496e58b307672c
Source0:        https://github.com/kolo/xmlrpc/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/kolo/xmlrpc) = %{version}

%description
This package provides an XML-RPC client implementation for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
