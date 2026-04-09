# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           inject
%define go_import_path  github.com/codegangsta/inject
%define package_version 1.0-rc1

Name:           go-github-codegangsta-inject
Version:        1.0~rc1
Release:        %autorelease
Summary:        Dependency injection for go
License:        MIT
URL:            https://github.com/codegangsta/inject
#!RemoteAsset
Source0:        https://github.com/codegangsta/inject/archive/refs/tags/v%{package_version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/codegangsta/inject) = %{version}

%description
Package inject provides utilities for mapping and injecting dependencies
in various ways.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
