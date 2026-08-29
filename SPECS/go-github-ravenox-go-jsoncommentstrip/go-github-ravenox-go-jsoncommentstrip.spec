# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-jsoncommentstrip
%define go_import_path  github.com/RaveNoX/go-jsoncommentstrip

Name:           go-github-ravenox-go-jsoncommentstrip
Version:        1.0.0
Release:        %autorelease
Summary:        Library for strip JSON comments
License:        MIT
URL:            https://github.com/RaveNoX/go-jsoncommentstrip
#!RemoteAsset:  sha256:d5f19ef91ff78f41f2c70c68051f1aa63d56344908a8334ce040d40157567d02
Source0:        https://github.com/RaveNoX/go-jsoncommentstrip/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

# github.com/apapsch/go-jsonmerge/v2 imports the defunct apapsch fork path,
# but the only available upstream source is RaveNoX/go-jsoncommentstrip.
# - HNO3Miracle
Provides:       go(github.com/apapsch/go-jsoncommentstrip) = %{version}
Provides:       go(github.com/RaveNoX/go-jsoncommentstrip) = %{version}

%description
Go library for stripping comments from JSON input.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
