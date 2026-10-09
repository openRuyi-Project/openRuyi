# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hashring
%define go_import_path  github.com/serialx/hashring
%define commit_id       49a4782e9908fe098c907022a1bd7519c79803d6

Name:           go-github-serialx-hashring
Version:        0+git20260922.49a4782
Release:        %autorelease
Summary:        Consistent hashing for Go
License:        MIT
URL:            https://github.com/serialx/hashring
#!RemoteAsset:  sha256:540468a75f9f8b664ab19a87ed3ea02351c9bb08a21877fa864e6219438cc299
Source0:        https://github.com/serialx/hashring/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/serialx/hashring) = %{version}

%description
Consistent hashing for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
