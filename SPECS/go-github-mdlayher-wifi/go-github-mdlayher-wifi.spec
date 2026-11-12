# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wifi
%define go_import_path  github.com/mdlayher/wifi

Name:           go-github-mdlayher-wifi
Version:        0.8.0
Release:        %autorelease
Summary:        Go library for Linux wireless device operations
License:        MIT
URL:            https://github.com/mdlayher/wifi
#!RemoteAsset:  sha256:f4322932e6801a754f3943508df503c6eec9a6deeb082d99b247198fefcbbafb
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mdlayher/genetlink)
BuildRequires:  go(github.com/mdlayher/netlink)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/mdlayher/wifi) = %{version}

Requires:       go(github.com/mdlayher/genetlink)
Requires:       go(github.com/mdlayher/netlink)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
Go library for interacting with Linux wireless devices through nl80211.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
