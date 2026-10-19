# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           turn
%define go_import_path  github.com/pion/turn/v2
%define go_test_exclude %{go_import_path}

Name:           go-github-pion-turn-v2
Version:        2.1.6
Release:        %autorelease
Summary:        A toolkit for building TURN clients and servers in Go
License:        MIT
URL:            https://github.com/pion/turn
#!RemoteAsset:  sha256:243841be67659ad71437e818b82c4032731cf1a3ad73e948bf3abbe27a5addb5
Source0:        https://github.com/pion/turn/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/pion/randutil)
BuildRequires:  go(github.com/pion/stun)
BuildRequires:  go(github.com/pion/transport/v2)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/pion/turn/v2) = %{version}

Requires:       go(github.com/pion/logging)
Requires:       go(github.com/pion/randutil)
Requires:       go(github.com/pion/stun)
Requires:       go(github.com/pion/transport/v2)
Requires:       go(golang.org/x/sys)

%description
Pion TURN is a Go toolkit for building TURN servers and clients. We wrote it
to solve problems we had when building RTC projects.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
