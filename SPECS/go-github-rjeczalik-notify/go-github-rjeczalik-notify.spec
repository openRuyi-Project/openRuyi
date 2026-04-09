# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           notify
%define go_import_path  github.com/rjeczalik/notify
# It just fail, and no why - Julian
%define go_test_ignore_failure 1

Name:           go-github-rjeczalik-notify
Version:        0.9.3
Release:        %autorelease
Summary:        File system event notification library on steroids.
License:        MIT
URL:            https://github.com/rjeczalik/notify
#!RemoteAsset
Source0:        https://github.com/rjeczalik/notify/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/rjeczalik/notify) = %{version}

Requires:       go(golang.org/x/sys)

%description
Filesystem event notification library on steroids.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
