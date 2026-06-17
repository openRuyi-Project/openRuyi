# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name strum
%global full_version 0.27.2
%global pkgname strum-0.27

Name:           rust-strum-0.27
Version:        0.27.2
Release:        %autorelease
Summary:        Rust crate "strum"
License:        MIT
URL:            https://github.com/Peternator7/strum
#!RemoteAsset:  sha256:af23d6f6c1a224baef9d3f61e287d2761385a5b88fdab4eb4c6f11aeb54c4bcf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "strum"

%package     -n %{name}+phf
Summary:        Helpful macros for working with enums and strings - feature "phf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-0.12/default) >= 0.12.0
Requires:       crate(phf-0.12/macros) >= 0.12.0
Provides:       crate(%{pkgname}/phf) = %{version}

%description -n %{name}+phf
This metapackage enables feature "phf" for the Rust strum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+strum-macros
Summary:        Helpful macros for working with enums and strings - feature "strum_macros" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(strum-macros-0.27/default) >= 0.27.0
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/strum-macros) = %{version}

%description -n %{name}+strum-macros
This metapackage enables feature "strum_macros" for the Rust strum crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
