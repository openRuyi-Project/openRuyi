# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name erased-serde
%global full_version 0.4.10
%global pkgname erased-serde-0.4

Name:           rust-erased-serde-0.4
Version:        0.4.10
Release:        %autorelease
Summary:        Rust crate "erased-serde"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/erased-serde
#!RemoteAsset:  sha256:d2add8a07dd6a8d93ff627029c51de145e12686fbc36ecb298ac22e74cf02dec
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1) >= 1.0.220
Requires:       crate(serde-core-1) >= 1.0.220
Requires:       crate(typeid-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unstable-debug) = %{version}

%description
Source code for takopackized Rust crate "erased-serde"

%package     -n %{name}+alloc
Summary:        Type-erased Serialize and Serializer traits - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/alloc) >= 1.0.220
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust erased-serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Type-erased Serialize and Serializer traits - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(serde-core-1/std) >= 1.0.220
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust erased-serde crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
