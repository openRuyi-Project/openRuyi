# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           concurrent
%define go_import_path  github.com/modern-go/concurrent

Name:           go-github-modern-go-concurrent
Version:        1.0.3
Release:        %autorelease
Summary:        concurrency utilities
License:        Apache-2.0
URL:            https://github.com/modern-go/concurrent
#!RemoteAsset
Source0:        https://github.com/modern-go/concurrent/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/modern-go/concurrent) = %{version}

%description
This package provides concurrency utilities

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
