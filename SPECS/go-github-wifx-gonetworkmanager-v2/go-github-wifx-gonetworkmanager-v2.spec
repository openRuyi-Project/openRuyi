# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name           gonetworkmanager
%define go_import_path  github.com/Wifx/gonetworkmanager/v2

Name:           go-github-wifx-gonetworkmanager-v2
Version:        2.2.0
Release:        %autorelease
Summary:        Go D-Bus bindings for NetworkManager
License:        MIT
URL:            https://github.com/Wifx/gonetworkmanager
#!RemoteAsset:  sha256:6b707575d80526891c7d2d39dcf315d9feab5fc4aa1b9d1ae12d808d511e9c4d
Source0:        https://github.com/Wifx/gonetworkmanager/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/godbus/dbus/v5)
BuildRequires:  go(github.com/google/uuid)

Provides:       go(github.com/Wifx/gonetworkmanager/v2) = %{version}

Requires:       go(github.com/godbus/dbus/v5)
Requires:       go(github.com/google/uuid)

%description
Go bindings for the NetworkManager D-Bus API, including network devices,
connections and wireless access points.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
