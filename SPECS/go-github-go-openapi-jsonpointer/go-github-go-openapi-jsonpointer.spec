# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jsonpointer
%define go_import_path  github.com/go-openapi/jsonpointer

Name:           go-github-go-openapi-jsonpointer
Version:        0.23.1
Release:        %autorelease
Summary:        jsonpointer for golang with support for structs
License:        Apache-2.0
URL:            https://github.com/go-openapi/jsonpointer
#!RemoteAsset:  sha256:cb56ae17744d58d8e2b54c51c88f06e7689f87b4913881d580ef8a0e25ee2ea2
Source0:        https://github.com/go-openapi/jsonpointer/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/testify)

Provides:       go(github.com/go-openapi/jsonpointer) = %{version}

Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/go-openapi/testify)

%description
An implementation of JSON Pointer for golang, which supports go struct.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
