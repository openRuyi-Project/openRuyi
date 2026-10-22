# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gochecknoglobals
%define go_import_path  4d63.com/gochecknoglobals

Name:           go-4d63-gochecknoglobals
Version:        0.2.2
Release:        %autorelease
Summary:        Go analyzer for global variables
License:        MIT
URL:            https://github.com/leighmcculloch/gochecknoglobals
#!RemoteAsset:  sha256:122892c502a7b304e417c1484f885f1a80bca80c19e04b79dda7a03175b80934
Source0:        https://github.com/leighmcculloch/gochecknoglobals/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n gochecknoglobals-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(4d63.com/gochecknoglobals) = %{version}
Provides:       go(4d63.com/gochecknoglobals/checknoglobals) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for global variables.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
