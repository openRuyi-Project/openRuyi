# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uuid-rng-internal
%global full_version 1.24.1
%global pkgname uuid-rng-internal-1

Name:           rust-uuid-rng-internal-1
Version:        1.24.1
Release:        %autorelease
Summary:        Rust crate "uuid-rng-internal"
License:        Apache-2.0 OR MIT
URL:            https://github.com/uuid-rs/uuid
#!RemoteAsset:  sha256:bbb6e4d912010d7646ef4e5a0ba89bafc6d9f8fd617c53433fe2aa86d26a3b77
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uuid-rng-internal"

%package     -n %{name}+getrandom
Summary:        Private implementation details of the uuid crate - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust uuid-rng-internal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Private implementation details of the uuid crate - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust uuid-rng-internal crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
