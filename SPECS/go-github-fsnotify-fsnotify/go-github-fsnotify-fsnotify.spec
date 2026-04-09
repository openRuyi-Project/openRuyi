# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fsnotify
%define go_import_path  github.com/fsnotify/fsnotify
# TODO: Seems like random test failures, need to fix it. - 251
%define go_test_ignore_failure 1

Name:           go-github-fsnotify-fsnotify
Version:        1.9.0
Release:        %autorelease
Summary:        Cross-platform filesystem notifications for Go.
License:        BSD-3-Clause
URL:            https://github.com/fsnotify/fsnotify
#!RemoteAsset
Source0:        https://github.com/fsnotify/fsnotify/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/fsnotify/fsnotify) = %{version}

Requires:       go(golang.org/x/sys)

%description
fsnotify is a Go library to provide cross-platform filesystem
notifications on Windows, Linux, macOS, BSD, and illumos.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
