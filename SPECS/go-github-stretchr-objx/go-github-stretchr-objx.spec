# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           objx
%define go_import_path  github.com/stretchr/objx

Name:           go-github-stretchr-objx
Version:        0.5.3
Release:        %autorelease
Summary:        Go package for dealing with maps, slices, JSON and other data.
License:        MIT
URL:            https://github.com/stretchr/objx
#!RemoteAsset
Source0:        https://github.com/stretchr/objx/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/stretchr/objx) = %{version}

%description
Objx provides the objx.Map type, which is a map[string]interface{} that
exposes a powerful Get method (among others) that allows you to easily
and quickly get access to data within the map, without having to worry
too much about type assertions, missing data, default values etc.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
