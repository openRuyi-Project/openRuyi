# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stringish
%define go_import_path  github.com/clipperhouse/stringish

Name:           go-github-clipperhouse-stringish
Version:        0.1.1
Release:        %autorelease
Summary:        Handle strings and bytes interchangeably in Go
License:        MIT
URL:            https://github.com/clipperhouse/stringish
#!RemoteAsset
Source0:        https://github.com/clipperhouse/stringish/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/clipperhouse/stringish) = %{version}

%description
A small Go module that provides a generic type constraint for “string-
like” data, and a utf8 package that works with both strings and byte
slices without conversions.

%files
%license LICENSE*
%doc README*
%{_datadir}/gocode/src/%{go_import_path}

%changelog
%autochangelog
