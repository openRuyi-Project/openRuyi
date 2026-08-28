# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gohai
%define go_import_path  github.com/DataDog/gohai
%define commit_id       4316413895ee2c3c35755fb3161f12bafe122b62

Name:           go-github-datadog-gohai
Version:        0+git20260817.4316413
Release:        %autorelease
Summary:        System information collector for Go
License:        MIT
URL:            https://github.com/DataDog/gohai
#!RemoteAsset:  sha256:a1723060f7ef4787e1edc631d8b88b25f527aa0044ad195f1f3d5c9ab9e49e84
Source0:        https://github.com/DataDog/gohai/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cihub/seelog)
BuildRequires:  go(github.com/shirou/gopsutil/v3)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/DataDog/gohai) = %{version}

Requires:       go(github.com/cihub/seelog)
Requires:       go(github.com/shirou/gopsutil/v3)
Requires:       go(golang.org/x/sys)

%description
Gohai is a Go library and command-line tool for collecting system information.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
