# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-policy-config
%global full_version 0.8.2
%global pkgname sequoia-policy-config-0.8

Name:           rust-sequoia-policy-config-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "sequoia-policy-config"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:54ecc2eeefc0ccbba225e6e57ef1cde9df78e55b315e71fd95ebebc5bd1dbbb6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(chrono-0.4/default) >= 0.4.0
Requires:       crate(sequoia-openpgp-2) >= 2.4.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(toml-0.6/default) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-policy-config"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
