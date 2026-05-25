# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bom
%define go_import_path  github.com/spkg/bom

Name:           go-github-spkg-bom
Version:        1.0.1
Release:        %autorelease
Summary:        Strip UTF-8 byte order marks
License:        MIT
URL:            https://github.com/spkg/bom
#!RemoteAsset:  sha256:9f59082fd159055e766d8354c07cc86826af8e97d4591c5692e4b6205033aac0
Source0:        https://github.com/spkg/bom/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/spkg/bom) = %{version}

%description
This package strips UTF-8 byte order marks from byte streams.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
