# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           semver
%define go_import_path  github.com/Masterminds/semver/v3

Name:           go-github-masterminds-semver-v3
Version:        3.5.0
Release:        %autorelease
Summary:        Semantic versioning library for Go
License:        MIT
URL:            https://github.com/Masterminds/semver
#!RemoteAsset:  sha256:5c3d1316e90ffec6ac0b56601147136e767daf4efbd94d669b747e1c3cb54714
Source0:        https://github.com/Masterminds/semver/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/Masterminds/semver/v3) = %{version}

%description
This package provides Semantic versioning library for Go.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
