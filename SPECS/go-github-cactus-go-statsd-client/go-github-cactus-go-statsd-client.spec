# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-statsd-client
%define go_import_path  github.com/cactus/go-statsd-client

Name:           go-github-cactus-go-statsd-client
Version:        3.2.1
Release:        %autorelease
Summary:        StatsD client for Go
License:        MIT
URL:            https://github.com/cactus/go-statsd-client
#!RemoteAsset:  sha256:8fc4f36ae20ec78721767135f0b23228b6db19ef3c05b101f071e3a1ff4659fb
Source0:        https://github.com/cactus/go-statsd-client/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/jessevdk/go-flags)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides a UDP StatsD client for Go.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
