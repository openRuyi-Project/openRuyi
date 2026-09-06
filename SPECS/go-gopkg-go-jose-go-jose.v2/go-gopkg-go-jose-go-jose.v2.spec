# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-jose.v2
%define go_import_path  gopkg.in/go-jose/go-jose.v2
# The command packages import the legacy gopkg.in kingpin path, which is not
# provided by the packaged kingpin module. The library packages remain tested.
%define go_test_exclude_glob %{go_import_path}/jose-util %{go_import_path}/jwk-keygen

Name:           go-gopkg-go-jose-go-jose.v2
Version:        2.6.3
Release:        %autorelease
Summary:        Go implementation of JSON Web Signature and Encryption standards
License:        Apache-2.0
URL:            https://github.com/go-jose/go-jose
#!RemoteAsset:  sha256:a0244a93fbea8621f242cc6cbc0342763961eadf16558e8dee127a141105ee55
Source0:        https://github.com/go-jose/go-jose/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix Go 1.26 vet errors in the package examples.
Patch2000:      2000-fix-non-constant-format-strings-in-examples.patch

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(gopkg.in/go-jose/go-jose.v2) = %{version}

%description
go-jose provides a Go implementation of JSON Web Signature, JSON Web
Encryption, and JSON Web Key standards.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
