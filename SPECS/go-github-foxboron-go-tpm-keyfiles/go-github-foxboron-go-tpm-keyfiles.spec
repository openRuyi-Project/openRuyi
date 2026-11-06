# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-tpm-keyfiles
%define go_import_path  github.com/foxboron/go-tpm-keyfiles
%define commit          8c9c2d1005f4527ada79bc29681bf53d3f0b4540

Name:           go-github-foxboron-go-tpm-keyfiles
Version:        0+git20261016.8c9c2d1005f4
Release:        %autorelease
Summary:        Go implementation of the ASN.1 format for TPM 2.0 key files
License:        MIT
URL:            https://github.com/foxboron/go-tpm-keyfiles
#!RemoteAsset:  sha256:a8f4472db87a8ec44cc1027c493c237ec786bbf9660c5b8833bfd0c08bac4400
Source0:        https://github.com/foxboron/go-tpm-keyfiles/archive/8c9c2d1005f4.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-configfs-tsm)
BuildRequires:  go(github.com/google/go-tpm)
BuildRequires:  go(github.com/google/go-tpm-tools)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/foxboron/go-tpm-keyfiles) = %{version}
Provides:       go(github.com/foxboron/go-tpm-keyfiles/pkix) = %{version}
Provides:       go(github.com/foxboron/go-tpm-keyfiles/template) = %{version}

Requires:       go(github.com/google/go-configfs-tsm)
Requires:       go(github.com/google/go-tpm)
Requires:       go(github.com/google/go-tpm-tools)
Requires:       go(github.com/google/uuid)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
This library reads and writes TPM 2.0 key files and provides helpers for
loadable, importable, and sealed keys, including a crypto.Signer interface.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
