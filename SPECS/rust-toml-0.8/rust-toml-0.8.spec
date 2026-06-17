# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml
%global full_version 0.8.23
%global pkgname toml-0.8

Name:           rust-toml-0.8
Version:        0.8.23
Release:        %autorelease
Summary:        Rust crate "toml"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:dc1beb996b9d83529a9e75c17a1686767d148d70663143c7854d8b4a09ced362
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.145
Requires:       crate(serde-spanned-0.6/default) >= 0.6.9
Requires:       crate(serde-spanned-0.6/serde) >= 0.6.9
Requires:       crate(toml-datetime-0.6/default) >= 0.6.11
Requires:       crate(toml-datetime-0.6/serde) >= 0.6.11
Provides:       crate(%{pkgname}) = %{version}

%description
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
Source code for takopackized Rust crate "toml"

%package     -n %{name}+default
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/display) = %{version}
Requires:       crate(%{pkgname}/parse) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "default" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+display
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "display"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-edit-0.22/display) >= 0.22.27
Requires:       crate(toml-edit-0.22/serde) >= 0.22.27
Provides:       crate(%{pkgname}/display) = %{version}

%description -n %{name}+display
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "display" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "indexmap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/indexmap) = %{version}
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+indexmap
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "indexmap" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "preserve_order" feature.

%package     -n %{name}+parse
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "parse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-edit-0.22/parse) >= 0.22.27
Requires:       crate(toml-edit-0.22/serde) >= 0.22.27
Provides:       crate(%{pkgname}/parse) = %{version}

%description -n %{name}+parse
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "parse" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unbounded
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "unbounded"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-edit-0.22/serde) >= 0.22.27
Requires:       crate(toml-edit-0.22/unbounded) >= 0.22.27
Provides:       crate(%{pkgname}/unbounded) = %{version}

%description -n %{name}+unbounded
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "unbounded" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
