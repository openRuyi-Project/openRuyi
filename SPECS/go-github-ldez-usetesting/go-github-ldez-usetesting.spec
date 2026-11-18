# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           usetesting
%define go_import_path  github.com/ldez/usetesting

Name:           go-github-ldez-usetesting
Version:        0.5.0
Release:        %autorelease
Summary:        Go analyzer for calls replaceable by testing package methods
License:        Apache-2.0
URL:            https://github.com/ldez/usetesting
#!RemoteAsset:  sha256:607628ffe48c5331b7b8224f72de1360c3b13b74e3ef49d4850d137f5ea6c098
Source0:        https://github.com/ldez/usetesting/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/ldez/usetesting) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for calls replaceable by testing package methods.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n usetesting-%{version}

%files
%doc readme.md
%license LICENSE
%{go_sys_gopath}/github.com/ldez/usetesting

%changelog
%autochangelog
