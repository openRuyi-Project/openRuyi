# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pkcs11
%define go_import_path  github.com/miekg/pkcs11
# Integration tests require SoftHSM, which is unavailable in the build root.
%define go_test_exclude github.com/miekg/pkcs11

Name:           go-github-miekg-pkcs11
Version:        1.1.2
Release:        %autorelease
Summary:        Go wrapper for PKCS#11
License:        BSD-2-Clause
URL:            https://github.com/miekg/pkcs11
#!RemoteAsset:  sha256:7beac0f3e2e11cfdae9a065eea249287de168afe0eca5b7de734f9bd1e775b46
Source0:        https://github.com/miekg/pkcs11/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
# Tests
BuildRequires:  softhsm

Provides:       go(github.com/miekg/pkcs11) = %{version}

%description
Go bindings for the PKCS#11 cryptographic token interface.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
