# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-autocrypt
%global full_version 0.26.0
%global pkgname sequoia-autocrypt-0.26

Name:           rust-sequoia-autocrypt-0.26
Version:        0.26.0
Release:        %autorelease
Summary:        Rust crate "sequoia-autocrypt"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:11d65ff1c8589a3e505d36c8e1919483bf4a2d8d6eb65f84c3922fbdcae6928b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.21/default) >= 0.21.0
Requires:       crate(sequoia-openpgp-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-autocrypt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
