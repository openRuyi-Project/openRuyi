# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossbeam-epoch
%global full_version 0.8.2
%global pkgname crossbeam-epoch-0.8

Name:           rust-crossbeam-epoch-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "crossbeam-epoch"
License:        MIT OR Apache-2.0
URL:            https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-epoch
#!RemoteAsset:  sha256:058ed274caafc1f60c4997b5fc07bf7dc7cca454af7c6e81edffe5f33f70dace
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(cfg-if-0.1/default) >= 0.1.2
Requires:       crate(crossbeam-utils-0.7) >= 0.7.0
Requires:       crate(maybe-uninit-2/default) >= 2.0.0
Requires:       crate(memoffset-0.5/default) >= 0.5.0
Requires:       crate(scopeguard-1) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/sanitize) = %{version}

%description
Source code for takopackized Rust crate "crossbeam-epoch"

%package     -n %{name}+alloc
Summary:        Epoch-based garbage collection - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-utils-0.7/alloc) >= 0.7.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust crossbeam-epoch crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lazy-static
Summary:        Epoch-based garbage collection - feature "lazy_static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lazy-static-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/lazy-static) = %{version}

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust crossbeam-epoch crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        Epoch-based garbage collection - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-utils-0.7/nightly) >= 0.7.0
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust crossbeam-epoch crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Epoch-based garbage collection - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/lazy-static) = %{version}
Requires:       crate(crossbeam-utils-0.7/std) >= 0.7.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust crossbeam-epoch crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
