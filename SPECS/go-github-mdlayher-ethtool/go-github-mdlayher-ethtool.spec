# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ethtool
%define go_import_path  github.com/mdlayher/ethtool

Name:           go-github-mdlayher-ethtool
Version:        0.6.1
Release:        %autorelease
Summary:        Go library for the Linux ethtool netlink interface
License:        MIT
URL:            https://github.com/mdlayher/ethtool
#!RemoteAsset:  sha256:e92e5ea85c7c90a481b6243ac132bf185a9bcf5d1df5e9a2eb548424781cd799
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mdlayher/genetlink)
BuildRequires:  go(github.com/mdlayher/netlink)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/mdlayher/ethtool) = %{version}

Requires:       go(github.com/mdlayher/genetlink)
Requires:       go(github.com/mdlayher/netlink)
Requires:       go(golang.org/x/sys)

%description
Go library for querying and configuring network devices through the Linux
ethtool generic netlink interface.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
