# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mdns
%define go_import_path  github.com/pion/mdns
%define go_test_exclude %{go_import_path}

Name:           go-github-pion-mdns
Version:        0.0.12
Release:        %autorelease
Summary:        A Go implementation of mDNS
License:        MIT
URL:            https://github.com/pion/mdns
#!RemoteAsset:  sha256:d291ea4260996731e09103beb498f6e1b9fd3643af9aa8f39e0458f95d3e1c06
Source0:        https://github.com/pion/mdns/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/pion/transport/v3)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/pion/mdns) = %{version}

Requires:       go(github.com/pion/logging)
Requires:       go(golang.org/x/net)

%description
Go mDNS implementation. The original user is Pion WebRTC, but we would love to
see it work for everyone.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
