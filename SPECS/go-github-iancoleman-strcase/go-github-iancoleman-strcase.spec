# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           strcase
%define go_import_path  github.com/iancoleman/strcase

Name:           go-github-iancoleman-strcase
Version:        0.3.0
Release:        %autorelease
Summary:        A golang package for converting to snake_case or CamelCase
License:        MIT
URL:            https://github.com/iancoleman/strcase
#!RemoteAsset
Source0:        https://github.com/iancoleman/strcase/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/iancoleman/strcase) = %{version}

%description
strcase is a go package for converting string case to various cases
(e.g. snake case (https://en.wikipedia.org/wiki/Snake_case) or camel
case (https://en.wikipedia.org/wiki/CamelCase)) to see the full
conversion table below.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
