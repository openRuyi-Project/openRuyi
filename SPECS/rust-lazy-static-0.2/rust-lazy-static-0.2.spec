# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lazy_static
%global full_version 0.2.11
%global pkgname lazy-static-0.2

Name:           rust-lazy-static-0.2
Version:        0.2.11
Release:        %autorelease
Summary:        Rust crate "lazy_static"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang-nursery/lazy-static.rs
#!RemoteAsset:  sha256:76f033c7ad61445c5b347c7382dd1237847eb1bce590fe50365dcb33d546be73
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "lazy_static"

%package     -n %{name}+compiletest-rs
Summary:        Macro for declaring lazily evaluated statics in Rust - feature "compiletest_rs" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compiletest-rs-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/compiletest) = %{version}
Provides:       crate(%{pkgname}/compiletest-rs) = %{version}

%description -n %{name}+compiletest-rs
This metapackage enables feature "compiletest_rs" for the Rust lazy_static crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compiletest" feature.

%package     -n %{name}+spin
Summary:        Macro for declaring lazily evaluated statics in Rust - feature "spin"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(spin-0.4/default) >= 0.4.6
Provides:       crate(%{pkgname}/spin) = %{version}

%description -n %{name}+spin
This metapackage enables feature "spin" for the Rust lazy_static crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spin-no-std
Summary:        Macro for declaring lazily evaluated statics in Rust - feature "spin_no_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/nightly) = %{version}
Requires:       crate(%{pkgname}/spin) = %{version}
Provides:       crate(%{pkgname}/spin-no-std) = %{version}

%description -n %{name}+spin-no-std
This metapackage enables feature "spin_no_std" for the Rust lazy_static crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
