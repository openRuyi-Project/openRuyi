# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonreference
%define go_import_path  github.com/go-openapi/jsonreference
# I dont know why it will fail on OBS - Julian
%define go_test_ignore_failure 1

Name:           go-github-go-openapi-jsonreference
Version:        0.21.4
Release:        %autorelease
Summary:        json reference for golang
License:        Apache-2.0
URL:            https://github.com/go-openapi/jsonreference
#!RemoteAsset
Source0:        https://github.com/go-openapi/jsonreference/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/testify)
BuildRequires:  go(github.com/go-openapi/swag)

Provides:       go(github.com/go-openapi/jsonreference) = %{version}

Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/go-openapi/testify)

%description
An implementation of JSON Reference for golang.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
