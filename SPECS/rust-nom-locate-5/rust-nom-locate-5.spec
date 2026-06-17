# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nom_locate
%global full_version 5.0.0
%global pkgname nom-locate-5

Name:           rust-nom-locate-5
Version:        5.0.0
Release:        %autorelease
Summary:        Rust crate "nom_locate"
License:        MIT
URL:            https://github.com/fflorent/nom_locate
#!RemoteAsset:  sha256:0b577e2d69827c4740cba2b52efaad1c4cc7c73042860b199710b3575c68438d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch0:         0001-fix-range-dependencies.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(bytecount-0.6/default) >= 0.6.0
Requires:       crate(memchr-2) >= 2.8.1
Requires:       crate(nom-8) >= 8.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "nom_locate"

%package     -n %{name}+alloc
Summary:        Special input type for nom to locate tokens - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nom-8/alloc) >= 8.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust nom_locate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generic-simd
Summary:        Special input type for nom to locate tokens - feature "generic-simd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecount-0.6/generic-simd) >= 0.6.0
Provides:       crate(%{pkgname}/generic-simd) = %{version}

%description -n %{name}+generic-simd
This metapackage enables feature "generic-simd" for the Rust nom_locate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-dispatch-simd
Summary:        Special input type for nom to locate tokens - feature "runtime-dispatch-simd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecount-0.6/runtime-dispatch-simd) >= 0.6.0
Provides:       crate(%{pkgname}/runtime-dispatch-simd) = %{version}

%description -n %{name}+runtime-dispatch-simd
This metapackage enables feature "runtime-dispatch-simd" for the Rust nom_locate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stable-deref-trait
Summary:        Special input type for nom to locate tokens - feature "stable_deref_trait"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(stable-deref-trait-1) >= 1.0.0
Provides:       crate(%{pkgname}/stable-deref-trait) = %{version}

%description -n %{name}+stable-deref-trait
This metapackage enables feature "stable_deref_trait" for the Rust nom_locate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Special input type for nom to locate tokens - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(memchr-2/use-std) >= 2.8.1
Requires:       crate(nom-8/std) >= 8.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust nom_locate crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
