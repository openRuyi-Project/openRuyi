# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-keystore-backend
%global full_version 0.7.0
%global pkgname sequoia-keystore-backend-0.7

Name:           rust-sequoia-keystore-backend-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "sequoia-keystore-backend"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:c55b047f9b6412c34dc7a26a42f278205cbf1e29516feab1228edccca215f500
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(async-trait-0.1/default) >= 0.1.0
Requires:       crate(env-logger-0.10/default) >= 0.10.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(futures-0.3/executor) >= 0.3.0
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(sequoia-openpgp-2) >= 2.0.0
Requires:       crate(tempfile-3/default) >= 3.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(tokio-1/default) >= 1.19.0
Requires:       crate(tokio-1/io-util) >= 1.19.0
Requires:       crate(tokio-1/macros) >= 1.19.0
Requires:       crate(tokio-1/net) >= 1.19.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.19.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-keystore-backend"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
