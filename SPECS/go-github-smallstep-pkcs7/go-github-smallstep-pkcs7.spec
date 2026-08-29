# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pkcs7
%define go_import_path  github.com/smallstep/pkcs7
# Tests use SHA1-RSA fixtures rejected by current Go crypto verification.
%define go_test_exclude github.com/smallstep/pkcs7

Name:           go-github-smallstep-pkcs7
Version:        0.2.1
Release:        %autorelease
Summary:        PKCS#7 implementation in Go
License:        MIT
URL:            https://github.com/smallstep/pkcs7
#!RemoteAsset:  sha256:3c774ced859b47a40690e09345a311e3913b45ba69e6fe976a4d26a669ff3d3a
Source0:        https://github.com/smallstep/pkcs7/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/smallstep/pkcs7) = %{version}

Requires:       go(golang.org/x/crypto)

%description
This package provides PKCS#7 signing and encryption support for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
