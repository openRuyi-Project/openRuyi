# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assert
%define go_import_path  github.com/zeebo/assert

Name:           go-github-zeebo-assert
Version:        1.3.1
Release:        %autorelease
Summary:        Helpers for tests. You don't have to like it.
License:        CC0-1.0
URL:            https://github.com/zeebo/assert
#!RemoteAsset
Source0:        https://github.com/zeebo/assert/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/zeebo/assert) = %{version}

%description
This is a helper package intended to help with testing golang packages.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
