# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name defmt
%global full_version 0.3.100
%global pkgname defmt-0.3

Name:           rust-defmt-0.3
Version:        0.3.100
Release:        %autorelease
Summary:        Rust crate "defmt"
License:        MIT OR Apache-2.0
URL:            https://knurling.ferrous-systems.com/
#!RemoteAsset:  sha256:f0963443817029b2024136fc4dd07a5107eb8f977eaf18fcd1fdeb11306b64ad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(defmt-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for the Rust crate "defmt"

%package     -n %{name}+alloc
Summary:        Highly efficient logging framework that targets resource-constrained devices, like microcontrollers - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust defmt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+avoid-default-panic
Summary:        Highly efficient logging framework that targets resource-constrained devices, like microcontrollers - feature "avoid-default-panic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/avoid-default-panic) >= 1.0.0
Provides:       crate(%{pkgname}/avoid-default-panic) = %{version}

%description -n %{name}+avoid-default-panic
This metapackage enables feature "avoid-default-panic" for the Rust defmt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encoding-raw
Summary:        Highly efficient logging framework that targets resource-constrained devices, like microcontrollers - feature "encoding-raw"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/encoding-raw) >= 1.0.0
Provides:       crate(%{pkgname}/encoding-raw) = %{version}

%description -n %{name}+encoding-raw
This metapackage enables feature "encoding-raw" for the Rust defmt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encoding-rzcobs
Summary:        Highly efficient logging framework that targets resource-constrained devices, like microcontrollers - feature "encoding-rzcobs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/encoding-rzcobs) >= 1.0.0
Provides:       crate(%{pkgname}/encoding-rzcobs) = %{version}

%description -n %{name}+encoding-rzcobs
This metapackage enables feature "encoding-rzcobs" for the Rust defmt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ip-in-core
Summary:        Highly efficient logging framework that targets resource-constrained devices, like microcontrollers - feature "ip_in_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/ip-in-core) >= 1.0.0
Provides:       crate(%{pkgname}/ip-in-core) = %{version}

%description -n %{name}+ip-in-core
This metapackage enables feature "ip_in_core" for the Rust defmt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-test
Summary:        Highly efficient logging framework that targets resource-constrained devices, like microcontrollers - feature "unstable-test"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-1/unstable-test) >= 1.0.0
Provides:       crate(%{pkgname}/unstable-test) = %{version}

%description -n %{name}+unstable-test
This metapackage enables feature "unstable-test" for the Rust defmt crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
