# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           smithy-go
%define go_import_path  github.com/aws/smithy-go
%define package_version 2025-12-01
# TODO: Test need too much dependencies, add it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-aws-smithy-go
Version:        2025.12.01
Release:        %autorelease
Summary:        Smithy code generators for Go (in development)
License:        Apache-2.0
URL:            https://github.com/aws/smithy-go
#!RemoteAsset
Source0:        https://github.com/aws/smithy-go/archive/refs/tags/release-%{package_version}.tar.gz#/%{_name}-%{package_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/aws/smithy-go) = %{version}

%description
Smithy code generators for Go and the accompanying smithy-go runtime.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
