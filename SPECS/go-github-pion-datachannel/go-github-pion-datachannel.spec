# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           datachannel
%define go_import_path  github.com/pion/datachannel

Name:           go-github-pion-datachannel
Version:        1.5.8
Release:        %autorelease
Summary:        A Go implementation of WebRTC Data Channels
License:        MIT
URL:            https://github.com/pion/datachannel
#!RemoteAsset:  sha256:1cfe3d8ffb25604333ab080fd7e3810b241a1d3c1f468931dedfe9cb0ce482c1
Source0:        https://github.com/pion/datachannel/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/pion/sctp)
BuildRequires:  go(github.com/pion/transport/v3)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/pion/datachannel) = %{version}

Requires:       go(github.com/pion/logging)
Requires:       go(github.com/pion/sctp)

%description
A Go implementation of WebRTC Data Channels

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
