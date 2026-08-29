# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rpds
%global full_version 1.2.0
%global pkgname rpds-1

Name:           rust-rpds-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "rpds"
License:        MIT
URL:            https://github.com/orium/rpds
#!RemoteAsset:  sha256:9e75f485e819d4d3015e6c0d55d02a4fd3db47c1993d9e603e0361fba2bffb34
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(archery-1/default) >= 1.2.2
Requires:       crate(archery-1/triomphe) >= 1.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "rpds"

%package     -n %{name}+rayon
Summary:        Persistent data structures with structural sharing - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(rayon-1/default) >= 1.11.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust rpds crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Persistent data structures with structural sharing - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.228
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rpds crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
