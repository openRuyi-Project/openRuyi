# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goldie
%define go_import_path  github.com/sebdah/goldie/v2

Name:           go-github-sebdah-goldie-v2
Version:        2.8.0
Release:        %autorelease
Summary:        Provides test assertions based on golden files
License:        MIT
URL:            https://github.com/sebdah/goldie
#!RemoteAsset:  sha256:ae992c98bb603506265cbb17951771bda58c2ea843276bcee22eac9ebea4d243
Source0:        https://github.com/sebdah/goldie/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/sebdah/goldie/v2) = %{version}

%description
Golden test utility for Go

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
