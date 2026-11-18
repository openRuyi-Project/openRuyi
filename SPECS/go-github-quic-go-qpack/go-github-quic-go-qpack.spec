# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           qpack
%define go_import_path  github.com/quic-go/qpack
# Skip interop subpackage test requiring external qifs submodule fixtures not shipped in the tarball.
%define go_test_exclude github.com/quic-go/qpack/interop

Name:           go-github-quic-go-qpack
Version:        0.6.0
Release:        %autorelease
Summary:        This is a minimal QPACK (RFC 9204) implementation in Go
License:        MIT
URL:            https://github.com/quic-go/qpack
#!RemoteAsset:  sha256:7ee72877bf4d2b3faf47cf7c7c191a80a6211010ef22b3bbb817c57deac30651
Source0:        https://github.com/quic-go/qpack/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/quic-go/qpack) = %{version}

Requires:       go(golang.org/x/net)

%description
Minimal QPACK (RFC 9204) implementation in Go.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
