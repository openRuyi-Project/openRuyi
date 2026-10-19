# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sdp
%define go_import_path  github.com/pion/sdp/v3

Name:           go-github-pion-sdp-v3
Version:        3.0.9
Release:        %autorelease
Summary:        A Go implementation of the SDP
License:        MIT
URL:            https://github.com/pion/sdp
#!RemoteAsset:  sha256:d0de98412c90f90379297f00c7b766a8bbf129672d2e896d3bcd780d37f35e60
Source0:        https://github.com/pion/sdp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/randutil)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/pion/sdp/v3) = %{version}

Requires:       go(github.com/pion/randutil)

%description
A Go implementation of the SDP

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
