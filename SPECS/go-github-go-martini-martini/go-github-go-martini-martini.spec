# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           martini
%define go_import_path  github.com/go-martini/martini

Name:           go-github-go-martini-martini
Version:        1.0
Release:        %autorelease
Summary:        Classy web framework for Go
License:        MIT
URL:            https://github.com/go-martini/martini
#!RemoteAsset
Source0:        https://github.com/go-martini/martini/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/codegangsta/inject)

Provides:       go(github.com/go-martini/martini) = %{version}

%description
**NOTE:** The martini framework is no longer maintained.

Martini is a powerful package for quickly writing modular web
applications/services in Golang.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
