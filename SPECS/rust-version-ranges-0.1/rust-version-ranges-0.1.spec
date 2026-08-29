# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name version-ranges
%global full_version 0.1.3
%global pkgname version-ranges-0.1

Name:           rust-version-ranges-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "version-ranges"
License:        MPL-2.0
URL:            https://github.com/pubgrub-rs/pubgrub
#!RemoteAsset:  sha256:31e9bd4e9c9ff6a2a9b5969462ba26216af3e010df0377dad8320ab515262ef8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(smallvec-1/default) >= 1.14.0
Requires:       crate(smallvec-1/union) >= 1.14.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "version-ranges"

%package     -n %{name}+proptest
Summary:        Performance-optimized type for generic version ranges and operations on them - feature "proptest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proptest-1/default) >= 1.6.0
Provides:       crate(%{pkgname}/proptest) = %{version}

%description -n %{name}+proptest
This metapackage enables feature "proptest" for the Rust version-ranges crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+semver
Summary:        Performance-optimized type for generic version ranges and operations on them - feature "semver"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(semver-1/default) >= 1.0.27
Provides:       crate(%{pkgname}/semver) = %{version}

%description -n %{name}+semver
This metapackage enables feature "semver" for the Rust version-ranges crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Performance-optimized type for generic version ranges and operations on them - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.219
Requires:       crate(serde-1/derive) >= 1.0.219
Requires:       crate(smallvec-1/serde) >= 1.14.0
Requires:       crate(smallvec-1/union) >= 1.14.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust version-ranges crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
