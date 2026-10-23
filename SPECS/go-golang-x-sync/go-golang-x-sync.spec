# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sync
%define go_import_path  golang.org/x/sync

Name:           go-golang-x-sync
Version:        0.23.0
Release:        %autorelease
Summary:        Concurrency primitives supplemental to the Go standard library
License:        BSD-3-Clause
URL:            https://golang.org/x/sync
VCS:            git:https://github.com/golang/sync
#!RemoteAsset:  sha256:2375f71b6371022b8163b50ab94e04868247da28413c80e0b7d5bd97b6219542
Source0:        https://github.com/golang/sync/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(golang.org/x/sync) = %{version}
Provides:       go(golang.org/x/sync/errgroup) = %{version}
Provides:       go(golang.org/x/sync/semaphore) = %{version}

%description
This package provides supplemental Go libraries (golang.org/x/sync) that
were not included in the main distribution. It provides Go concurrency
primitives in addition to the ones provided by the language ro the "sync"
and "sync/atomic" packages.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
