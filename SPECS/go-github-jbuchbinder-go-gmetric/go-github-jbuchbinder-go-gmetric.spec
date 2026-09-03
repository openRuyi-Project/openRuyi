# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-gmetric
%define go_import_path  github.com/jbuchbinder/go-gmetric
%define commit_id       6d69d618f698afa05957afe48c2e0d411cf0547c

Name:           go-github-jbuchbinder-go-gmetric
Version:        0+git20260819.6d69d61
Release:        %autorelease
Summary:        Native Ganglia gmetric sender for Go
License:        Apache-2.0
URL:            https://github.com/jbuchbinder/go-gmetric
#!RemoteAsset:  sha256:c10311ab75c88942598003f1ede2f0c0183dfc143581f780e4a4669714b9a2a7
Source0:        https://github.com/jbuchbinder/go-gmetric/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Go-gmetric provides native support for sending Ganglia gmetric packets from
Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
