# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-tpm-keyfiles
%define commit          609e4778396fb645389f144a094132424dc3a5a9
%define go_import_path  github.com/foxboron/go-tpm-keyfiles
# Root-package tests require the optional Microsoft TPM simulator. Keep testing
# the independent subpackages while the production package is compiled by its
# Collector consumer.
%define go_test_exclude %{go_import_path}

Name:           go-github-foxboron-go-tpm-keyfiles
Version:        0+git20260811.609e477
Release:        %autorelease
Summary:        TPM 2.0 TSS keyfile library for Go
License:        MIT
URL:            https://github.com/foxboron/go-tpm-keyfiles
#!RemoteAsset:  sha256:c4288afef8af8fa19a196cab5067dc456243279f437495a6751e2ce1c25ed38d
Source0:        https://github.com/foxboron/go-tpm-keyfiles/archive/%{commit}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-tpm)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/foxboron/go-tpm-keyfiles) = %{version}

Requires:       go(github.com/google/go-tpm)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
Go-TPM-Keyfiles implements TPM 2.0 TSS keyfile encoding, decoding, signing,
sealing, and key import support for Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
