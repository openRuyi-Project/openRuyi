# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml
%global full_version 0.9.12+spec-1.1.0
%global pkgname toml-0.9

Name:           rust-toml-0.9
Version:        0.9.12
Release:        %autorelease
Summary:        Rust crate "toml"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:cf92845e79fc2e2def6a5d828f0801e29a2f8acc037becc5ab08595c7d5e9863
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-spanned-1/alloc) >= 1.0.4
Requires:       crate(toml-datetime-0.7/alloc) >= 0.7.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unbounded) = %{version}

%description
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
Source code for takopackized Rust crate "toml"

%package     -n %{name}+debug
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(anstream-0.6/default) >= 0.6.20
Requires:       crate(anstyle-1/default) >= 1.0.11
Requires:       crate(toml-parser-1/alloc) >= 1.0.7
Requires:       crate(toml-parser-1/debug) >= 1.0.7
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "debug" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/display) = %{version}
Requires:       crate(%{pkgname}/parse) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "default" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+display
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "display"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-writer-1/alloc) >= 1.0.6
Provides:       crate(%{pkgname}/display) = %{version}

%description -n %{name}+display
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "display" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fast-hash
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "fast_hash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/preserve-order) = %{version}
Requires:       crate(foldhash-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/fast-hash) = %{version}

%description -n %{name}+fast-hash
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "fast_hash" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parse
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "parse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-parser-1/alloc) >= 1.0.7
Requires:       crate(winnow-0.7) >= 0.7.13
Provides:       crate(%{pkgname}/parse) = %{version}

%description -n %{name}+parse
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "parse" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+preserve-order
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "preserve_order"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(indexmap-2) >= 2.11.4
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+preserve-order
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "preserve_order" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/alloc) >= 1.0.225
Requires:       crate(serde-spanned-1/alloc) >= 1.0.4
Requires:       crate(serde-spanned-1/serde) >= 1.0.4
Requires:       crate(toml-datetime-0.7/alloc) >= 0.7.5
Requires:       crate(toml-datetime-0.7/serde) >= 0.7.5
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "serde" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/std) >= 2.11.4
Requires:       crate(serde-core-1/alloc) >= 1.0.225
Requires:       crate(serde-core-1/std) >= 1.0.225
Requires:       crate(serde-spanned-1/alloc) >= 1.0.4
Requires:       crate(serde-spanned-1/std) >= 1.0.4
Requires:       crate(toml-datetime-0.7/alloc) >= 0.7.5
Requires:       crate(toml-datetime-0.7/std) >= 0.7.5
Requires:       crate(toml-parser-1/alloc) >= 1.0.7
Requires:       crate(toml-parser-1/std) >= 1.0.7
Requires:       crate(toml-writer-1/alloc) >= 1.0.6
Requires:       crate(toml-writer-1/std) >= 1.0.6
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "std" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
