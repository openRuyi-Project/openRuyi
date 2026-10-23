# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name           go-udev
%define go_import_path  github.com/pilebones/go-udev

Name:           go-github-pilebones-go-udev
Version:        0.9.1
Release:        %autorelease
Summary:        Pure Go implementation of udev event handling
License:        GPL-3.0-only
URL:            https://github.com/pilebones/go-udev
#!RemoteAsset:  sha256:560a5d8befc5aafefa7720210c4d5c3b16fd72dae6bbabc5ca6c771eb6f42f41
Source0:        https://github.com/pilebones/go-udev/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/kr/pretty)

Provides:       go(github.com/pilebones/go-udev) = %{version}

Requires:       go(github.com/kr/pretty)

%description
Go libraries for receiving and parsing Linux udev events through netlink.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
