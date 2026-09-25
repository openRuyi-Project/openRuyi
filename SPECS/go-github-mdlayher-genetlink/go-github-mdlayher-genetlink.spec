# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           genetlink
%define go_import_path  github.com/mdlayher/genetlink

Name:           go-github-mdlayher-genetlink
Version:        1.0.0
Release:        %autorelease
Summary:        Generic netlink interactions and data types for Go
License:        MIT
URL:            https://github.com/mdlayher/genetlink
#!RemoteAsset:  sha256:0c9cd5060767359881c7b706491b7a4b212c75cd0305722410fbf86cefa3cb23
Source0:        https://github.com/mdlayher/genetlink/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The OBS kernel does not expose the test's hardcoded acpi_event family.
BuildOption(check):  -skip "^TestIntegrationConnConcurrentSerializeExecute$"

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mdlayher/netlink)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/mdlayher/netlink)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)

%description
Genetlink provides access to Linux generic netlink families, messages and
connections, with helpers for testing netlink clients.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
