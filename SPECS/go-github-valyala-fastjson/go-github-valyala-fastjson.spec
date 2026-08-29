# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fastjson
%define go_import_path  github.com/valyala/fastjson

Name:           go-github-valyala-fastjson
Version:        1.6.10
Release:        %autorelease
Summary:        Fast JSON parser and validator for Go
License:        MIT
URL:            https://github.com/valyala/fastjson
#!RemoteAsset:  sha256:4e56f1d500e25bac7127c93bfbbf9deedfbec324c8b4b8e4c7a5e86091a05a95
Source0:        https://github.com/valyala/fastjson/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/valyala/fastjson) = %{version}

%description
fastjson is a fast JSON parser and validator for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
