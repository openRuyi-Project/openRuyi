# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_distr
%global full_version 0.4.3
%global pkgname rand-distr-0.4

Name:           rust-rand-distr-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "rand_distr"
License:        MIT OR Apache-2.0
URL:            https://rust-random.github.io/book
#!RemoteAsset:  sha256:32cb0b9bc82b0a0876c2dd994a7e7a2683d3e7390ca40e6886785ef0c7e3ee31
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/libm) >= 0.2.0
Requires:       crate(rand-0.8) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rand_distr"

%package     -n %{name}+alloc
Summary:        Sampling from random number distributions - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8/alloc) >= 0.8.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rand_distr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Sampling from random number distributions - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.103
Requires:       crate(serde-1/derive) >= 1.0.103
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand_distr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde1
Summary:        Sampling from random number distributions - feature "serde1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(rand-0.8/serde1) >= 0.8.0
Provides:       crate(%{pkgname}/serde1) = %{version}

%description -n %{name}+serde1
This metapackage enables feature "serde1" for the Rust rand_distr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Sampling from random number distributions - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(rand-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand_distr crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+std-math
Summary:        Sampling from random number distributions - feature "std_math"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/libm) >= 0.2.0
Requires:       crate(num-traits-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/std-math) = %{version}

%description -n %{name}+std-math
This metapackage enables feature "std_math" for the Rust rand_distr crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
