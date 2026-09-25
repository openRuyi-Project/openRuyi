# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           moniker
%define go_import_path  github.com/technosophos/moniker

Name:           go-github-technosophos-moniker
Version:        0.2.0
Release:        %autorelease
Summary:        Generate readable random names for Go applications
License:        MIT
URL:            https://github.com/technosophos/moniker
#!RemoteAsset:  sha256:c39041f48f8f024c8f71db525f382f18e94e69570a57aabe9569610397a1d2d2
Source0:        https://github.com/technosophos/moniker/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/technosophos/moniker) = %{version}

%description
Moniker generates human-readable random names from built-in word lists.
Helm 2 uses it to name releases when a name is not supplied.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
