# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-progress
%define go_import_path  github.com/wagoodman/go-progress
%define commit_id       10176f79b2c0

Name:           go-github-wagoodman-go-progress
Version:        0+git20260718.10176f7
Release:        %autorelease
Summary:        Simple progress utils
License:        MIT
URL:            https://github.com/wagoodman/go-progress
#!RemoteAsset:  sha256:9524f33abf451f7dc2b553dd7726c6ddd5a9f2945211f0cd2c5e272adf0effc0
Source0:        %{url}/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gookit/color)
BuildRequires:  go(github.com/sergi/go-diff)

Provides:       go(github.com/wagoodman/go-progress) = %{version}

Requires:       go(github.com/gookit/color)
Requires:       go(github.com/sergi/go-diff)

%description
Simple progress utils

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
