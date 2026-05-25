# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pretty
%define go_import_path  github.com/tidwall/pretty

Name:           go-github-tidwall-pretty
Version:        1.2.1
Release:        %autorelease
Summary:        JSON pretty printer for Go
License:        MIT
URL:            https://github.com/tidwall/pretty
#!RemoteAsset:  sha256:1104d56f12b522b041abe7b9201e4cd46a63dad7c017db9dad87fed50bcc716b
Source0:        https://github.com/tidwall/pretty/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/tidwall/pretty) = %{version}

%description
This package provides JSON pretty printer for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
