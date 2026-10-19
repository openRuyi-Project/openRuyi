# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ice
%define go_import_path  github.com/pion/ice/v2
%define go_test_exclude %{go_import_path}

Name:           go-github-pion-ice-v2
Version:        2.3.38
Release:        %autorelease
Summary:        A Go implementation of ICE
License:        MIT
URL:            https://github.com/pion/ice
#!RemoteAsset:  sha256:86ebc52c48553736275a6032ff5293c58b6268f37ae6fc4807e6324268d104a5
Source0:        https://github.com/pion/ice/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/pion/dtls/v2)
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/pion/mdns)
BuildRequires:  go(github.com/pion/randutil)
BuildRequires:  go(github.com/pion/stun)
BuildRequires:  go(github.com/pion/transport/v2)
BuildRequires:  go(github.com/pion/turn/v2)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/pion/ice/v2) = %{version}

Requires:       go(github.com/google/uuid)
Requires:       go(github.com/pion/dtls/v2)
Requires:       go(github.com/pion/logging)
Requires:       go(github.com/pion/mdns)
Requires:       go(github.com/pion/randutil)
Requires:       go(github.com/pion/stun)
Requires:       go(github.com/pion/transport/v2)
Requires:       go(github.com/pion/turn/v2)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/net)

%description
A Go implementation of ICE

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
