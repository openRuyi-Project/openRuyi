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

Patch0:         2000-Fix-non-constant-format-string-in-test.patch

BuildOption(prep):  -n zk-1.0.4

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-zookeeper/zk) = %{version}


%description
Native Go Zookeeper Client Library

[Image: GoDoc] (https://godoc.org/github.com/go-zookeeper/zk?status.svg)
(https://godoc.org/github.com/go-zookeeper/zk) [Image: unittest]
(https://github.com/go-
zookeeper/zk/actions/workflows/unittest.yaml/badge.
svg?branch=master&event=push)
(https://github.com/go-zookeeper/zk/actions/workflows/unittest.yaml)
[Image: Coverage Status] (https://img.shields.io/codecov/c/github/go-
zookeeper/zk/master) (https://codecov.io/gh/go-
zookeeper/zk/branch/master)

License

3-clause BSD. See LICENSE (/LICENSE) file.


%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
