# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           transport
%define go_import_path  github.com/pion/transport/v2

Name:           go-github-pion-transport-v2
Version:        2.2.10
Release:        %autorelease
Summary:        Transport testing for Pion
License:        MIT
URL:            https://github.com/pion/transport
#!RemoteAsset:  sha256:112640b7644824e3e63426bfd23712bcaadab670e3171f86c34948863b5ff0ff
Source0:        https://github.com/pion/transport/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/pion/transport/v3)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/wlynxg/anet)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/pion/transport/v2) = %{version}

Requires:       go(github.com/pion/logging)
Requires:       go(github.com/wlynxg/anet)
Requires:       go(golang.org/x/net)

%description
Transport testing for Pion

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
