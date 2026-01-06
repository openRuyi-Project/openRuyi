# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-bfloat16
%define go_import_path  github.com/d4l3k/go-bfloat16
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id 690c3bdd05f13e639d272b6b05061ea57e639d2d

Name:           go-github-d4l3k-go-bfloat16
Version:        0+git20260106.690c3bd
Release:        %autorelease
Summary:        Bfloat16 conversion utilities for Go/Golang
License:        MIT
URL:            https://github.com/d4l3k/go-bfloat16
#!RemoteAsset
Source0:        https://github.com/d4l3k/go-bfloat16/archive/%{commit_id}.zip#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  unzip

Provides:       go(github.com/d4l3k/go-bfloat16) = %{version}

%description
BFloat16 conversion utilities for Go/Golang

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
