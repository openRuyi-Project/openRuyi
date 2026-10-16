# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml
%global full_version 0.6.0
%global pkgname toml-0.6

Name:           rust-toml-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "toml"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:4fb9d890e4dc9298b70f740f615f2e05b9db37dce531f6b24fb77ac993f9f217
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.145
Requires:       crate(serde-spanned-0.6/default) >= 0.6.0
Requires:       crate(serde-spanned-0.6/serde) >= 0.6.0
Requires:       crate(toml-datetime-0.5/default) >= 0.5.1
Requires:       crate(toml-datetime-0.5/serde) >= 0.5.1

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
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "display" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-edit-0.18/default) >= 0.18.0
Requires:       crate(toml-edit-0.18/serde) >= 0.18.0
Provides:       crate(%{pkgname}/display) = %{version}
Provides:       crate(%{pkgname}/parse) = %{version}

%description -n %{name}+display
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "display" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "parse" feature.

%package     -n %{name}+indexmap
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "indexmap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-1/default) >= 1.9.1
Provides:       crate(%{pkgname}/indexmap) = %{version}
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+indexmap
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "indexmap" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "preserve_order" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
