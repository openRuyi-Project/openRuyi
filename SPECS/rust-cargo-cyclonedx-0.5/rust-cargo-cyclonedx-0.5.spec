# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-cyclonedx
%global full_version 0.5.9
%global pkgname cargo-cyclonedx-0.5

Name:           rust-cargo-cyclonedx-0.5
Version:        0.5.9
Release:        %autorelease
Summary:        Rust crate "cargo-cyclonedx"
License:        Apache-2.0
URL:            https://cyclonedx.org/
#!RemoteAsset:  sha256:5d162f67705f0f5038759d73bf546a083bf30e8677c2e944b416bca48d9d69a8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.75
Requires:       crate(cargo-lock-10/default) >= 10.0.1
Requires:       crate(cargo-metadata-0.18/default) >= 0.18.1
Requires:       crate(clap-4/default) >= 4.4.11
Requires:       crate(clap-4/derive) >= 4.4.11
Requires:       crate(cyclonedx-bom-0.8/default) >= 0.8.1
Requires:       crate(env-logger-0.10/default) >= 0.10.0
Requires:       crate(log-0.4/default) >= 0.4.20
Requires:       crate(once-cell-1/default) >= 1.18.0
Requires:       crate(pathdiff-0.2/camino) >= 0.2.1
Requires:       crate(pathdiff-0.2/default) >= 0.2.1
Requires:       crate(percent-encoding-2/default) >= 2.3.1
Requires:       crate(purl-0.1/package-type) >= 0.1.3
Requires:       crate(regex-1/default) >= 1.9.3
Requires:       crate(serde-1/default) >= 1.0.193
Requires:       crate(serde-1/derive) >= 1.0.193
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(time-0.3/default) >= 0.3.36
Requires:       crate(validator-0.19/default) >= 0.19.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cargo-cyclonedx"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
