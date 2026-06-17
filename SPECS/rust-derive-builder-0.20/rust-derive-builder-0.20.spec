# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive_builder
%global full_version 0.20.2
%global pkgname derive-builder-0.20

Name:           rust-derive-builder-0.20
Version:        0.20.2
Release:        %autorelease
Summary:        Rust crate "derive_builder"
License:        MIT OR Apache-2.0
URL:            https://github.com/colin-kiegel/rust-derive-builder
#!RemoteAsset:  sha256:507dfb09ea8b7fa618fcf76e953f4f5e192547945816d5358edffe39f6f94947
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(derive-builder-macro-0.20/default) >= 0.20.2
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "derive_builder"

%package     -n %{name}+alloc
Summary:        Rust macro to automatically implement the builder pattern for arbitrary structs - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-builder-macro-0.20/alloc) >= 0.20.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust derive_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clippy
Summary:        Rust macro to automatically implement the builder pattern for arbitrary structs - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-builder-macro-0.20/clippy) >= 0.20.2
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust derive_builder crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Rust macro to automatically implement the builder pattern for arbitrary structs - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-builder-macro-0.20/lib-has-std) >= 0.20.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust derive_builder crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
