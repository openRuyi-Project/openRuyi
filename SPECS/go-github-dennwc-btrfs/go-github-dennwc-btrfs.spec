# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           btrfs
%define go_import_path  github.com/dennwc/btrfs
%define git_commit      edfb8b9e4f558a76181f59776df2b5cd8dda84da
# These tests mount Btrfs filesystems, which OBS build workers cannot do.
%define go_test_flags_default -v -skip '^(TestOpen|TestIsSubvolume|TestSubvolumes|TestCompression|TestCloneFile|TestResize)$'

Name:           go-github-dennwc-btrfs
Version:        0+git20260222.edfb8b9
Release:        %autorelease
Summary:        Go library for Btrfs filesystem information
License:        Apache-2.0
URL:            https://github.com/dennwc/btrfs
#!RemoteAsset:  sha256:05ce58df5ca34daabe564a8a9669b02f0f1bb4c3e27e00e1d36f7f378846b15e
Source0:        %{url}/archive/%{git_commit}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(prep):  -n %{_name}-%{git_commit}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/dennwc/ioctl)
BuildRequires:  go(github.com/spf13/cobra)

Provides:       go(github.com/dennwc/btrfs) = %{version}

Requires:       go(github.com/dennwc/ioctl)

%description
Go library for reading Btrfs filesystem and device information on Linux.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
