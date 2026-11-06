# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           recvcheck
%define go_import_path  github.com/raeperd/recvcheck

Name:           go-github-raeperd-recvcheck
Version:        0.3.1
Release:        %autorelease
Summary:        Go linter that detects mixing pointer and value method receivers
License:        MIT
URL:            https://github.com/raeperd/recvcheck
#!RemoteAsset:  sha256:8eabd8afaa1b9e2b9e189d761f6afd8bb57259255a3e7dc97d70d880d098097b
Source0:        https://github.com/raeperd/recvcheck/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/raeperd/recvcheck) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go linter that detects mixing pointer and value method receivers.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n recvcheck-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/raeperd/recvcheck

%changelog
%autochangelog
