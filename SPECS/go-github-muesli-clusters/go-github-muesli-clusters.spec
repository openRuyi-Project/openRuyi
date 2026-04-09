# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           clusters
%define go_import_path  github.com/muesli/clusters
%define commit_id 2700303c1762040efdd3afdf356eb01163603fa6

Name:           go-github-muesli-clusters
Version:        0+git20200529.2700303
Release:        %autorelease
Summary:        Data structs and algorithms for clustering data observations and basic computations in n-dimensional spaces
License:        MIT
URL:            https://github.com/muesli/clusters
#!RemoteAsset
Source0:        https://github.com/muesli/clusters/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/muesli/clusters) = %{version}

%description
Data structs and algorithms for clustering data observations and basic
computations in n-dimensional spaces.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
