# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-lock
%global full_version 8.0.3
%global pkgname cargo-lock-8

Name:           rust-cargo-lock-8
Version:        8.0.3
Release:        %autorelease
Summary:        Rust crate "cargo-lock"
License:        Apache-2.0 OR MIT
URL:            https://rustsec.org
#!RemoteAsset:  sha256:031718ddb8f78aa5def78a09e90defe30151d1f6c672f937af4dd916429ed996
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(semver-1/default) >= 1.0.0
Requires:       crate(semver-1/serde) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/serde-derive) >= 1.0.0
Requires:       crate(toml-0.5/default) >= 0.5.0
Requires:       crate(url-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cargo-lock"

%package     -n %{name}+cli
Summary:        Self-contained Cargo.lock parser with optional dependency graph analysis - feature "cli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dependency-tree) = %{version}
Requires:       crate(%{pkgname}/gumdrop) = %{version}
Provides:       crate(%{pkgname}/cli) = %{version}

%description -n %{name}+cli
This metapackage enables feature "cli" for the Rust cargo-lock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gumdrop
Summary:        Self-contained Cargo.lock parser with optional dependency graph analysis - feature "gumdrop"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gumdrop-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/gumdrop) = %{version}

%description -n %{name}+gumdrop
This metapackage enables feature "gumdrop" for the Rust cargo-lock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+petgraph
Summary:        Self-contained Cargo.lock parser with optional dependency graph analysis - feature "petgraph" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(petgraph-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/dependency-tree) = %{version}
Provides:       crate(%{pkgname}/petgraph) = %{version}

%description -n %{name}+petgraph
This metapackage enables feature "petgraph" for the Rust cargo-lock crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dependency-tree" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
