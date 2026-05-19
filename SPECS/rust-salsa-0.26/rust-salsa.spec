# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name salsa
%global full_version 0.26.2
%global pkgname salsa-0.26

Name:           rust-salsa-0.26
Version:        0.26.2
Release:        %autorelease
Summary:        Rust crate "salsa"
License:        Apache-2.0 OR MIT
URL:            https://github.com/salsa-rs/salsa
#!RemoteAsset:  sha256:4612ff789805e65c87e9b38cb749a293212a615af065bed8a2001086801498c3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(boxcar-0.2/default) >= 0.2.14
Requires:       crate(crossbeam-queue-0.3/default) >= 0.3.12
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.21
Requires:       crate(hashbrown-0.17/default) >= 0.17.0
Requires:       crate(hashlink-0.10/default) >= 0.10.0
Requires:       crate(indexmap-2.0/default) >= 2.14.0
Requires:       crate(intrusive-collections-0.9/default) >= 0.9.7
Requires:       crate(parking-lot-0.12/default) >= 0.12.4
Requires:       crate(portable-atomic-1.0/default) >= 1.13.1
Requires:       crate(rustc-hash-2.0/default) >= 2.1.2
Requires:       crate(salsa-macro-rules-0.26/default) >= 0.26.2
Requires:       crate(salsa-macros-0.26/default) >= 0.26.2
Requires:       crate(smallvec-1.0/const-new) >= 1.15.1
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thin-vec-0.2/default) >= 0.2.14
Requires:       crate(tracing-0.1/std) >= 0.1.44
Requires:       crate(typeid-1.0/default) >= 1.0.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/salsa-unstable)

%description
Source code for takopackized Rust crate "salsa"

%package     -n %{name}+accumulator
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "accumulator"
Requires:       crate(%{pkgname})
Requires:       crate(salsa-macro-rules-0.26/accumulator) >= 0.26.2
Provides:       crate(%{pkgname}/accumulator)

%description -n %{name}+accumulator
This metapackage enables feature "accumulator" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compact-str
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "compact_str"
Requires:       crate(%{pkgname})
Requires:       crate(compact-str-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/compact-str)

%description -n %{name}+compact-str
This metapackage enables feature "compact_str" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/accumulator)
Requires:       crate(%{pkgname}/inventory)
Requires:       crate(%{pkgname}/macros)
Requires:       crate(%{pkgname}/rayon)
Requires:       crate(%{pkgname}/salsa-unstable)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+inventory
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "inventory"
Requires:       crate(%{pkgname})
Requires:       crate(inventory-0.3/default) >= 0.3.24
Provides:       crate(%{pkgname}/inventory)

%description -n %{name}+inventory
This metapackage enables feature "inventory" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "macros"
Requires:       crate(%{pkgname})
Requires:       crate(salsa-macros-0.26/default) >= 0.26.2
Provides:       crate(%{pkgname}/macros)

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ordermap
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "ordermap"
Requires:       crate(%{pkgname})
Requires:       crate(ordermap-1.0/default) >= 1.2.0
Provides:       crate(%{pkgname}/ordermap)

%description -n %{name}+ordermap
This metapackage enables feature "ordermap" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+persistence
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "persistence"
Requires:       crate(%{pkgname})
Requires:       crate(erased-serde-0.4/default) >= 0.4.6
Requires:       crate(salsa-macros-0.26/persistence) >= 0.26.2
Requires:       crate(serde-1.0/default) >= 1.0.219
Requires:       crate(serde-1.0/derive) >= 1.0.219
Requires:       crate(thin-vec-0.2/serde) >= 0.2.14
Provides:       crate(%{pkgname}/persistence)

%description -n %{name}+persistence
This metapackage enables feature "persistence" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.10.0
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+shuttle
Summary:        Generic framework for on-demand, incrementalized computation (experimental) - feature "shuttle"
Requires:       crate(%{pkgname})
Requires:       crate(shuttle-0.8/default) >= 0.8.1
Provides:       crate(%{pkgname}/shuttle)

%description -n %{name}+shuttle
This metapackage enables feature "shuttle" for the Rust salsa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
