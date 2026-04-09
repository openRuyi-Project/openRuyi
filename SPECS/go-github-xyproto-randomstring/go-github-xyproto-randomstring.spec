# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           randomstring
%define go_import_path  github.com/xyproto/randomstring

Name:           go-github-xyproto-randomstring
Version:        1.2.0
Release:        %autorelease
Summary:        Generate random strings
License:        BSD-3-Clause
URL:            https://github.com/xyproto/randomstring
#!RemoteAsset
Source0:        https://github.com/xyproto/randomstring/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/xyproto/randomstring) = %{version}

%description
This package provides generate random strings.


%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
