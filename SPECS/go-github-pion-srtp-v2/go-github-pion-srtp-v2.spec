# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           srtp
%define go_import_path  github.com/pion/srtp/v2

Name:           go-github-pion-srtp-v2
Version:        2.0.20
Release:        %autorelease
Summary:        A Go implementation of SRTP
License:        MIT
URL:            https://github.com/pion/srtp
#!RemoteAsset:  sha256:8156afe373b0f6f43dbbbd56deca6b32f039d9995d0b6bd3c2757c1630b5443e
Source0:        https://github.com/pion/srtp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Patch0:         0001-preserve-padding-in-session-RTP-encryption.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/pion/rtcp)
BuildRequires:  go(github.com/pion/rtp)
BuildRequires:  go(github.com/pion/transport/v2)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/pion/srtp/v2) = %{version}

Requires:       go(github.com/pion/logging)
Requires:       go(github.com/pion/rtcp)
Requires:       go(github.com/pion/rtp)
Requires:       go(github.com/pion/transport/v2)

%description
A Go implementation of SRTP

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
