# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           plan9stats
%define go_import_path  github.com/lufia/plan9stats
%define commit_id       39d0f177ccd07bdf5eb6f051ab9b09651f05d6f2

Name:           go-github-lufia-plan9stats
Version:        0+git20260817.39d0f17
Release:        %autorelease
Summary:        System statistics utilities for Plan 9
License:        BSD-3-Clause
URL:            https://github.com/lufia/plan9stats
#!RemoteAsset:  sha256:4dcb7862a1f12dff4d1c819847a7c065c212cb730daf3b41c5bf53c65dd952fd
Source0:        https://github.com/lufia/plan9stats/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)

Provides:       go(github.com/lufia/plan9stats) = %{version}

%description
Plan9stats provides Go utilities for retrieving Plan 9 system statistics.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
