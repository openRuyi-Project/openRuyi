# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ini
%define go_import_path  gopkg.in/ini.v1

Name:           go-gopkg-ini.v1
Version:        1.67.2
Release:        %autorelease
Summary:        Package ini provides INI file read and write functionality in Go
License:        Apache-2.0
URL:            https://github.com/go-ini/ini
#!RemoteAsset:  sha256:0cf3ebc458c4fe0bf495759c9e3aafe668d3b9febbd91db7d52c852ad4d3875e
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
