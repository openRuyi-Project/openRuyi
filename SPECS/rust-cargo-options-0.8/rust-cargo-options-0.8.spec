# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-options
%global full_version 0.8.1
%global pkgname cargo-options-0.8

Name:           rust-cargo-options-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "cargo-options"
License:        MIT
URL:            https://github.com/messense/cargo-options
#!RemoteAsset:  sha256:b916a16b2a4b0ce91d46e42c51b7fc42e754220a4cc8bbfd1947efaafea99af7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1/default) >= 1.0.14
Requires:       crate(clap-4/default) >= 4.6.1
Requires:       crate(clap-4/derive) >= 4.6.1
Requires:       crate(clap-4/env) >= 4.6.1
Requires:       crate(clap-4/unstable-styles) >= 4.6.1
Requires:       crate(clap-4/wrap-help) >= 4.6.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cargo-options"

%package     -n %{name}+serde
Summary:        Reusable common Cargo command line options - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust cargo-options crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
