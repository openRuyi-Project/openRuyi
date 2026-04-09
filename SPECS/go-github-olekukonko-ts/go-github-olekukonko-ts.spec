# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ts
%define go_import_path  github.com/olekukonko/ts
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id 78ecb04241c0121483589a30b0814836a746187d
# ioctl system call is not supported in some CI environments - 251
%define go_test_ignore_failure 1

Name:           go-github-olekukonko-ts
Version:        0+git20260107.78ecb04
Release:        %autorelease
Summary:        Simple go Application to get Terminal Size
License:        MIT
URL:            https://github.com/olekukonko/ts
#!RemoteAsset
Source0:        https://github.com/olekukonko/ts/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/olekukonko/ts) = %{version}

%description
Simple go Application to get Terminal Size. So Many Implementations do
not support windows but ts has full windows support.

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
