# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bit-set
%global full_version 0.8.0
%global pkgname bit-set-0.8

Name:           rust-bit-set-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "bit-set"
License:        Apache-2.0 OR MIT
URL:            https://github.com/contain-rs/bit-set
#!RemoteAsset:  sha256:08807e080ed7f9d5433fa9b275196cfc35414f66a0c79d864dc51a0d825231a3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bit-vec-0.8) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bit-set"

%package     -n %{name}+serde
Summary:        Set of bits - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bit-vec-0.8/serde) >= 0.8.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bit-set crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Set of bits - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bit-vec-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bit-set crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
