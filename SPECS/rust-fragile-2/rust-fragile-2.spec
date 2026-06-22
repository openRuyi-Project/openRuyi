# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fragile
%global full_version 2.1.0
%global pkgname fragile-2

Name:           rust-fragile-2
Version:        2.1.0
Release:        %autorelease
Summary:        Rust crate "fragile"
License:        Apache-2.0
URL:            https://github.com/mitsuhiko/fragile
#!RemoteAsset:  sha256:8878864ba14bb86e818a412bfd6f18f9eabd4ec0f008a28e8f7eb61db532fcf9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/future) = %{version}

%description
Source code for takopackized Rust crate "fragile"

%package     -n %{name}+futures-core
Summary:        Provides wrapper types for sending non-send values to other threads - feature "futures-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/default) >= 0.3.11
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust fragile crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+slab
Summary:        Provides wrapper types for sending non-send values to other threads - feature "slab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(slab-0.4/default) >= 0.4.5
Provides:       crate(%{pkgname}/slab) = %{version}

%description -n %{name}+slab
This metapackage enables feature "slab" for the Rust fragile crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stream
Summary:        Provides wrapper types for sending non-send values to other threads - feature "stream" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/future) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/stream) = %{version}

%description -n %{name}+stream
This metapackage enables feature "stream" for the Rust fragile crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
