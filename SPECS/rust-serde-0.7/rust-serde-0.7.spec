# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde
%global full_version 0.7.15
%global pkgname serde-0.7

Name:           rust-serde-0.7
Version:        0.7.15
Release:        %autorelease
Summary:        Rust crate "serde"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/serde
#!RemoteAsset:  sha256:1b0e0732aa8ec4267f61815a396a942ba3525062e3bd5520aa8419927cfc0a92
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/collections) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Patch2000:      2000-Specify-a-concrete-compatible-Clippy-dependency.patch

%description
Source code for takopackized Rust crate "serde"

%package     -n %{name}+clippy
Summary:        Generic serialization/deserialization framework - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.166/default) >= 0.0.166
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly-testing
Summary:        Generic serialization/deserialization framework - feature "nightly-testing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clippy) = %{version}
Requires:       crate(%{pkgname}/nightly) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/nightly-testing) = %{version}

%description -n %{name}+nightly-testing
This metapackage enables feature "nightly-testing" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
