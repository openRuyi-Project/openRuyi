# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hpke
%define go_import_path  filippo.io/hpke

Name:           go-filippo-hpke
Version:        0.4.0
Release:        %autorelease
Summary:        Hybrid Public Key Encryption implementation for Go
License:        BSD-3-Clause
URL:            https://github.com/FiloSottile/hpke
#!RemoteAsset:  sha256:b91f9b3d32ab960d64aa97efbfc948957828a89d2184f13abcf652ee7dd1668f
Source0:        https://github.com/FiloSottile/hpke/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)

%description
HPKE implements Hybrid Public Key Encryption as specified by RFC 9180,
including conventional and post-quantum key encapsulation mechanisms.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
