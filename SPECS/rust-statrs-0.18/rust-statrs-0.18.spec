# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name statrs
%global full_version 0.18.0
%global pkgname statrs-0.18

Name:           rust-statrs-0.18
Version:        0.18.0
Release:        %autorelease
Summary:        Rust crate "statrs"
License:        MIT
URL:            https://github.com/statrs-dev/statrs
#!RemoteAsset:  sha256:2a3fe7c28c6512e766b0874335db33c94ad7b8f9054228ae1c2abd47ce7d335e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(approx-0.5/default) >= 0.5.0
Requires:       crate(num-traits-0.2/default) >= 0.2.14
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "statrs"

%package     -n %{name}+default
Summary:        Statistical computing library for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/nalgebra) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust statrs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nalgebra
Summary:        Statistical computing library for Rust - feature "nalgebra"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nalgebra-0.33/std) >= 0.33.0
Provides:       crate(%{pkgname}/nalgebra) = %{version}

%description -n %{name}+nalgebra
This metapackage enables feature "nalgebra" for the Rust statrs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Statistical computing library for Rust - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nalgebra-0.33/rand) >= 0.33.0
Requires:       crate(nalgebra-0.33/std) >= 0.33.0
Requires:       crate(rand-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust statrs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
