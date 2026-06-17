# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive_builder_macro
%global full_version 0.20.2
%global pkgname derive-builder-macro-0.20

Name:           rust-derive-builder-macro-0.20
Version:        0.20.2
Release:        %autorelease
Summary:        Rust crate "derive_builder_macro"
License:        MIT OR Apache-2.0
URL:            https://github.com/colin-kiegel/rust-derive-builder
#!RemoteAsset:  sha256:ab63b0e2bf4d5928aff72e83a7dace85d7bba5fe12dcc3c5a572d78caffd3f3c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(derive-builder-core-0.20/default) >= 0.20.2
Requires:       crate(syn-2/default) >= 2.0.15
Requires:       crate(syn-2/extra-traits) >= 2.0.15
Requires:       crate(syn-2/full) >= 2.0.15
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "derive_builder_macro"

%package     -n %{name}+alloc
Summary:        Rust macro to automatically implement the builder pattern for arbitrary structs - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-builder-core-0.20/alloc) >= 0.20.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust derive_builder_macro crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clippy
Summary:        Rust macro to automatically implement the builder pattern for arbitrary structs - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-builder-core-0.20/clippy) >= 0.20.2
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust derive_builder_macro crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lib-has-std
Summary:        Rust macro to automatically implement the builder pattern for arbitrary structs - feature "lib_has_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-builder-core-0.20/lib-has-std) >= 0.20.2
Provides:       crate(%{pkgname}/lib-has-std) = %{version}

%description -n %{name}+lib-has-std
This metapackage enables feature "lib_has_std" for the Rust derive_builder_macro crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
