# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uncased
%global full_version 0.9.10
%global pkgname uncased-0.9

Name:           rust-uncased-0.9
Version:        0.9.10
Release:        %autorelease
Summary:        Rust crate "uncased"
License:        MIT OR Apache-2.0
URL:            https://github.com/SergioBenitez/uncased
#!RemoteAsset:  sha256:e1b88fcfe09e89d3866a5c11019378088af2d24c3fbd4f0543f96b479ec90697
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(version-check-0.9) >= 0.9.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uncased"

%package     -n %{name}+serde
Summary:        Case-preserving, ASCII case-insensitive, no_std string types - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/with-serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust uncased crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-serde" feature.

%package     -n %{name}+with-serde-alloc
Summary:        Case-preserving, ASCII case-insensitive, no_std string types - feature "with-serde-alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/with-serde-alloc) = %{version}

%description -n %{name}+with-serde-alloc
This metapackage enables feature "with-serde-alloc" for the Rust uncased crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
