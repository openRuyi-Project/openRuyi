# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           liberation
%define go_import_path  codeberg.org/go-fonts/liberation

Name:           go-codeberg-go-fonts-liberation
Version:        0.5.0
Release:        %autorelease
Summary:        Liberation fonts for Go
License:        BSD-3-Clause
URL:            https://codeberg.org/go-fonts/liberation
#!RemoteAsset
Source0:        https://codeberg.org/go-fonts/liberation/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/image)

Provides:       go(codeberg.org/go-fonts/liberation) = %{version}

Requires:       go(golang.org/x/image)

%description
This package provides the liberation fonts as importable Go packages.

%files
%license LICENSE*
%doc README*
%{_datadir}/gocode/src/%{go_import_path}

%changelog
%autochangelog
