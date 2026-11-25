# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rapidhash
%global full_version 4.5.1
%global pkgname rapidhash-4

Name:           rust-rapidhash-4
Version:        4.5.1
Release:        %autorelease
Summary:        Rust crate "rapidhash"
License:        MIT OR Apache-2.0
URL:            https://github.com/hoxxep/rapidhash
#!RemoteAsset:  sha256:5da7e78a036ce858e8d55b7e7dc8ba3a88b78350fd2155d3591bbd966b58589e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustversion-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unsafe) = %{version}

%description
Source code for takopackized Rust crate "rapidhash"

%package     -n %{name}+getrandom-03
Summary:        Extremely fast, high quality, platform-independent hashing algorithm - feature "getrandom_03"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/getrandom-03) = %{version}

%description -n %{name}+getrandom-03
This metapackage enables feature "getrandom_03" for the Rust rapidhash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom-04
Summary:        Extremely fast, high quality, platform-independent hashing algorithm - feature "getrandom_04"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/getrandom-04) = %{version}

%description -n %{name}+getrandom-04
This metapackage enables feature "getrandom_04" for the Rust rapidhash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Extremely fast, high quality, platform-independent hashing algorithm - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/getrandom-03) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust rapidhash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rng
Summary:        Extremely fast, high quality, platform-independent hashing algorithm - feature "rng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/rng) = %{version}

%description -n %{name}+rng
This metapackage enables feature "rng" for the Rust rapidhash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
