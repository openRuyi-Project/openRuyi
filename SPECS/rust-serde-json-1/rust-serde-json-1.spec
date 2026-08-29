# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_json
%global full_version 1.0.150
%global pkgname serde-json-1

Name:           rust-serde-json-1
Version:        1.0.150
Release:        %autorelease
Summary:        Rust crate "serde_json"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/json
#!RemoteAsset:  sha256:e8014e44b4736ed0538adeecded0fce2a272f22dc9578a7eb6b2d9993c74cfb9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(memchr-2) >= 2.0.0
Requires:       crate(serde-1) >= 1.0.220
Requires:       crate(serde-core-1) >= 1.0.220
Requires:       crate(zmij-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/arbitrary-precision) = %{version}
Provides:       crate(%{pkgname}/float-roundtrip) = %{version}
Provides:       crate(%{pkgname}/raw-value) = %{version}
Provides:       crate(%{pkgname}/unbounded-depth) = %{version}

%description
Source code for takopackized Rust crate "serde_json"

%package     -n %{name}+alloc
Summary:        JSON serialization file format - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/alloc) >= 1.0.220
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust serde_json crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        JSON serialization file format - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.2.3
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust serde_json crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+preserve-order
Summary:        JSON serialization file format - feature "preserve_order"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/indexmap) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+preserve-order
This metapackage enables feature "preserve_order" for the Rust serde_json crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        JSON serialization file format - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/std) >= 2.0.0
Requires:       crate(serde-core-1/std) >= 1.0.220
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust serde_json crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
