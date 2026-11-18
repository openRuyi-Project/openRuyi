# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cron
%define go_import_path  github.com/robfig/cron/v3

Name:           go-github-robfig-cron-v3
Version:        3.0.1
Release:        %autorelease
Summary:        Implements a cron spec parser and job runner
License:        MIT
URL:            https://github.com/robfig/cron
#!RemoteAsset:  sha256:ef97328622b5eac7adfb1aa47ddab7b3f68271b9a9b76e5bc07bf2ad65bb051a
Source0:        https://github.com/robfig/cron/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
# For timezone tests.
BuildRequires:  tzdata

Provides:       go(github.com/robfig/cron/v3) = %{version}

%description
Cron spec parser and job runner for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
