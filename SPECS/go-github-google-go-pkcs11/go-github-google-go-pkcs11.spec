# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-pkcs11
%define go_import_path  github.com/google/go-pkcs11

Name:           go-github-google-go-pkcs11
Version:        0.3.0
Release:        %autorelease
Summary:        PKCS#11 bindings for Go
License:        Apache-2.0
URL:            https://github.com/google/go-pkcs11
#!RemoteAsset:  sha256:9eea54a878c1876f26468270c81099e561d0e933625aa1efaac34aabababda0c
Source0:        https://github.com/google/go-pkcs11/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/go-pkcs11) = %{version}

%description
This package provides Go bindings for PKCS#11 cryptographic token interfaces.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
