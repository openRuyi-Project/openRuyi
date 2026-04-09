# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bbolt
%define go_import_path  go.etcd.io/bbolt
# Exclude this test as debian
# Test timeout on riscv64
%define go_test_exclude %{shrink:
    go.etcd.io/bbolt/tests/failpoint
    go.etcd.io/bbolt
}

Name:           go-github-etcd-io-bbolt
Version:        1.4.3
Release:        %autorelease
Summary:        An embedded key/value database for Go.
License:        MIT
URL:            https://github.com/etcd-io/bbolt
#!RemoteAsset
Source0:        https://github.com/etcd-io/bbolt/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.etcd.io/gofail)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(go.etcd.io/bbolt) = %{version}

%description
bbolt is a fork of Ben Johnson's Bolt key/value store. The purpose of this
fork is to provide the Go community with an active maintenance and
development target for Bolt; the goal is improved reliability and
stability. bbolt includes bug fixes, performance enhancements, and
features not found in Bolt while preserving backwards compatibility with
the Bolt API.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
