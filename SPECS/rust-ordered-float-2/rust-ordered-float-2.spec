# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ordered-float
%global full_version 2.10.1
%global pkgname ordered-float-2

Name:           rust-ordered-float-2
Version:        2.10.1
Release:        %autorelease
Summary:        Rust crate "ordered-float"
License:        MIT
URL:            https://github.com/reem/rust-ordered-float
#!RemoteAsset:  sha256:68f19d67e5a2795c94e73e0bb1cc1a7edeb2e28efd39e2e1c9b7a40c1108b11c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2) >= 0.2.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ordered-float"

%package     -n %{name}+arbitrary
Summary:        Wrappers for total ordering on floats - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest
Summary:        Wrappers for total ordering on floats - feature "proptest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proptest-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/proptest) = %{version}

%description -n %{name}+proptest
This metapackage enables feature "proptest" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Wrappers for total ordering on floats - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8) >= 0.8.3
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+randtest
Summary:        Wrappers for total ordering on floats - feature "randtest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8/std) >= 0.8.3
Requires:       crate(rand-0.8/std-rng) >= 0.8.3
Provides:       crate(%{pkgname}/randtest) = %{version}

%description -n %{name}+randtest
This metapackage enables feature "randtest" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv
Summary:        Wrappers for total ordering on floats - feature "rkyv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.7/size-32) >= 0.7.0
Provides:       crate(%{pkgname}/rkyv) = %{version}

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars
Summary:        Wrappers for total ordering on floats - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-0.6/default) >= 0.6.5
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Wrappers for total ordering on floats - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Wrappers for total ordering on floats - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/std) >= 0.2.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
