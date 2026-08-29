# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-config2
%global full_version 0.1.44
%global pkgname cargo-config2-0.1

Name:           rust-cargo-config2-0.1
Version:        0.1.44
Release:        %autorelease
Summary:        Rust crate "cargo-config2"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/cargo-config2
#!RemoteAsset:  sha256:25ada53f7339c78084fb37d7e17f34e76537541c4fbb02fa3a2baa14b8faad37
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.225
Requires:       crate(serde-derive-1/default) >= 1.0.225
Requires:       crate(toml-1/parse) >= 1.0.0
Requires:       crate(toml-1/serde) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cargo-config2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
