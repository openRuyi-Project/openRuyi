# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossbeam-epoch
%global full_version 0.9.18
%global pkgname crossbeam-epoch-0.9

Name:           rust-crossbeam-epoch-0.9
Version:        0.9.18
Release:        %autorelease
Summary:        Rust crate "crossbeam-epoch"
License:        MIT OR Apache-2.0
URL:            https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-epoch
#!RemoteAsset:  sha256:5b82ac4a3c2ca9c3460964f020e1402edd5753411d7737aa39c3714ad1b5420e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-utils-0.8) >= 0.8.18
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "crossbeam-epoch"

%package     -n %{name}+loom
Summary:        Epoch-based garbage collection - feature "loom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/loom-crate) = %{version}
Requires:       crate(crossbeam-utils-0.8/loom) >= 0.8.18
Provides:       crate(%{pkgname}/loom) = %{version}

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust crossbeam-epoch crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loom-crate
Summary:        Epoch-based garbage collection - feature "loom-crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(loom-0.7/default) >= 0.7.1
Provides:       crate(%{pkgname}/loom-crate) = %{version}

%description -n %{name}+loom-crate
This metapackage enables feature "loom-crate" for the Rust crossbeam-epoch crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        Epoch-based garbage collection - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-utils-0.8/nightly) >= 0.8.18
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust crossbeam-epoch crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Epoch-based garbage collection - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(crossbeam-utils-0.8/std) >= 0.8.18
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust crossbeam-epoch crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
