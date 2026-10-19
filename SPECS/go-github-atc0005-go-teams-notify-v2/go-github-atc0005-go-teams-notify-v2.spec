# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-teams-notify
%define go_import_path  github.com/atc0005/go-teams-notify/v2

Name:           go-github-atc0005-go-teams-notify-v2
Version:        2.14.0
Release:        %autorelease
Summary:        A package to send messages to a Microsoft Teams channel
License:        MIT
URL:            https://github.com/atc0005/go-teams-notify
#!RemoteAsset:  sha256:e019fa0bb270a446da3f3edbf2629d77afb95d0f37d5cdbdd4859ee237242b4b
Source0:        https://github.com/atc0005/go-teams-notify/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/atc0005/go-teams-notify/v2) = %{version}

%description
A package to send messages to a Microsoft Teams channel.

%prep -a
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
