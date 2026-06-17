# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml
%global full_version 1.1.2+spec-1.1.0
%global pkgname toml-1

Name:           rust-toml-1
Version:        1.1.2
Release:        %autorelease
Summary:        Rust crate "toml"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:81f3d15e84cbcd896376e6730314d59fb5a87f31e4b038454184435cd57defee
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-spanned-1/alloc) >= 1.1.1
Requires:       crate(toml-datetime-1/alloc) >= 1.1.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unbounded) = %{version}

%description
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
Source code for takopackized Rust crate "toml"

%package     -n %{name}+debug
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(anstream-1/default) >= 1.0.0
Requires:       crate(anstyle-1/default) >= 1.0.14
Requires:       crate(toml-parser-1/alloc) >= 1.1.2
Requires:       crate(toml-parser-1/debug) >= 1.1.2
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
Requires:       crate(toml-writer-1/alloc) >= 1.1.1
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
Requires:       crate(toml-parser-1/alloc) >= 1.1.2
Requires:       crate(winnow-1) >= 1.0.0
Provides:       crate(%{pkgname}/parse) = %{version}

%description -n %{name}+parse
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "parse" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+preserve-order
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "preserve_order"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(indexmap-2) >= 2.13.0
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+preserve-order
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "preserve_order" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/alloc) >= 1.0.228
Requires:       crate(serde-spanned-1/alloc) >= 1.1.1
Requires:       crate(serde-spanned-1/serde) >= 1.1.1
Requires:       crate(toml-datetime-1/alloc) >= 1.1.1
Requires:       crate(toml-datetime-1/serde) >= 1.1.1
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "serde" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/std) >= 2.13.0
Requires:       crate(serde-core-1/alloc) >= 1.0.228
Requires:       crate(serde-core-1/std) >= 1.0.228
Requires:       crate(serde-spanned-1/alloc) >= 1.1.1
Requires:       crate(serde-spanned-1/std) >= 1.1.1
Requires:       crate(toml-datetime-1/alloc) >= 1.1.1
Requires:       crate(toml-datetime-1/std) >= 1.1.1
Requires:       crate(toml-parser-1/alloc) >= 1.1.2
Requires:       crate(toml-parser-1/std) >= 1.1.2
Requires:       crate(toml-writer-1/alloc) >= 1.1.1
Requires:       crate(toml-writer-1/std) >= 1.1.1
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
Provides implementations of the standard Serialize/Deserialize traits for TOML data to facilitate deserializing and serializing Rust structures.
This metapackage enables feature "std" for the Rust toml crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
