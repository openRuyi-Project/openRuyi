# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sync
%define go_import_path  golang.org/x/sync

Name:           go-golang-x-sync
Version:        0.19.0
Release:        %autorelease
Summary:        concurrency primitives supplemental to the Go standard library
License:        BSD-3-Clause
URL:            https://golang.org/x/sync
VCS:            git:https://github.com/golang/sync
#!RemoteAsset
Source0:        https://github.com/golang/sync/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(golang.org/x/sync) = %{version}

%description
This package provides supplemental Go libraries (golang.org/x/sync) that
were not included in the main distribution. It provides Go concurrency
primitives in addition to the ones provided by the language ro the "sync"
and "sync/atomic" packages.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
