# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           now
%define go_import_path  github.com/jinzhu/now

Name:           go-github-jinzhu-now
Version:        1.1.5
Release:        %autorelease
Summary:        Now is a time toolkit for golang
License:        MIT
URL:            https://github.com/jinzhu/now
#!RemoteAsset
Source0:        https://github.com/jinzhu/now/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/jinzhu/now) = %{version}

%description
Now is a time toolkit for golang

%files
%license License*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
