# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           match
%define go_import_path  github.com/tidwall/match

Name:           go-github-tidwall-match
Version:        1.2.0
Release:        %autorelease
Summary:        Pattern matching library for Go
License:        MIT
URL:            https://github.com/tidwall/match
#!RemoteAsset:  sha256:b12425c445e850d07c2bb8b3c4b343920494dfc78842cb1228da357c5b1c6563
Source0:        https://github.com/tidwall/match/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/tidwall/match) = %{version}

%description
This package provides Pattern matching library for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
