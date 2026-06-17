# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name triomphe
%global full_version 0.1.15
%global pkgname triomphe-0.1

Name:           rust-triomphe-0.1
Version:        0.1.15
Release:        %autorelease
Summary:        Rust crate "triomphe"
License:        MIT OR Apache-2.0
URL:            https://github.com/Manishearth/triomphe
#!RemoteAsset:  sha256:dd69c5aa8f924c7519d6372789a74eac5b94fb0f8fcf0d4a97eb0bfc3e785f39
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-dropck-eyepatch) = %{version}

%description
Source code for takopackized Rust crate "triomphe"

%package     -n %{name}+arc-swap
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references (originally servo_arc) - feature "arc-swap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arc-swap-1/default) >= 1.3.0
Provides:       crate(%{pkgname}/arc-swap) = %{version}

%description -n %{name}+arc-swap
This metapackage enables feature "arc-swap" for the Rust triomphe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references (originally servo_arc) - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/stable-deref-trait) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust triomphe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references (originally servo_arc) - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust triomphe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stable-deref-trait
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references (originally servo_arc) - feature "stable_deref_trait"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(stable-deref-trait-1) >= 1.1.1
Provides:       crate(%{pkgname}/stable-deref-trait) = %{version}

%description -n %{name}+stable-deref-trait
This metapackage enables feature "stable_deref_trait" for the Rust triomphe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unsize
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references (originally servo_arc) - feature "unsize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unsize-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/unsize) = %{version}

%description -n %{name}+unsize
This metapackage enables feature "unsize" for the Rust triomphe crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
