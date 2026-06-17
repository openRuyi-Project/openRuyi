# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_spanned
%global full_version 1.1.1
%global pkgname serde-spanned-1

Name:           rust-serde-spanned-1
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "serde_spanned"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:6662b5879511e06e8999a8a235d848113e942c9124f211511b16466ee2995f26
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "serde_spanned"

%package     -n %{name}+alloc
Summary:        Serde-compatible spanned Value - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/alloc) >= 1.0.228
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust serde_spanned crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Serde-compatible spanned Value - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust serde_spanned crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Serde-compatible spanned Value - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1) >= 1.0.228
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust serde_spanned crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Serde-compatible spanned Value - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(serde-core-1/std) >= 1.0.228
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust serde_spanned crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
