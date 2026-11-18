# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           quic-go
%define go_import_path  github.com/quic-go/quic-go

Name:           go-github-quic-go-quic-go
Version:        0.65.0
Release:        %autorelease
Summary:        QUIC protocol implementation in pure Go
License:        MIT
URL:            https://github.com/quic-go/quic-go
#!RemoteAsset:  sha256:19cb9a7f8a6bf6f46cda4a00bd186894afae692aee0ce3baf055edf66064bf9c
Source0:        https://github.com/quic-go/quic-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/quic-go/go-ossfuzz-seeds)
BuildRequires:  go(github.com/quic-go/qpack)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/mock/gomock)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/quic-go/quic-go) = %{version}

Requires:       go(github.com/quic-go/qpack)
Requires:       go(go.uber.org/mock/gomock)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)

%description
Implementation of the QUIC protocol (RFC 9000, RFC 9001, RFC 9002) and HTTP/3 in pure Go.

%check -p
# synctest, ServeMux method routing, and X25519MLKEM768 require Go 1.24+ defaults under GOPATH mode.
export GODEBUG=asynctimerchan=0,httpmuxgo121=0,tlsmlkem=1

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
