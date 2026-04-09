# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           anton
%define go_import_path  codeberg.org/go-fonts/anton

Name:           go-codeberg-go-fonts-anton
Version:        0.2.0
Release:        %autorelease
Summary:        Anton fonts for Go
License:        BSD-3-Clause
URL:            https://codeberg.org/go-fonts/anton
#!RemoteAsset
Source0:        https://codeberg.org/go-fonts/anton/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-v%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/image)

Provides:       go(codeberg.org/go-fonts/anton) = %{version}

Requires:       go(golang.org/x/image)

%description
This package provides the anton fonts as importable Go packages.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
