# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           netlink
%define go_import_path  github.com/vishvananda/netlink

Name:           go-github-vishvananda-netlink
Version:        1.3.1
Release:        %autorelease
Summary:        Provides a simple library for netlink
License:        Apache-2.0
URL:            https://github.com/vishvananda/netlink
#!RemoteAsset:  sha256:61c9832054c4a68b9459f4b60c90fef273adb1c7ab8d85a634da7220960e1186
Source0:        https://github.com/vishvananda/netlink/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# OBS workers cannot create AF_XDP raw sockets, so skip only the affected test when it gets EPERM.
Patch2000:      2000-skip-xdp-test-without-privileges.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/vishvananda/netns)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/vishvananda/netlink) = %{version}

Requires:       go(github.com/vishvananda/netns)
Requires:       go(golang.org/x/sys)

%description
This package provides Go bindings for Linux network namespace and netlink APIs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
