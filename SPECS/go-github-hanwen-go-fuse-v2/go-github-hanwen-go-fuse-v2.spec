# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-fuse
%define go_import_path  github.com/hanwen/go-fuse/v2
# These packages contain tests that require OBS to expose the FUSE control
# filesystem, enable user_allow_other, or provide stable statfs values.
# - Jvle
%define go_test_exclude %{shrink:
    %{go_import_path}/fs
    %{go_import_path}/fuse
}

Name:           go-github-hanwen-go-fuse-v2
Version:        2.11.0
Release:        %autorelease
Summary:        Go bindings for writing FUSE file systems
License:        BSD-3-Clause
URL:            https://github.com/hanwen/go-fuse
#!RemoteAsset:  sha256:62a5b972d215cbc3f550d5d251aef1239f271a7f0b57e76f16542775bd6aab20
Source0:        https://github.com/hanwen/go-fuse/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  fuse3
BuildRequires:  go(github.com/kylelemons/godebug)
BuildRequires:  go(github.com/moby/sys/mountinfo)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/hanwen/go-fuse/v2) = %{version}

Requires:       go(golang.org/x/sys)

%description
Go native bindings for the FUSE kernel module.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
