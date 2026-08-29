# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sjson
%define go_import_path  github.com/tidwall/sjson

Name:           go-github-tidwall-sjson
Version:        1.2.5
Release:        %autorelease
Summary:        JSON value setter for Go
License:        MIT
URL:            https://github.com/tidwall/sjson
#!RemoteAsset:  sha256:2aaf9ad86db939cf8ab573aea61fd35cb4e4f89e819d9cefbfe45c2a29282859
Source0:        https://github.com/tidwall/sjson/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/pretty)

Provides:       go(github.com/tidwall/sjson) = %{version}

Requires:       go(github.com/tidwall/gjson)
Requires:       go(github.com/tidwall/pretty)

%description
This package provides JSON value setter for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
