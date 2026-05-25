# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           circl
%define go_import_path  github.com/cloudflare/circl

Name:           go-github-cloudflare-circl
Version:        1.6.3
Release:        %autorelease
Summary:        CIRCL: Cloudflare Interoperable Reusable Cryptographic Library
License:        BSD-3-Clause
URL:            https://github.com/cloudflare/circl
#!RemoteAsset:  sha256:1bf5a8618060d189780981675ef41fadf80da00069e80fa85c79554ed339d955
Source0:        https://github.com/cloudflare/circl/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/bwesterb/go-ristretto)
BuildRequires:  go(github.com/mmcloughlin/avo)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/cloudflare/circl) = %{version}

Requires:       go(github.com/bwesterb/go-ristretto)
Requires:       go(github.com/mmcloughlin/avo)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
CIRCL provides a collection of cryptographic primitives written in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
