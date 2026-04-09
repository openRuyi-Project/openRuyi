# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           structs
%define go_import_path  github.com/fatih/structs

Name:           go-github-fatih-structs
Version:        1.1.0
Release:        %autorelease
Summary:        Utilities for Go structs
License:        MIT
URL:            https://github.com/fatih/structs
#!RemoteAsset
Source0:        https://github.com/fatih/structs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/fatih/structs) = %{version}

%description
Structs contains various utilities to work with Go (Golang) structs. It
was initially used by me to convert a struct into a
map[string]interface{}. With time I've added other utilities for
structs.  It's basically a high level package based on primitives from
the reflect package. Feel free to add new functions or improve the
existing code.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
