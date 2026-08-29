# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-crypto
%define go_import_path  github.com/ProtonMail/go-crypto
%define upstream_version  1.4.1-proton

Name:           go-github-protonmail-go-crypto
Version:        1.4.1~proton
Release:        %autorelease
Summary:        Fork of go/x/crypto, providing an up-to-date OpenPGP implementation
License:        BSD-3-Clause
URL:            https://github.com/ProtonMail/go-crypto
#!RemoteAsset:  sha256:2b7f353dca703b103c23fc2b378bcdc448abe7fb1bae0a0713ea61c5f29013f9
Source0:        https://github.com/ProtonMail/go-crypto/archive/refs/tags/v%{upstream_version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The forwarding test should use this module's OpenPGP armor package; current
# golang.org/x/crypto no longer ships golang.org/x/crypto/openpgp/armor.
# - HNO3Miracle
Patch2000:      2000-use-local-openpgp-armor-in-forwarding-test.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cloudflare/circl)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/ProtonMail/go-crypto) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp) = %{version}
Provides:       go(github.com/ProtonMail/go-crypto/openpgp/packet) = %{version}

Requires:       go(github.com/cloudflare/circl)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
go-crypto is ProtonMail's fork of golang.org/x/crypto with an updated OpenPGP
implementation and compatibility import paths for existing OpenPGP users.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
