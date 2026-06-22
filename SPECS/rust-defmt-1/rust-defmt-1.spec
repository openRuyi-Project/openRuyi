# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name defmt
%global full_version 1.1.0
%global pkgname defmt-1

Name:           rust-defmt-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "defmt"
License:        MIT OR Apache-2.0
URL:            https://knurling.ferrous-systems.com/
#!RemoteAsset:  sha256:a6e524506490a1953d237cb87b1cfc1e46f88c18f10a22dfe0f507dc6bfc7f7f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.0
Requires:       crate(defmt-macros-1/default) >= 1.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/avoid-default-panic) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/encoding-raw) = %{version}
Provides:       crate(%{pkgname}/encoding-rzcobs) = %{version}
Provides:       crate(%{pkgname}/ip-in-core) = %{version}

%description
Source code for takopackized Rust crate "defmt"

%package     -n %{name}+unstable-test
Summary:        Highly efficient logging framework that targets resource-constrained devices, like microcontrollers - feature "unstable-test"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-macros-1/unstable-test) >= 1.1.0
Provides:       crate(%{pkgname}/unstable-test) = %{version}

%description -n %{name}+unstable-test
This metapackage enables feature "unstable-test" for the Rust defmt crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
