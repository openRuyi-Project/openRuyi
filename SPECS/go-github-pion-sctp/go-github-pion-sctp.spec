# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sctp
%define go_import_path  github.com/pion/sctp

Name:           go-github-pion-sctp
Version:        1.8.19
Release:        %autorelease
Summary:        A Go implementation of SCTP
License:        MIT
URL:            https://github.com/pion/sctp
#!RemoteAsset:  sha256:0ff42252ac049066315605ad4afec3676369a493c93c15846ae2047925f57fde
Source0:        https://github.com/pion/sctp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/pion/randutil)
BuildRequires:  go(github.com/pion/transport/v3)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/pion/sctp) = %{version}

Requires:       go(github.com/pion/logging)
Requires:       go(github.com/pion/randutil)

%description
A Go implementation of SCTP

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
