# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-deadlock
%define go_import_path  github.com/sasha-s/go-deadlock

Name:           go-github-sasha-s-go-deadlock
Version:        0.3.9
Release:        %autorelease
Summary:        Online deadlock detection in go (golang)
License:        Apache-2.0
URL:            https://github.com/sasha-s/go-deadlock
#!RemoteAsset:  sha256:9174e6fd0763c59e8c8b31cc4e585fc6c14609de18fed7b3ccfbe8213bbc526c
Source0:        https://github.com/sasha-s/go-deadlock/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/petermattis/goid)

Provides:       go(github.com/sasha-s/go-deadlock) = %{version}

Requires:       go(github.com/petermattis/goid)

%description
go-deadlock provides online deadlock detection as a drop-in replacement for sync.Mutex/RWMutex.

%files
%doc Readme*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
