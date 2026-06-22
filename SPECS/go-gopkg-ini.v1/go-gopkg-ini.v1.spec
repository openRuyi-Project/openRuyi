# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ini
%define go_import_path  gopkg.in/ini.v1

Name:           go-gopkg-ini.v1
Version:        1.67.3
Release:        %autorelease
Summary:        Package ini provides INI file read and write functionality in Go
License:        Apache-2.0
URL:            https://github.com/go-ini/ini
#!RemoteAsset:  sha256:20564d725575a12e174a17f8d1d42a0a03503448fab8f3703dc64599d79ad79a
Source0:        https://github.com/go-ini/ini/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(gopkg.in/ini.v1) = %{version}

%description
Package ini provides INI file parsing and writing functionality for Go,
including section, key, comment, and type-conversion helpers.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
