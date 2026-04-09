# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golog
%define go_import_path  github.com/kataras/golog

Name:           go-github-kataras-golog
Version:        0.1.15
Release:        %autorelease
Summary:        A high-performant Logging Foundation for Go Applications. X3 faster than the rest leveled loggers.
License:        BSD-3-Clause
URL:            https://github.com/kataras/golog
#!RemoteAsset
Source0:        https://github.com/kataras/golog/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kataras/golog) = %{version}

%description
golog is a zero-dependency simple, fast and easy-to-use level-based
logger written in Go Programming Language (https://go.dev).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
