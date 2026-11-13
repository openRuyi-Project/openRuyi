# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-attestation
%define go_import_path  github.com/google/go-attestation

Name:           go-github-google-go-attestation
Version:        0.6.4
Release:        %autorelease
Summary:        TPM-backed platform attestation for Go
License:        Apache-2.0
URL:            https://github.com/google/go-attestation
#!RemoteAsset:  sha256:cd0b7ad4caefc20716cf8a912dd515714a32ba6b9ad0cb675bc5c4ea4832da5b
Source0:        https://github.com/google/go-attestation/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-tpm)
BuildRequires:  go(github.com/google/go-tpm-tools)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/google/go-attestation) = %{version}
Provides:       go(github.com/google/go-attestation/attest) = %{version}
Provides:       go(github.com/google/go-attestation/attributecert) = %{version}
Provides:       go(github.com/google/go-attestation/oid) = %{version}
Provides:       go(github.com/google/go-attestation/rsa) = %{version}
Provides:       go(github.com/google/go-attestation/x509) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-tpm)
Requires:       go(github.com/google/go-tpm-tools)
Requires:       go(go.uber.org/multierr)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
Go Attestation provides TPM-backed keys, credential activation, platform
attestation, and event log parsing.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
