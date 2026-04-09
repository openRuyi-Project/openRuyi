# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           snappy
%define go_import_path  github.com/golang/snappy

Name:           go-github-golang-snappy
Version:        1.0.0
Release:        %autorelease
Summary:        The Snappy compression format in the Go programming language.
License:        BSD-3-Clause
URL:            https://github.com/golang/snappy
#!RemoteAsset
Source0:        https://github.com/golang/snappy/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/golang/snappy) = %{version}

%description
The Snappy compression format in the Go programming language.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
