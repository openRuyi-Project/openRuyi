# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap-cargo
%global full_version 0.18.3
%global pkgname clap-cargo-0.18

Name:           rust-clap-cargo-0.18
Version:        0.18.3
Release:        %autorelease
Summary:        Rust crate "clap-cargo"
License:        MIT OR Apache-2.0
URL:            https://github.com/crate-ci/clap-cargo
#!RemoteAsset:  sha256:936551935c8258754bb8216aec040957d261f977303754b9bf1a213518388006
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1/default) >= 1.0.13

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/testing-colors) = %{version}

%description
Source code for takopackized Rust crate "clap-cargo"

%package     -n %{name}+cargo-metadata
Summary:        Re-usable CLI flags for `cargo` plugins - feature "cargo_metadata"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cargo-metadata-0.23/default) >= 0.23.0
Requires:       crate(serde-1/default) >= 1.0.210
Requires:       crate(serde-json-1/default) >= 1.0.133
Provides:       crate(%{pkgname}/cargo-metadata) = %{version}

%description -n %{name}+cargo-metadata
This metapackage enables feature "cargo_metadata" for the Rust clap-cargo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap
Summary:        Re-usable CLI flags for `cargo` plugins - feature "clap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/derive) >= 4.5.48
Requires:       crate(clap-4/std) >= 4.5.48
Provides:       crate(%{pkgname}/clap) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust clap-cargo crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
