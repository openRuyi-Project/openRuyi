# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gotenv
%define go_import_path  github.com/subosito/gotenv

Name:           go-github-subosito-gotenv
Version:        1.6.0
Release:        %autorelease
Summary:        Load environment variables from .env or io.Reader in Go.
License:        MIT
URL:            https://github.com/subosito/gotenv
#!RemoteAsset
Source0:        https://github.com/subosito/gotenv/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://src.fedoraproject.org/rpms/golang-github-subosito-gotenv/blob/09207f14d1300d7c0f7407ec3de4d3bc03d1c783/f/30.patch
Patch0:         2000-Fix-tests.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/subosito/gotenv) = %{version}

Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/text)

%description
This package provides load environment variables from .env or
io.Reader in Go.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
