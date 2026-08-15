# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gronx
%define go_import_path  github.com/adhocore/gronx

Name:           go-github-adhocore-gronx
Version:        1.20.1
Release:        %autorelease
Summary:        Gronx is Golang cron expression parser ported from adhocore/cron-expr with task runner
License:        MIT
URL:            https://github.com/adhocore/gronx
#!RemoteAsset:  sha256:698ba7c8b869e88c31a44175e8b0699b7bca988e49f04b0d7e4d04c0218ecb03
Source0:        https://github.com/adhocore/gronx/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata

Provides:       go(github.com/adhocore/gronx) = %{version}

%description
gronx is a Go cron expression parser with a task runner and daemon supporting crontab-like task-list files. It can be used as a library or standalone executable to compute next and previous schedules.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
