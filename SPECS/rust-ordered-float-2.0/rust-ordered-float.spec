# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ordered-float
%global full_version 2.10.1
%global pkgname ordered-float-2.0

Name:           rust-ordered-float-2.0
Version:        2.10.1
Release:        %autorelease
Summary:        Rust crate "ordered-float"
License:        MIT
URL:            https://github.com/reem/rust-ordered-float
#!RemoteAsset:  sha256:68f19d67e5a2795c94e73e0bb1cc1a7edeb2e28efd39e2e1c9b7a40c1108b11c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2) >= 0.2.19
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "ordered-float"

%package     -n %{name}+arbitrary
Summary:        Wrappers for total ordering on floats - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest
Summary:        Wrappers for total ordering on floats - feature "proptest"
Requires:       crate(%{pkgname})
Requires:       crate(proptest-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/proptest)

%description -n %{name}+proptest
This metapackage enables feature "proptest" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Wrappers for total ordering on floats - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8) >= 0.8.3
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+randtest
Summary:        Wrappers for total ordering on floats - feature "randtest"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8/std) >= 0.8.3
Requires:       crate(rand-0.8/std-rng) >= 0.8.3
Provides:       crate(%{pkgname}/randtest)

%description -n %{name}+randtest
This metapackage enables feature "randtest" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv
Summary:        Wrappers for total ordering on floats - feature "rkyv"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7/size-32) >= 0.7.0
Provides:       crate(%{pkgname}/rkyv)

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars
Summary:        Wrappers for total ordering on floats - feature "schemars"
Requires:       crate(%{pkgname})
Requires:       crate(schemars-0.6/default) >= 0.6.5
Provides:       crate(%{pkgname}/schemars)

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Wrappers for total ordering on floats - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Wrappers for total ordering on floats - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ordered-float crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
