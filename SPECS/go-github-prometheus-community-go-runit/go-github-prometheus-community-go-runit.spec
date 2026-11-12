# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-runit
%define go_import_path  github.com/prometheus-community/go-runit

Name:           go-github-prometheus-community-go-runit
Version:        0.1.0
Release:        %autorelease
Summary:        Go library for reading runit service status
License:        MIT
URL:            https://github.com/prometheus-community/go-runit
#!RemoteAsset:  sha256:19f5a55b65d16a7450f78c8ba47212e4017b19af4ade5ff766f07dde7e024661
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/prometheus-community/go-runit) = %{version}

%description
Go library for obtaining status information from runit-managed services.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
