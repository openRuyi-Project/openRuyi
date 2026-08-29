# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-options
%global full_version 0.7.6
%global pkgname cargo-options-0.7

Name:           rust-cargo-options-0.7
Version:        0.7.6
Release:        %autorelease
Summary:        Rust crate "cargo-options"
License:        MIT
URL:            https://github.com/messense/cargo-options
#!RemoteAsset:  sha256:f89e1d6d6f65fe04d5e21be9de19d31a074e3b7e43aa39ee5b85f4cee16c3188
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1/default) >= 1.0.2
Requires:       crate(clap-4/default) >= 4.5.23
Requires:       crate(clap-4/derive) >= 4.5.23
Requires:       crate(clap-4/env) >= 4.5.23
Requires:       crate(clap-4/unstable-styles) >= 4.5.23
Requires:       crate(clap-4/wrap-help) >= 4.5.23
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cargo-options"

%package     -n %{name}+serde
Summary:        Reusable common Cargo command line options - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust cargo-options crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
