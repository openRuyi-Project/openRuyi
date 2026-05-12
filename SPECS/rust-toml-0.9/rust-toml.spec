# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-spanned-1.0/alloc) >= 1.0.4
Requires:       crate(toml-datetime-0.7/alloc) >= 0.7.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unbounded)

%description
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
Source code for takopackized Rust crate "toml"

%package     -n %{name}+debug
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(anstream-0.6/default) >= 0.6.20
Requires:       crate(anstyle-1.0/default) >= 1.0.11
Requires:       crate(toml-parser-1.0/alloc) >= 1.0.10
Requires:       crate(toml-parser-1.0/debug) >= 1.0.10
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "debug" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/display)
Requires:       crate(%{pkgname}/parse)
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "default" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+display
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "display"
Requires:       crate(%{pkgname})
Requires:       crate(toml-writer-1.0/alloc) >= 1.0.7
Provides:       crate(%{pkgname}/display)

%description -n %{name}+display
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "display" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fast-hash
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "fast_hash"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/preserve-order)
Requires:       crate(foldhash-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/fast-hash)

%description -n %{name}+fast-hash
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "fast_hash" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parse
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "parse"
Requires:       crate(%{pkgname})
Requires:       crate(toml-parser-1.0/alloc) >= 1.0.10
Requires:       crate(winnow-0.7) >= 0.7.15
Provides:       crate(%{pkgname}/parse)

%description -n %{name}+parse
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "parse" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+preserve-order
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "preserve_order"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(indexmap-2.0) >= 2.13.0
Provides:       crate(%{pkgname}/preserve-order)

%description -n %{name}+preserve-order
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "preserve_order" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/alloc) >= 1.0.228
Requires:       crate(serde-spanned-1.0/alloc) >= 1.0.4
Requires:       crate(serde-spanned-1.0/serde) >= 1.0.4
Requires:       crate(toml-datetime-0.7/alloc) >= 0.7.5
Requires:       crate(toml-datetime-0.7/serde) >= 0.7.5
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "serde" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0/std) >= 2.13.0
Requires:       crate(serde-core-1.0/alloc) >= 1.0.228
Requires:       crate(serde-core-1.0/std) >= 1.0.228
Requires:       crate(serde-spanned-1.0/alloc) >= 1.0.4
Requires:       crate(serde-spanned-1.0/std) >= 1.0.4
Requires:       crate(toml-datetime-0.7/alloc) >= 0.7.5
Requires:       crate(toml-datetime-0.7/std) >= 0.7.5
Requires:       crate(toml-parser-1.0/alloc) >= 1.0.10
Requires:       crate(toml-parser-1.0/std) >= 1.0.10
Requires:       crate(toml-writer-1.0/alloc) >= 1.0.7
Requires:       crate(toml-writer-1.0/std) >= 1.0.7
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "std" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
