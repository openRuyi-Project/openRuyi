# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name indexmap
%global full_version 1.9.3
%global pkgname indexmap-1

Name:           rust-indexmap-1
Version:        1.9.3
Release:        %autorelease
Summary:        Rust crate "indexmap"
License:        Apache-2.0 OR MIT
URL:            https://github.com/bluss/indexmap
#!RemoteAsset:  sha256:bd070e393353796e801d209ad339e89596eb4c8d430d18ede6a1cced8fafbd99
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(hashbrown-0.12/raw) >= 0.12.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/test-debug) = %{version}
Provides:       crate(%{pkgname}/test-low-transition-point) = %{version}

%description
Source code for takopackized Rust crate "indexmap"

%package     -n %{name}+arbitrary
Summary:        Hash table with consistent order and fast iteration - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

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
Requires:       crate(rayon-1/default) >= 1.4.1
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-rayon
Summary:        Hash table with consistent order and fast iteration - feature "rustc-rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-rayon-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/rustc-rayon) = %{version}

%description -n %{name}+rustc-rayon
This metapackage enables feature "rustc-rayon" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Hash table with consistent order and fast iteration - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-1) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust indexmap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde-1" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
