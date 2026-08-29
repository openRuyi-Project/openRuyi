# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gjson
%define go_import_path  github.com/tidwall/gjson

Name:           go-github-tidwall-gjson
Version:        1.19.0
Release:        %autorelease
Summary:        JSON value getter for Go
License:        MIT
URL:            https://github.com/tidwall/gjson
#!RemoteAsset:  sha256:2470bedce4658fe5161d3651cf2ccc799b58c64630fddde8c5414aee0b5a4f6b
Source0:        https://github.com/tidwall/gjson/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/tidwall/match)
BuildRequires:  go(github.com/tidwall/pretty)

Provides:       go(github.com/tidwall/gjson) = %{version}

Requires:       go(github.com/tidwall/match)
Requires:       go(github.com/tidwall/pretty)

%description
This package provides JSON value getter for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
