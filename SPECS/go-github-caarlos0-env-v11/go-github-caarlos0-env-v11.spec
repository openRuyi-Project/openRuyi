# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           env
%define go_import_path  github.com/caarlos0/env/v11

Name:           go-github-caarlos0-env-v11
Version:        11.4.1
Release:        %autorelease
Summary:        Parse environment variables into Go structs
License:        MIT
URL:            https://github.com/caarlos0/env
#!RemoteAsset:  sha256:cf44f0e46ccb843a71569d2a7c89f3d5ffb4d40b81b694475505acfc1597745e
Source0:        https://github.com/caarlos0/env/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  --skip TestParsesEnv

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/caarlos0/env/v11) = %{version}

%description
A simple, zero-dependency Go library for parsing environment variables into structs.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
