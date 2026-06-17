# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name indexmap
%global full_version 2.14.0
%global pkgname indexmap-2

Name:           rust-indexmap-2
Version:        2.14.0
Release:        %autorelease
Summary:        Rust crate "indexmap"
License:        Apache-2.0 OR MIT
URL:            https://github.com/indexmap-rs/indexmap
#!RemoteAsset:  sha256:d466e9454f08e4a911e14806c24e16fba1b4c121d1ea474396f396069cf949d9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(equivalent-1) >= 1.0.0
Requires:       crate(hashbrown-0.17) >= 0.17.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/test-debug) = %{version}

%description
Source code for takopackized Rust crate "indexmap"

%package     -n %{name}+arbitrary
Summary:        Hash table with consistent order and fast iteration - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+borsh
Summary:        Hash table with consistent order and fast iteration - feature "borsh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(borsh-1) >= 1.2.0
Provides:       crate(%{pkgname}/borsh) = %{version}

%description -n %{name}+borsh
This metapackage enables feature "borsh" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Hash table with consistent order and fast iteration - feature "quickcheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quickcheck-1) >= 1.0.0
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Hash table with consistent order and fast iteration - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.9.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Hash table with consistent order and fast iteration - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.220
Requires:       crate(serde-core-1) >= 1.0.220
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sval
Summary:        Hash table with consistent order and fast iteration - feature "sval"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sval-2) >= 2.0.0
Provides:       crate(%{pkgname}/sval) = %{version}

%description -n %{name}+sval
This metapackage enables feature "sval" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
