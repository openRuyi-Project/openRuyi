# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-zfs
%define go_import_path  github.com/mistifyio/go-zfs/v3
# Root tests create temporary ZFS pools and require ZFS kernel privileges unavailable in OBS.
%define go_test_exclude  github.com/mistifyio/go-zfs/v3

Name:           go-github-mistifyio-go-zfs-v3
Version:        3.1.0
Release:        %autorelease
Summary:        Provides wrappers around the ZFS command line tools
License:        Apache-2.0
URL:            https://github.com/mistifyio/go-zfs
#!RemoteAsset:  sha256:5602daf2943c4085335891009472a92d9688c1de499b2b213c61fa03a146fdec
Source0:        https://github.com/mistifyio/go-zfs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/uuid)

Provides:       go(github.com/mistifyio/go-zfs/v3) = %{version}

Requires:       go(github.com/google/uuid)

%description
Go Wrapper for ZFS

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
