# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           diskv
%define go_import_path  github.com/peterbourgon/diskv

Name:           go-github-peterbourgon-diskv
Version:        3.0.1
Release:        %autorelease
Summary:        Persistent key-value store for Go
License:        MIT
URL:            https://github.com/peterbourgon/diskv
#!RemoteAsset:  sha256:a5b476653f88ab82593bd3d342cb53915f6c7a0cdd4db25bc9d6c5dde71b2c65
Source0:        https://github.com/peterbourgon/diskv/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/btree)

Provides:       go(github.com/peterbourgon/diskv) = %{version}

Requires:       go(github.com/google/btree)

%description
This package provides a disk-backed key-value store for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
