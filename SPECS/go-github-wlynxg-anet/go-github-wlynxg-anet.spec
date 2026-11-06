# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           anet
%define go_import_path  github.com/wlynxg/anet

Name:           go-github-wlynxg-anet
Version:        0.0.3
Release:        %autorelease
Summary:        using the Go net package in the Android environment
License:        BSD-3-Clause
URL:            https://github.com/wlynxg/anet
#!RemoteAsset:  sha256:15efff7f60d1f6b0c3af2c5f5ce34779bc00309ea2ce2c128d421a5fcd72e229
Source0:        https://github.com/wlynxg/anet/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/wlynxg/anet) = %{version}

%description
Go net package in the Android environment

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
