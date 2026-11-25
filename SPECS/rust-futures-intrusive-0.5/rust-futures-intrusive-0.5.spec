# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-intrusive
%global full_version 0.5.0
%global pkgname futures-intrusive-0.5

Name:           rust-futures-intrusive-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "futures-intrusive"
License:        MIT OR Apache-2.0
URL:            https://github.com/Matthias247/futures-intrusive
#!RemoteAsset:  sha256:1d930c203dd0b6ff06e0201a4a2fe9149b43c684fd4420555b26d21b1a02956f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(lock-api-0.4/default) >= 0.4.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "futures-intrusive"

%package     -n %{name}+alloc
Summary:        Futures based on intrusive data structures - for std and no-std environments - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/alloc) >= 0.3.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust futures-intrusive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking-lot
Summary:        Futures based on intrusive data structures - for std and no-std environments - feature "parking_lot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/parking-lot) = %{version}

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust futures-intrusive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Futures based on intrusive data structures - for std and no-std environments - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/parking-lot) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures-intrusive crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
