# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           netns
%define go_import_path  github.com/vishvananda/netns

Name:           go-github-vishvananda-netns
Version:        0.0.5
Release:        %autorelease
Summary:        Allows ultra-simple network namespace handling
License:        Apache-2.0
URL:            https://github.com/vishvananda/netns
#!RemoteAsset:  sha256:745c35e848d0decde763848ceb0347290ad48287e9640d021628f32e888dd93e
Source0:        https://github.com/vishvananda/netns/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Skip only the network namespace creation test when OBS lacks the required privilege.
# - Jvle
Patch2000:      2000-skip-netns-test-without-privileges.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/vishvananda/netns) = %{version}

Requires:       go(golang.org/x/sys)

%description
This package provides Go bindings for Linux network namespace and netlink APIs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
