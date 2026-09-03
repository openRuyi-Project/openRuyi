# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           netlink
%define go_import_path  github.com/mdlayher/netlink
# Privileged integration support imports nftables, which requires netlink and
# would create a clean-build dependency cycle. Root integration tests also
# require stable access to the worker's kernel netlink resources.
%define go_test_exclude %{go_import_path}
%define go_test_exclude_glob %{go_import_path}/internal/integration*

Name:           go-github-mdlayher-netlink
Version:        1.11.2
Release:        %autorelease
Summary:        Low-level access to Linux netlink sockets for Go
License:        MIT
URL:            https://github.com/mdlayher/netlink
#!RemoteAsset:  sha256:902fd37fb72bf7b5e0e1f41579402988fcf10096c96cc927b32e8dcc820c5df1
Source0:        https://github.com/mdlayher/netlink/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mdlayher/socket)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  iproute2

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/mdlayher/socket)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)

%description
Netlink provides low-level access to Linux netlink sockets and their message
encoding from Go.

%check -a
# Compile the root package without running privileged integration tests.
go test -c -o /dev/null %{go_import_path}

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
