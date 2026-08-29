# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-securesystemslib
%define go_import_path  github.com/secure-systems-lab/go-securesystemslib

Name:           go-github-secure-systems-lab-go-securesystemslib
Version:        0.11.0
Release:        %autorelease
Summary:        A library that provides cryptographic and general-purpose functions for Go
License:        MIT
URL:            https://github.com/secure-systems-lab/go-securesystemslib
#!RemoteAsset:  sha256:2bf9c97afec8e45f5f4b68121ac747e14e76c887024000a4a8bebf463fe2d50e
Source0:        https://github.com/secure-systems-lab/go-securesystemslib/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/codahale/rfc6979)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/secure-systems-lab/go-securesystemslib) = %{version}

Requires:       go(github.com/codahale/rfc6979)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/crypto)

%description
A library that provides cryptographic and general-purpose functions for
Go Secure Systems Lab projects at NYU.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
