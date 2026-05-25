# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zk
%define go_import_path  github.com/go-zookeeper/zk

Name:           go-github-go-zookeeper-zk
Version:        1.0.4
Release:        %autorelease
Summary:        Native ZooKeeper client for Go
License:        BSD-3-Clause
URL:            https://github.com/go-zookeeper/zk
#!RemoteAsset:  sha256:2405d27f766505b9fa17f5b19dbe9fc08aaf7456dae0ee03177a2e659fc52b47
Source0:        https://github.com/go-zookeeper/zk/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix Go vet errors and skip integration tests that need an unpackaged
# ZooKeeper server tree; submitted upstream as
# https://github.com/go-zookeeper/zk/pull/164. - HNO3Miracle
Patch2000:      2000-Fix-non-constant-format-string-in-test.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-zookeeper/zk) = %{version}

%description
This package provides a native ZooKeeper client library for Go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
