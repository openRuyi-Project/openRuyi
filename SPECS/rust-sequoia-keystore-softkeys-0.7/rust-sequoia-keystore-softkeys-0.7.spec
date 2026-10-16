# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-keystore-softkeys
%global full_version 0.7.3
%global pkgname sequoia-keystore-softkeys-0.7

Name:           rust-sequoia-keystore-softkeys-0.7
Version:        0.7.3
Release:        %autorelease
Summary:        Rust crate "sequoia-keystore-softkeys"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:6c27613ad5961ba4b7968d786ade71b157658fee999dde421929c17cc90271b2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(async-trait-0.1/default) >= 0.1.0
Requires:       crate(dirs-5/default) >= 5.0.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(sequoia-keystore-backend-0.7/default) >= 0.7.0
Requires:       crate(sequoia-openpgp-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-keystore-softkeys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
