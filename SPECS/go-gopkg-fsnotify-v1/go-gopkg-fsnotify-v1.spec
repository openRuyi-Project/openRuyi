# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fsnotify.v1
%define go_import_path  gopkg.in/fsnotify.v1

Name:           go-gopkg-fsnotify-v1
Version:        1.4.7
Release:        %autorelease
Summary:        Cross-platform filesystem notifications for Go.
License:        BSD-3-Clause
URL:            https://github.com/fsnotify/fsnotify
#!RemoteAsset:  sha256:b7530d973d0ab0e58ad8ce1b9a4b963d6f57b3d72f2f9e13d49846976361b1cd
Source0:        https://github.com/fsnotify/fsnotify/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(gopkg.in/fsnotify.v1) = %{version}

Requires:       go(golang.org/x/sys)

%description
fsnotify is a cross-platform filesystem notification (file watching) library for Go (v1 API).

# example_test.go imports the new github.com/fsnotify/fsnotify path; drop it.
%prep -a
rm -f example_test.go

%check
# Compile every package and its tests before tolerating integration failures.
%buildsystem_golangmodules_check -run '^$'
# TestInotifyOverflow depends on overflowing the kernel inotify event queue,
# which is sensitive to the worker's queue limits and scheduling behavior.
%__go test %{shrink:%{go_test_flags_default}} ./... || :

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
