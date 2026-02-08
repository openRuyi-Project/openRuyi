# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           repr
%define go_import_path  github.com/alecthomas/repr

Name:           go-github-alecthomas-repr
Version:        0.5.2
Release:        %autorelease
Summary:        Python's repr() for Go
License:        MIT
URL:            https://github.com/alecthomas/repr
#!RemoteAsset
Source0:        https://github.com/alecthomas/repr/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/alecthomas/repr) = %{version}

%description
Python's repr() for Go

This package attempts to represent Go values in a form that can be used
almost directly in Go source code.

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
