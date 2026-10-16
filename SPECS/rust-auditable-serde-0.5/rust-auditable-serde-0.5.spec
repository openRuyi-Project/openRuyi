# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name auditable-serde
%global full_version 0.5.2
%global pkgname auditable-serde-0.5

Name:           rust-auditable-serde-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "auditable-serde"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-secure-code/cargo-auditable
#!RemoteAsset:  sha256:57ba7d807ad2850c436750154dbc442eb8611527deb6dfcc4e5e0bd10d5fbf28
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(semver-1/default) >= 1.0.0
Requires:       crate(semver-1/serde) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/serde-derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.57
Requires:       crate(topological-sort-0.2/default) >= 0.2.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "auditable-serde"

%package     -n %{name}+cargo-lock
Summary:        Serialize/deserialize data encoded by `cargo auditable` - feature "cargo-lock" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cargo-lock-8) >= 8.0.2
Provides:       crate(%{pkgname}/cargo-lock) = %{version}
Provides:       crate(%{pkgname}/toml) = %{version}

%description -n %{name}+cargo-lock
This metapackage enables feature "cargo-lock" for the Rust auditable-serde crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "toml" feature.

%package     -n %{name}+cargo-metadata
Summary:        Serialize/deserialize data encoded by `cargo auditable` - feature "cargo_metadata" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cargo-metadata-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/cargo-metadata) = %{version}
Provides:       crate(%{pkgname}/from-metadata) = %{version}

%description -n %{name}+cargo-metadata
This metapackage enables feature "cargo_metadata" for the Rust auditable-serde crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "from_metadata" feature.

%package     -n %{name}+schemars
Summary:        Serialize/deserialize data encoded by `cargo auditable` - feature "schemars" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-0.8/default) >= 0.8.10
Provides:       crate(%{pkgname}/schema) = %{version}
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust auditable-serde crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "schema" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
