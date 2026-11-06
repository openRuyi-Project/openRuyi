# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           transport
%define go_import_path  github.com/pion/transport/v3

Name:           go-github-pion-transport-v3
Version:        3.0.2
Release:        %autorelease
Summary:        Transport testing for Pion
License:        MIT
URL:            https://github.com/pion/transport
#!RemoteAsset:  sha256:8be56c19a6144fe89fc55a786cd0a2278fedefaf3bc0aaacf5fc15d7953510af
Source0:        https://github.com/pion/transport/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/pion/transport/v3) = %{version}

Requires:       go(github.com/pion/logging)
Requires:       go(golang.org/x/net)

%description
Transport testing for Pion

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
